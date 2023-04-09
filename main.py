# Testing out the methods Norfolk provided through their 3rd party API host (Socrata)
# Socrata was acquired by Tyler Technologies, so hopefully that changes up a little bit.

import pandas as pd
from sodapy import Socrata
import requests

link = "https://data.norfolk.gov/resource/jz6u-9g3c.json"

# should probably make a post/get request handler for this so that I don't have to modify it too much
# but I should play around with this a lot more before doing that

value = requests.get("https://data.norfolk.gov/resource/jz6u-9g3c.json")
print(value.content)


client = Socrata("data.norfolk.gov", None)

results = client.get("jz6u-9g3c", limit=2000)

results_df = pd.DataFrame.from_records(results)

print(results_df)
