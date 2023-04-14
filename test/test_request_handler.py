# Testing out the requests handler that I create for this project


import pytest
from logic.request_handler import *


def test_assert_works():
    assert(True)


def test_init():
    rc = request_handler()
    assert(rc.link_to_api != None)
