from core.utils.utils import get_env_variable
import pandas as pd
import numpy as np

class Clustering:
    def __init__(self):
        self.default_batch_size = int(get_env_variable("DEFAULT_CLUSTER_SIZE"))

    def detect_clustering_key(self, column_info, data):
        clustering_info = dict()
        for datatype in column_info:
            if "date" in datatype or "time" in datatype:
                type_clustering_info = self.group_by_timestamp_column(column_info[datatype])

            clustering_info.update(type_clustering_info)

        clustering_key = max(clustering_info, key=clustering_info.get)
        return clustering_key

    def group_by_timestamp_column(self, data):
        group_by_levels = ['YE', 'QE', 'ME', 'W', 'D']
        column_group_by_count = {}
        for column in data.columns():
            index = pd.to_datetime(data[column].to_list())
            data.index = index

            for group_by_level in group_by_levels:
                group_by_data = data[column].resample(group_by_level)
                max_count = group_by_data.count().max()
                if max_count <= self.default_batch_size:
                    column_group_by_count[column] = {"frequency": group_by_level, "max_count": max_count}
                    break

        return column_group_by_count

    def group_by_integer_column(self, data):
        bins = 2
        column_group_by_count = {}

        for column in data.columns():
            while True:
                bin_edges = np.histogram_bin_edges(data[column], bins=bins)
                hist, _ = np.histogram(data[column], bins=bin_edges)

                if max(hist) <= self.default_batch_size:
                    column_group_by_count[column] = {"frequency": bin_edges}

                bins += 1
        return column_group_by_count

    def group_by_string_column(self, data):
        for column in data.columns():
            pass


import random

import pandas as pd
from datetime import datetime, timedelta
df = {"columns": [random.randint(1, 10000) for x in range(1000)]}
ts_data = []
ts_data2 = []
for x in range(1000):
    break
    timestamp = datetime.now()
    randint = random.randrange(-365, 365)
    timestamp = timestamp + timedelta(days=randint)
    ts_data.append(timestamp)

    randint2 = random.randrange(-365, 365)
    timestamp2 = timestamp + timedelta(days=randint2)
    ts_data2.append(timestamp2)


# df = {"columns": ts_data, "columns2": ts_data2}
# print(df)
df = pd.DataFrame(df)
cls = Clustering()
print(cls.group_by_integer_column(df, ["columns"]))
# print(cls.group_by_timestamp_column(df, ["columns", "columns2"]))
