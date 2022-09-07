import json
from pymongo import MongoClient
import glob


myclient = MongoClient("mongodb://localhost:27017/")

db = myclient["GFG"]


Collection = db["data"]


filelist = glob.glob('jsonFile/*.json')

for filename in filelist:
    with open(filename) as file:
        file_data = json.load(file)

if isinstance(file_data,list):
    Collection.insert_many(file_data)
else:
    Collection.insert_one(file_data)