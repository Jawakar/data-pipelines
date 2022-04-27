from http import client

# Connecting to mongo
import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['truckgenie-dev']
collection = db['tripDistance']


# Connecting to PG
import psycopg2
connect_pg = psycopg2.connect(
    user="postgres", 
    password="2208711Sel", 
    host="127.0.0.1",
    port = "5432", 
    database = "truckgenie-dev"
    )
db_cursor = connect_pg.cursor()

#pulling all the documents from tripDistance collection
records = collection.find()

#inserting to PG
for row in records:
    db_cursor.execute("""INSERT INTO "tripsDistance" (_id, "tripNo", origin, destination, "totalDistance", "updatedAt", _class) VALUES (%s, %s, %s, %s, %s, %s, %s);""", (row['_id'], row['tripNo'], row['origin'], row['destination'], row['totalDistance'], row['updatedAt'], row['_class']))

db_cursor.execute("commit")
db_cursor.close()