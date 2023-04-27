import os
import ast
from dotenv import dotenv_values

basedir = os.path.abspath(os.path.dirname(__file__))

config_dict = dict(dotenv_values(".env"))

# this key's string value must be converted to an actual dictionary before use
config_dict['OIDC_CLIENT_KWARGS'] = ast.literal_eval(config_dict['OIDC_CLIENT_KWARGS'])

Config = type("Config", (object,), config_dict)
