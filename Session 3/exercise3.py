from pymongo import MongoClient
from bson.objectid import ObjectId
from collections import Counter
import matplotlib.pyplot as plt


uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
c4e = client.c4e
customers = c4e["customers"]

cust_ref = customers.find()

for i in cust_ref:
    ref = Counter(i['ref'] for i in cust_ref if i.get('ref'))
    # print(ref)

labels = list(ref.keys())
sizes = list(ref.values())

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.show()