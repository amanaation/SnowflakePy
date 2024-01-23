from enum import Enum


class Metadata(Enum):
    pass


def db_metadata() -> dict:
    return {
        "DB_NAME": "",
        "DB_OWNER": "",
        "DB_CREATED": "",
        "DB_LAST_ALTERED": "",
    }


def schema_metadata() -> dict:
    db_meta = db_metadata()
    schema_meta = {
        "SCHEMA_NAME": "",
        "SCHEMA_OWNER": "",
        "SCHEMA_CREATED": "",
        "SCHEMA_LAST_ALTERED": "",
    }
    db_meta.update(schema_meta)
    return db_meta


def table_metadata() -> dict:
    table_meta = {
        "TABLE_NAME": "",
        "TABLE_OWNER": "",
        "TABLE_TYPE": "",
        "IS_TRANSIENT": "",
        "CLUSTERING_KEY": "",
        "ROW_COUNT": "",
        "TABLE_CREATED": "",
        "TABLE_LAST_ALTERED": "",
        "LAST_DDL": ""
    }

    schema_meta = schema_metadata()
    schema_meta.update(table_meta)
    return schema_meta
