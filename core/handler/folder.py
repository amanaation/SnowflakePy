from core.utils.utils import get_env_variable
from typing import List
import os


class Folders:

    def __init__(self):
        self.base_dir = get_env_variable("DATA_FOLDER_PATH")

    def list_folders(self, path: str) -> List:
        if os.path.exists(path):
            return os.listdir(path)

    def check_folder_exists(self, path: str) -> List:
        return os.path.exists(path)

    def create_folder(self, folder_name: str):
        os.mkdir(folder_name)


if __name__ == "__main__":
    path = get_env_variable("DATA_FOLDER_PATH")
    full_path = os.path.join(path, "db")

    fld = Folders()
    # print(fld.list_folders())
    fld.create_folder(full_path)
