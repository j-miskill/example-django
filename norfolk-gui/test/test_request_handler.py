# Testing out the requests handler that I create for this project


import pytest
from root import src_code
from src_code import request_handler


def test_init():
    rc = request_handler.request_handler()
    assert(rc.link_to_api != None)


def test_init_2():
    assert(True)
