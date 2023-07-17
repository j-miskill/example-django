import pytest
from logic import request_handler


class TestClass:
    def test_init(self):
        tmp_var = request_handler.request_handler("Jackson Miskill")
        assert tmp_var is not None

    def test_link(self):
        tmp_var = request_handler.request_handler("Jackson Miskill")
        assert tmp_var.get_link() == "https://data.norfolk.gov/resource/jz6u-9g3c.json"

    def test_user(self):
        tmp_var = request_handler.request_handler("Jackson Miskill")
        assert tmp_var.get_user() == "Jackson Miskill"
