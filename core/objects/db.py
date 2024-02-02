import os.path

from core.objects.object import Object
from datetime import datetime, timezone

import logging

logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class Database(Object):
    def __init__(self, name):
        super().__init__(name)
        self.db_path = os.path.join(self.base_dir, self.name)

    def create_metadata(self):
        metadata = {
            "name": self.name,
            "number_of_schemas": 0,
            "number_of_tables": 0,
            "created_at": datetime.now(timezone.utc),
            "last_modified_at": datetime.now(timezone.utc)
        }
        self.write_metadata(metadata)


if __name__ == "__main__":
    db = Database("db1")
    db.create()

