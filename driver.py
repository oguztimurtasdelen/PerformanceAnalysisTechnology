"""
Izmir University of Economics Faculty of Engineering
Project Name: Performance Analysis Technology
Lecture: FENG 498 - Graduation Project II
Supervisor: İlker KORKMAZ
Project Group: Ömer EROĞLU - Fatih KOCA - Oğuz Timur TAŞDELEN
"""

import csv # importing the csv module
import re #importing regex
import random #importing random module
from datetime import datetime
import DBmanager

def randomDataGenerator(trainingMode):
    #creating random sensorNum
    sensorNum=random.randint(1, 12)

    responseTime = 0.0
    isSuccess = 0


    if trainingMode == "E":
        responseTime = round(random.uniform(0.50, 4.00), 2)
        if responseTime < 3.00:
            isSuccess = 1
        else:
            isSuccess = 0
            responseTime = 3.00

    elif trainingMode == "M":
        responseTime = round(random.uniform(0.5, 4.0), 2)
        if responseTime < 2.00:
            isSuccess = 1
        else:
            isSuccess = 0
            responseTime = 2.00

    elif trainingMode == "H":
        responseTime = round(random.uniform(0.5, 4.0), 2)
        if responseTime < 1.50:
            isSuccess = 1
        else:
            isSuccess = 0
            responseTime = 1.50

    """
    #random result of attempt
    isSuccess=random.randint(0,1)
    """

    return(sensorNum, responseTime, isSuccess)


def dataConfirmation(paramVar):  # 'paramVar' means 'parameter variable'
    with open("training_process.csv") as file:
        csv_list = list(csv.reader(file))
        data = list(csv_list)
        count = len(data) / 2

        file.close()

        print("paramVar:" + str(paramVar))
        print("count:" + str(count))
        print("")

        if count == paramVar:
            print("Everything is OK!")
            return True
        else:
            print("There is some missing data. Please repeat the training!")
            return False




def trainingProcess(playerID, trainingID, trainingMode):
    difficulty = ""
    if trainingMode == "E":
        difficulty = "easy"
        minTouch = 10
        maxTouch = 60
    elif trainingMode == "M":
        difficulty = "medium"
        minTouch = 15
        maxTouch = 60
    elif trainingMode == "H":
        difficulty = "hard"
        minTouch = 20
        maxTouch = 60


    print(trainingMode)

    #accuracy training constant=30 times sensors will light
    ACCURACY_CONSTANT=30
    # name of csv file
    filename = "training_process.csv"
    # field names
    fields = ['playerID', 'trainingID', 'sensorNum', 'responseTime', 'isSuccess']
    accuracyTraining=re.compile("A-*")
    speedTraining=re.compile("S-*")

    #it means it is a accuracy training
    if(re.match(accuracyTraining, trainingID)):
        for i in range(ACCURACY_CONSTANT):
            print("accuracy ", i)
            with open(filename, 'a+') as csvfile:
                # creating a csv dict writer object
                writer = csv.DictWriter(csvfile, fieldnames=fields)


                randomData=randomDataGenerator(trainingMode)
                #light sensor
                sensorLight=randomData[0]
                #getting random response time
                responseTime = randomData[1]
                #getting random result of random attempt
                isSuccess=randomData[2]

                myDict = [{'playerID': playerID, 'trainingID': trainingID, 'sensorNum': sensorLight, 'responseTime': responseTime, 'isSuccess': isSuccess}]
                writer.writerows(myDict)
                csvfile.close()

        # Counts csv file if it is missing or not.
        if dataConfirmation(ACCURACY_CONSTANT):
            # no need to check if input is valid or not because this is not an actual implementation.
            confirmation = input("Do you confirm the training? Y/N")
            if confirmation == "Y" or confirmation == "y":
                print("Confirmed, send to Database here!")
            elif confirmation == "N" or confirmation == "n":
                print("Not confirmed, cancel the Training!")

                f = open("training_process.csv.csv", "w")
                f.truncate()
                f.close()
                Welcome()
        else:
            # There is missing data in csv file. Clear the csv file and restart the training process!
            print("")
            f = open("training_process.csv.csv", "w")
            f.truncate()
            f.close()
            Welcome()




    #Speed Training
    else:

        randomSpeed = random.randint(minTouch, maxTouch)  # Generates number of touches in 30 seconds.
        for i in range(randomSpeed):
            print("speed ", i)
            with open(filename, 'a+') as csvfile:
                # creating a csv dict writer object
                writer = csv.DictWriter(csvfile, fieldnames=fields)


                randomData = randomDataGenerator(trainingMode)
                # light sensor
                sensorLight = randomData[0]
                # getting random response time
                responseTime = randomData[1]
                # getting random result of random attempt
                isSuccess = randomData[2]
                myDict = [
                    {'playerID': playerID, 'trainingID': trainingID, 'sensorNum': sensorLight, 'responseTime': responseTime, 'isSuccess': isSuccess}]
                writer.writerows(myDict)
                csvfile.close()

        # Counts csv file if it is missing or not.
        dataConfirmation(randomSpeed)





# creating random trainingID
def randomTrainingID(type):


    lastIndex = DBmanager.getNextSequence("trainingID")
    trainingID = ""



    if type == 0:

        trainingID = ("A-{}")
        trainingID = (trainingID.format(lastIndex))
        print(trainingID.format(lastIndex))
        return trainingID

    elif type == 1:

        trainingID = ("S-{}")
        trainingID = (trainingID.format(lastIndex))
        print(trainingID.format(lastIndex))
        return trainingID










def Welcome():
    f = open("training_process.csv", "w")
    f.truncate()
    f.close()

    # Section: 'Welcome'
    print("\n ***WELCOME TO PERFORMANCE ANALYSIS TECHNOLOGY SYSTEM*** \n")
    print("Performance Analysis Technology is used to measure performance of players in wide range sports branch and "
          "to serve this measurements to coaches.")

    enterKey = input("Press Enter to Start!")
    # Checks if input is 'Enter' key or not.
    while enterKey != "":
        enterKey = ""
        continue

    print("\n\n\n")
    print("***SETUP THE PLATFORM***")

    # Section: 'Prepare the Platform'
    coachID = input('Enter Coach ID: ')  # Check if coach exists!
    playerID = input('Enter Player ID: ')  # Check if player exists!

    print("\n\n\n")
    print("***SETUP THE PLATFORM***")
    print("\n0: Accuracy Measurement Training | 1: Speed Measurement Training")
    trainingType = int(input('Select Training Type (Press 0 or 1): '))

    print("'E': easy\n'M': medium\n'H': hard")
    # No need to check if input is valid or not because this is not an actual implementation
    difficultyType = input("Select Difficulty - E/M/H:")

    # Actual implementation will not be terminal application. Therefore no need to check if input is valid or not.
    trainingID = randomTrainingID(trainingType)

    enterKey = input("Ready, Go!")
    # Checks if input is 'Enter' key or not.
    while enterKey != "":
        enterKey = ""
        continue

    print("\n\n\n")

    # Training process starts after pressed the Enter Key.
    trainingProcess(playerID, trainingID, difficultyType)
    print("\n\n\n")
    print("Process has finished!")

#process is completed for one step for now




def timeStamp():
    time = datetime.now()
    stamp = time.strftime("%d.%m.%Y, %H:%M")

    print(stamp)



timeStamp()
Welcome()






"""
*****NOTEBOOK*****
Please add your warnings/suggestions/complaints about the program to this field as a comment and 
mark 'Cancel/In Progress/Done' if any of comments fit.


1. Create a new 'cache.csv' file to hold copy of data. And provide database operations through 'cache.csv' file. (In Progress)
2. For 'RandomDataGenerator' function, write the percentage of success/unsuccess probability to final report. 
For example, in easy mode, success rate is 3/3.5 means responseTime/(maxResponseTime-minResponseTime) (In Progress)
"""