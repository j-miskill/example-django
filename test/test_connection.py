import pytest
from trees.connection import Connection
class TestConnection:

    # Test the request function

    def testRequest(self):
        c = Connection(token = "OT1Gvi1Lw0Cu0eOkWdfIAaMZK")
        print(c)
        assert c is not None

