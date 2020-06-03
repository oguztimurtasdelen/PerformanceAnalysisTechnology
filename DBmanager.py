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



# for auto_increment
def getNextSequence(sequenceName):
    try:
        sequenceDocument = getTable("testTable").find_one_and_update({}, {"$set": {"_id": sequenceName}, "$inc": {"sequence_value": 1}}, return_document=True)
        return (sequenceDocument["sequence_value"])

    except:
        print("Exception Message: Error")






# Records all data to database
def recorder():

    with open("training_process.csv") as file:
        csv_list = list(csv.reader(file))


    flag = True

    for row in csv_list:
        if row:
            playerID = row[0]
            trainingID = row[1]
            sensorNo = row[2]
            responseTime = row[3]
            isSucces = row[4]
            trainingMode = row[5]
            timeStamp = row[6]

            queryTraining = {"trainingID": trainingID, "sensorNo": sensorNo, "responseTime": responseTime, "isSucces": isSucces}
            getTable("trainingsTable").insert_one(queryTraining)

            # runs once for recording 'historyTable'
            if flag:
                # Records once for 'historyTable'
                queryHistory = {"playerID": playerID, "trainingID": trainingID, "trainingMode": trainingMode, "timeStamp": timeStamp}
                getTable("historyTable").insert_one(queryHistory)
                flag = False

        else:
            # skip blank lines
            continue




# check if coach is exist or not
def checkCoach(coachID):

    return bool(getTable("coachTable").find_one({"ID": coachID}))



def checkPlayer(playerID, coachID):

    if bool(getTable("playerTable").find_one({"ID": playerID})):
        # means player exists
        playerInfo = getTable("playerTable").find_one({"ID": playerID})
        c_ID = playerInfo["CoachID"]

        if c_ID == coachID:
            # means the player belongs this coach
            return True
        else:
            # means the coach calls another player that he/she does not train
            print("You do not have permissions to train this player!")
            return False
    else:
        print("There is no player for this ID!")
        return False



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