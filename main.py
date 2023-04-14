import pytest
from logic.request_handler import *
import os

if __name__ == "__main__":
    print(os.getcwd())
    rc = request_handler()
    print(rc.link_to_api)
