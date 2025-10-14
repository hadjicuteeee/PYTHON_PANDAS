from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["coffee_db"]
collection = db["sales"]
sample_data= [
    {"coffee_name": "Hot Chocolate", "money": 40, "cash_type": "Cash"},
    {"coffee_name": "Cocoa", "money": 60, "cash_type": "Cash"},
    {"coffee_name": "Americano w Milk", "money": 70, "cash_type": "Cash"},
    {"coffee_name": "Cortado", "money": 20, "cash_type": "Cash"},
    {"coffee_name": "Cocoa", "money": 60, "cash_type": "Cash"},
    {"coffee_name": "Capuccino", "money": 160, "cash_type": "Cash"},
]
collection.insert_many(sample_data)

print("Inserted")


pipeline = [
    {"$group": {"_id": "$coffee_name", "total_sales": {"$sum": "$money"}}},
    {"$sort": {"total_sales": -1}}
]
for result in collection.aggregate(pipeline):
    print(result)


for doc in collection.find({"cash_type": "Cash"}):
    print(doc)
