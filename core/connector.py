from core.objects.db import DB
from core.objects.tables import Tables
from core.objects.schema import Schema
from enum import Enum


class Controller(Enum):
    db = DB
    table = Tables
    schema = Schema
