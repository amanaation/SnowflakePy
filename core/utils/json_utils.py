import json
import os


class JSON_UTILS:
    def __init__(self):
        pass

    def write(self, path, data, mode='w'):
        with open(path, mode) as file:
            file.write(json.dumps(data, indent=4, default=str))

    def read(self, path, mode='r'):
        with open(path, mode) as file:
            data = json.loads(file.read())

        return data

    def delete(self, path):
        pass