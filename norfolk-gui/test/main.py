import pytest
from src_code import request_handler
import os

if __name__ == "__main__":
    print(os.getcwd())
    rc = request_handler.request_handler()
    print(rc.link_to_api)
