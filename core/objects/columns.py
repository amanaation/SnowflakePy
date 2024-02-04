from core.objects.object import Object
from datetime import datetime, timezone
from dotenv import load_dotenv

import os
load_dotenv(".table_env")


class Columns(Object):

    def __init__(self, name,
                 table_name,
                 schema_name,
                 db_name,
                 datatype,
                 constraints=None
                 ):
        super().__init__(db_name)
        self.name = name
        self.table_name = table_name
        self.schema_name = schema_name
        self.db_name = db_name
        self.base_dir = self.full_path
        self.parent_path = os.path.join(self.base_dir, schema_name, table_name)
        self.full_path = os.path.join(self.parent_path, name)
        self.metadata_file_path = os.path.join(self.full_path, "metadata.json")
        self.metadata = {
            "DATABASE": db_name,
            "SCHEMA": schema_name,
            "TABLE_NAME": name,
            "DATATYPE": datatype,
            "CONSTRAINTS": constraints,
            "CREATED": datetime.now(timezone.utc),
            "LAST_ALTERED": datetime.now(timezone.utc),
        }

    def create_metadata(self):
        self.write_metadata(self.metadata)


if __name__ == "__main__":
    tb = Columns("column1", "table2", "schema1", "db1", "integer")
    tb.create()
