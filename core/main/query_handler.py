import sqlparse


class QueryHandler:
    def __init__(self):
        self.database = ""
        self.schema = ""
        self.table = ""

    def get_query_type(self, query):
        parse = sqlparse.parse("select * from table;")
        for p in parse:
            return p.get_type()

    def execute(self, query):
        query_type = self.get_query_type(query)
        if query_type == "select":
            pass
        elif query_type == "use":
            pass
        elif query_type == "create":
            pass
        else:
            raise Exception("Invalid query!!! syntax error at line 1 position 1")
