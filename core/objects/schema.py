from core.objects.object import Object
from core.utils.utils import get_env_variable
from datetime import datetime, timezone
import os


class Schema(Object):
    def __init__(self, schema_name, db_name=get_env_variable("DB_NAME")):
        super().__init__(db_name)
        self.name = schema_name
        self.db_name = db_name
        self.base_dir = self.full_path
        self.parent_path = self.base_dir
        self.full_path = os.path.join(self.base_dir, schema_name)
        self.metadata_file_path = os.path.join(self.full_path, "metadata.json")

    def create_metadata(self):
        metadata = {
            "name": self.name,
            "number_of_tables": 0,
            "created_at": datetime.now(timezone.utc),
            "last_modified_at": datetime.now(timezone.utc)
        }
        self.write_metadata(metadata)


if __name__ == "__main__":
    sch = Schema('schema1', 'db1')
    sch.create(True)
