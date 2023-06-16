"""
The reason this is OK is because I don't want to store all of the data on my disk. I want to write 
a program that accesses that data and then changes/uses it.
"""

from os import link
import pandas as pd
from sodapy import Socrata
import requests
import json

class request_handler:



    def __init__(self, user):
        self.link = "https://data.norfolk.gov/resource/jz6u-9g3c.json"
        self.user = user

    def request_all_data(self):
        data = requests.get(self.link)
        return data



