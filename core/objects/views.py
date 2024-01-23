from core.objects.object import Object
from datetime import datetime, timezone


class Views(Object):
    def __init__(self, name):
        super().__init__(name)

    def create_metadata(self):
        metadata = {
            "name": self.name,
            "source_table": '',
            "created_at": datetime.now(timezone.utc),
            "last_modified_at": datetime.now(timezone.utc)
        }
        self.write_metadata(metadata)


if __name__ == "__main__":
    pass
