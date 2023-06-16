# Handle requests to the API server for data.

from os import link
import pandas as pd
from sodapy import Socrata
import requests
import json


# These are ways I have discovered to access the data better
# value = requests.get("https://data.norfolk.gov/resource/jz6u-9g3c.json")
# print(value.content)

# client = Socrata("data.norfolk.gov", None)
# results = client.get("jz6u-9g3c", limit=2000)


class request_handler:

    LINK_TO_API = "https://data.norfolk.gov/resource/jz6u-9g3c.json"

    def __init__(self):
        print("Initialized")

    def get_data(self):
        data = requests.post(self.LINK_TO_API)
        return data.text
