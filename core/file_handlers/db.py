from core.file_handlers.handler import Folders
from core.utils import get_env_variable
from datetime import datetime, timezone

import logging
import json
import os
import shutil

logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class DB:
    def __init__(self, name):
        self.name = name
        self.folder_obj = Folders()
        self.base_dir = self.folder_obj.base_dir
        self.full_path = os.path.join(self.base_dir, name)
        self.metadata_file_path = os.path.join(self.full_path, "meta_data.json")

    def create(self, replace=False):
        if self.folder_obj.check_folder_exists(self.full_path):
            if replace:
                shutil.rmtree(self.full_path)
                self.folder_obj.create_folder(self.full_path)
            else:
                raise Exception("Database already exists!!")
        else:
            self.folder_obj.create_folder(self.full_path)

        self.db_create_metadata(self.full_path)

    def db_create_metadata(self, path):
        file_name = "meta_data.json"
        metadata = {
            "name": self.name,
            "number_of_tables": 0,
            "created_at": datetime.now(timezone.utc),
            "last_modified_at": datetime.now(timezone.utc)
        }
        self.write_metadata(metadata)

    def read_metadata(self):
        with open(self.metadata_file_path) as file:
            data = json.loads(file.read())

        return data

    def write_metadata(self, metadata):
        if os.path.exists(self.full_path):
            with open(self.metadata_file_path, "w") as file:
                file.write(json.dumps(metadata, indent=4, default=str))

    def update_metadata(self):
        metadata = self.read_metadata()
        metadata['number_of_tables'] += 1
        metadata["last_modified_at"] = datetime.now(timezone.utc)

        self.write_metadata(metadata)


if __name__ == "__main__":
    db = DB("db1")
    db.create(True)
    print(db.read_metadata())
    # db.update_metadata()
    # print(db.read_metadata())

