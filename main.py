import pytest
from logic.request_handler import *
import os

if __name__ == "__main__":
    print(os.getcwd())
    rc = request_handler()
    print(rc.LINK_TO_API)
    data = rc.get_data()
    print(data)
