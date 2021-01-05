import json
import logging

# add additional attributes you need here
format_string = {
    "filename": "%(filename)s",
    "levelname": "%(levelname)s",
    "message": "%(message)s",
    "levelno": "%(levelno)s",
    "logger": "%(name)s",
    "pathname": "%(pathname)s",
    "funcName": "%(funcName)s"
}

# set default log level with level parameter if required
logging.basicConfig(format=json.dumps(format_string))
