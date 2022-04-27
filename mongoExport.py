import pymongo
import pandas
import datetime
import os

#Connecting to mongo server
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['truckgenie-dev']
collection = db['tripDistance']

#API call to get all documents
mongo_docs = collection.find()

#Exports as csv with timestamp to a directory
def mongo_export_to_csv(mongo_docs, filename):
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%d.%m.%Y %H-%M-%S")
    docs = pandas.DataFrame(mongo_docs)
    path = os.getcwd()
    out_dir = os.path.join(path,'mongoOut', filename+' '+current_date+'.csv')
    docs.to_csv(out_dir,",", index=False)

mongo_export_to_csv(mongo_docs, "tripDistance")