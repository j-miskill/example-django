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

    def get_link(self):
        return self.link

    def get_user(self):
        return self.user


