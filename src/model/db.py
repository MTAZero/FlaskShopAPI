from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database =  client.ItemShopFlask
