from sodapy import Socrata
import pandas as pd
import openpyxl

class Connection:
    """
        create connection to the API
    """
    def __init__(self, token):
        self.link = "jz6u-9g3c"
        self.token = token

    def request(self, client, limit):
        try:
            return client.get(self.link, limit)
        except:
            raise Exception("Something went wrong . . . ")



