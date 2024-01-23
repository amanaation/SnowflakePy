from core.handler.folder import Folders
from core.utils.json_utils import JSON_UTILS
from datetime import datetime, timezone
import os
import shutil


class Object:
    def __init__(self, name):
        self.name = name
        self.folder_obj = Folders()
        self.base_dir = self.folder_obj.base_dir
        self.full_path = os.path.join(self.base_dir, name)
        self.metadata_file_path = os.path.join(self.full_path, "metadata.json")
        self.metadata_obj = JSON_UTILS()

    def create(self, replace=False):
        if self.folder_obj.check_folder_exists(self.full_path):
            if replace:
                shutil.rmtree(self.full_path)
                self.folder_obj.create_folder(self.full_path)
            else:
                raise Exception("Database already exists!!")
        else:
            self.folder_obj.create_folder(self.full_path)
        self.create_metadata()

    def create_metadata(self):
        metadata = {
            "name": self.name,
            "number_of_tables": 0,
            "created_at": datetime.now(timezone.utc),
            "last_modified_at": datetime.now(timezone.utc)
        }
        self.write_metadata(metadata)

    def write_metadata(self, metadata):
        if os.path.exists(self.full_path):
            self.metadata_obj.write(self.metadata_file_path, metadata)

    def read_metadata(self):
        return self.metadata_obj.read(self.metadata_file_path)

    def update_metadata(self):
        # metadata = self.read_metadata()
        # metadata['number_of_tables'] += 1
        # metadata["last_modified_at"] = datetime.now(timezone.utc)
        #
        # self.write_metadata(metadata)
        pass

    def read(self):
        pass

    def drop(self):
        pass

    def truncate(self):
        pass

    def alter(self):
        pass
