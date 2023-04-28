import os
import ast
from dotenv import dotenv_values, find_dotenv

# ensure basedir is set to our app folder
basedir = os.path.abspath(os.path.dirname(__file__))

# throw error if .env file is not found
find_dotenv(".env", raise_error_if_not_found=True)

# load configuration from .env
config_dict = dict(dotenv_values(".env"))

# this particular key's value is a dictionary and must be evaL'd before use
config_dict['OIDC_CLIENT_KWARGS'] = ast.literal_eval(config_dict['OIDC_CLIENT_KWARGS'])

# flask loads config from a class so convert our dict to a Config class object
Config = type("Config", (object,), config_dict)
