import pandas as pd
import json

#converted json file to a dataframe 
with open("Data/2021_OCTOBER.json") as f:
 data = json.load(f)
 print(type(data))