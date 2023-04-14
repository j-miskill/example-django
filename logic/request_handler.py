# This is the file I will be using to handle requests to the API server for data.

import pandas as pd
from sodapy import Socrata
import requests


# These are ways I have discovered to access the data better
# value = requests.get("https://data.norfolk.gov/resource/jz6u-9g3c.json")
# print(value.content)

# client = Socrata("data.norfolk.gov", None)
# results = client.get("jz6u-9g3c", limit=2000)


class request_handler:
    link_to_api = "https://data.norfolk.gov/resource/jz6u-9g3c.json"

    def __init__(self):
        print("Initialized, my friend")
