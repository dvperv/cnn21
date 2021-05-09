import pandas as pd
from pymongo import MongoClient

db_params = {
    'd': [
        'mongodb+srv://arthur:xaH3Uq3rO9JhUBUQ@cluster0.vx1qm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',
        'astral',
        'metas'],
    'r': [
        'mongodb+srv://reader:xd8bHliKHNxJJK1g@cluster0.vujwe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',
        'test',
        'itog']
}

uri, database, collection = db_params['r']

client = MongoClient(uri)
db = client[database]
collection = db[collection]
df = pd.DataFrame(iter(collection.find()))
print(df)
