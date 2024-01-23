from core.objects.object import Object
from datetime import datetime, timezone


class Tables(Object):
    def __init__(self, name):
        super().__init__(name)
        self.metadata = {
            "TABLE_CATALOG": "",
            "TABLE_SCHEMA": "",
            "TABLE_NAME": "",
            "TABLE_OWNER": "",
            "TABLE_TYPE": "",
            "IS_TRANSIENT": "",
            "CLUSTERING_KEY": "",
            "ROW_COUNT": "",
            "CREATED": "",
            "LAST_ALTERED": "",
            "LAST_DDL": ""
        }

    def create_metadata(self):
        self.write_metadata(self.metadata)


if __name__ == "__main__":
    pass
