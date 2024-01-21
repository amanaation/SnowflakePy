import os


def get_env_variable(variable):
    from dotenv import load_dotenv
    load_dotenv()
    return os.getenv(variable, None)
