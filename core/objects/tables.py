from core.objects.object import Object
from core.objects.columns import Columns
from core.utils.utils import get_env_variable
from datetime import datetime, timezone
from dotenv import load_dotenv

import json
import os

load_dotenv(".table_env")


class Tables(Object):

    def __init__(self, name,
                 schema_name=get_env_variable("SCHEMA_NAME"),
                 db_name=get_env_variable("DB_NAME"),
                 ddl="",
                 owner=os.getenv("USER_NAME"),
                 table_type="persistent",
                 transient=False,
                 clustering_key=None):
        super().__init__(db_name)
        self.name = name
        self.schema_name = schema_name
        self.db_name = db_name
        self.base_dir = self.full_path
        self.parent_path = os.path.join(self.base_dir, schema_name)
        self.full_path = os.path.join(self.base_dir, schema_name, name)
        self.metadata_file_path = os.path.join(self.full_path, "metadata.json")
        if os.path.exists(self.metadata_file_path):
            self.metadata_file_path = self.read_metadata()
        else:
            self.metadata = {
                "DATABASE": db_name,
                "SCHEMA": schema_name,
                "TABLE_NAME": name,
                "TABLE_OWNER": owner,
                "TABLE_TYPE": table_type,
                "IS_TRANSIENT": transient,
                "CLUSTERING_KEY": clustering_key,
                "ROW_COUNT": 0,
                "NUMBER_OF_PARTITIONS": 0,
                "CREATED": datetime.now(timezone.utc),
                "LAST_ALTERED": datetime.now(timezone.utc),
                "LAST_DDL": ddl
            }

    def add_column(self, column_name, datatype, constraint=None):
        column = Columns(column_name, self.name, self.schema_name, self.db_name, datatype, constraint)
        column.create()

    def get_column(self):
        column_metadata = []
        for column in os.listdir(self.full_path):
            column_path = os.path.join(self.full_path, column)
            if os.path.isdir(column_path):
                metadata_path = os.path.join(column_path, 'metadata.json')

                with open(metadata_path) as file:
                    data = json.loads(file.read())

                dynamic_column_class = type('Column', (), data)
                column_metadata.append(dynamic_column_class)

    def create_metadata(self):
        self.write_metadata(self.metadata)

    def update_metadata(self):
        pass

    def get_new_partition_name(self, last_partition_name):
        last_partition_count = last_partition_name.split("partition")[-1]
        new_partition_count = int(last_partition_count) + 1

        return f"partition{new_partition_count}"

    def get_sorted_files(self, files_list):
        sorted_files = sorted(files_list, key=lambda x: os.path.getctime(x), reverse=True)
        return sorted_files

    def get_latest_partition(self, column_partitions_files_path):
        files = self.get_sorted_files(column_partitions_files_path)
        return files[0]

    def get_partition_count(self):
        return self.metadata["NUMBER_OF_PARTITIONS"]

    def create_partitions(self, column, data, partition_size=int(os.getenv("DEFAULT_CLUSTER_SIZE"))):
        partitions_count = self.get_partition_count()
        partition_name = "partition"

        for i in range(0, len(data), partition_size):
            print(data[i: i + partition_size])
        pass

    def detect_clustering_key(self, column_info):
        pass

    def get_clustering_key(self, column_info):
        if self.metadata["CLUSTERING_KEY"]:
            return self.metadata["CLUSTERING_KEY"]
        else:
            self.detect_clustering_key(column_info)

    def insert_data(self, data, column_info):
        if self.get_partition_count():  # if partition count is 0 then its first time load then we need to detect the clustering key
            pass

        for column in column_info:
            self.create_partitions(column, data[column])

        pass


if __name__ == "__main__":
    tb = Tables("table2", "schema1", "db1")
    # tb.create()
    columns = [
        {
            "column_name": "column1",
            "datatype": "int",
        },
        {
            "column_name": "column2",
            "datatype": "int",
        },
        {
            "column_name": "column3",
            "datatype": "int",
        },
        {
            "column_name": "column4",
            "datatype": "int",
        },

    ]
    # for column in columns:
    #     tb.add_column(**column)
    tb.get_column()
