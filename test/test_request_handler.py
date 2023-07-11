import pytest
from logic.request_handler import request_handler


class TestClass:
    def test_init(self):
        tmp_var = request_handler("Jackson Miskill")
        assert tmp_var is not None

    def test_link(self):
        tmp_var = request_handler("Jackson Miskill")
        assert tmp_var.get_link() == "https://data.norfolk.gov/resource/jz6u-9g3c.json"

    def test_user(self):
        tmp_var = request_handler("Jackson Miskill")
