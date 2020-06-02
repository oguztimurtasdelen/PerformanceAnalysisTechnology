import pymongo
from pymongo import MongoClient
import csv

# Connection Link
cluster = MongoClient("mongodb+srv://admin:BNRnELrcmRhGUjrN@clusterpat-luajm.mongodb.net/test?retryWrites=true&w=majority")
# Database/Cluster Name
db = cluster["test"]



def getTable(tableName):
    table = db[tableName]
    return table




def getNextSequence(sequenceName):
    try:
        sequenceDocument = getTable("testTable").find_one_and_update({}, {"$set": {"_id": sequenceName}, "$inc": {"sequence_value": 1}}, return_document=True)
        return (sequenceDocument["sequence_value"])

    except:
        print("Exception Message: Error")



# trainingTable.insert_one({"trainingID": getNextSequence("trainingID")})





with open("training_process.csv") as file:
    csv_list = list(csv.reader(file))

for row in csv_list:
    if row:
        NameSurname = row[0]
        trainingID = row[1]


    else:
        # skip blank lines
        continue






"""
query1 = {"ID": "20150601017", "Name": "Ömer", "Surname": "Eroğlu", "CoachID": "3"}
query2 = {"ID": "20150601030", "Name": "Fatih", "Surname": "Koca", "CoachID": "2"}
query3 = {"ID": "20150601045", "Name": "Oğuz Timur", "Surname": "Taşdelen", "CoachID": "4"}
collection.insert_many([query1, query2, query3])

-------------------------------------------------------------------------------------------------

query = {"ID": "1", "Name": "İlker", "Surname": "Korkmaz", "Category": "U15"}
collection.insert_one(query)

----------------------------------------------------------------------------------------------------


"""