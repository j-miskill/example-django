import pytest
from ... import trees
class TestConnection:

    # Test the request function

    def testRequest(self):
        connection = connection(token = "OT1Gvi1Lw0Cu0eOkWdfIAaMZK")
        assert connection is not None

