from core.utils.utils import get_env_variable
from core.utils.json_utils import JSON_UTILS
from core.objects.object import Object
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv(".table_env")

import os


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
        self.base_dir = self.full_path
        self.full_path = os.path.join(self.base_dir, schema_name, name)
        self.metadata_file_path = os.path.join(self.full_path, "metadata.json")
        self.metadata_obj = JSON_UTILS()
        self.metadata = {
            "DATABASE": db_name,
            "SCHEMA": schema_name,
            "TABLE_NAME": name,
            "TABLE_OWNER": owner,
            "TABLE_TYPE": table_type,
            "IS_TRANSIENT": transient,
            "CLUSTERING_KEY": clustering_key,
            "ROW_COUNT": 0,
            "CREATED": datetime.now(timezone.utc),
            "LAST_ALTERED": datetime.now(timezone.utc),
            "LAST_DDL": ddl
        }

    def create_metadata(self):
        self.write_metadata(self.metadata)


if __name__ == "__main__":
    tb = Tables("t1", "schema1")
    tb.create()
