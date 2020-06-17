"""
Izmir University of Economics Faculty of Engineering
Project Name: Performance Analysis Technology
Lecture: FENG 498 - Graduation Project II
Supervisor: İlker KORKMAZ
Project Group: Ömer EROĞLU - Fatih KOCA - Oğuz Timur TAŞDELEN
"""

import csv  # importing the csv module
import re  # importing regex
import random  # importing random module
from datetime import datetime
import DBmanager


def randomDataGenerator(trainingMode):
    # creating random sensorNum
    sensorNum = random.randint(1, 12)

    responseTime = 0.0
    isSuccess = 0

    if trainingMode == "Easy":
        responseTime = round(random.uniform(0.50, 4.00), 2)
        if responseTime < 3.00:
            isSuccess = 1
        else:
            isSuccess = 0
            responseTime = 3.00

    elif trainingMode == "Medium":
        responseTime = round(random.uniform(0.5, 4.0), 2)
        if responseTime < 2.00:
            isSuccess = 1
        else:
            isSuccess = 0
            responseTime = 2.00

    elif trainingMode == "Hard":
        responseTime = round(random.uniform(0.5, 4.0), 2)
        if responseTime < 1.50:
            isSuccess = 1
        else:
            isSuccess = 0
            responseTime = 1.50

    return sensorNum, responseTime, isSuccess


# This function checks the csv file if there is missing data or not.
def dataConfirmation(paramVar):  # 'paramVar' means 'parameter variable'.
    with open("training_process.csv") as file:
        csv_list = list(csv.reader(file))
        data = list(csv_list)
        count = int(len(data) / 2)  # returns float originally and make it type integer

        file.close()

        """
        print("paramVar:" + str(paramVar))
        print("count:" + str(count))
        print("")
        """

        if count == paramVar:
            print("Training has completed!")
            return True
        else:
            print("There is some missing data. Please repeat the training!")
            return False


def trainingProcess(playerID, trainingID, trainingMode, timeStamp):
    # Easy Mode
    if trainingMode == "E":
        trainingMode = "Easy"
        minTouch = 4
        maxTouch = 24

    # Medium Mode
    elif trainingMode == "M":
        trainingMode = "Medium"
        minTouch = 6
        maxTouch = 24

    # Hard Mode
    elif trainingMode == "H":
        trainingMode = "Hard"
        minTouch = 8
        maxTouch = 24

    # accuracy training constant=12 times sensors will light
    ACCURACY_CONSTANT = 12
    # name of csv file
    filename = "training_process.csv"
    # field names
    fields = ['playerID', 'trainingID', 'sensorNum', 'responseTime', 'isSuccess', 'trainingMode', 'timeStamp']
    accuracyTraining = re.compile("A-*")
    speedTraining = re.compile("S-*")

    # It means it is an accuracy training
    if re.match(accuracyTraining, trainingID):
        for i in range(ACCURACY_CONSTANT):
            # print("accuracy ", i)
            with open(filename, 'a+') as csvFile:
                # creating a csv dict writer object
                writer = csv.DictWriter(csvFile, fieldnames=fields)

                randomData = randomDataGenerator(trainingMode)
                # light sensor
                sensorLight = randomData[0]
                # getting random response time
                responseTime = randomData[1]
                # getting random result of random attempt
                isSuccess = randomData[2]

                myDict = [{'playerID': playerID, 'trainingID': trainingID, 'sensorNum': sensorLight,
                           'responseTime': responseTime, 'isSuccess': isSuccess, 'trainingMode': trainingMode,
                           'timeStamp': timeStamp}]
                writer.writerows(myDict)
                csvFile.close()

        # Counts csv file if it is missing or not.
        if dataConfirmation(ACCURACY_CONSTANT):
            # no need to check if input is valid or not because this is not an actual implementation.
            confirmation = input("Do you confirm the training? Y/N")
            if confirmation == "Y" or confirmation == "y":
                DBmanager.recorder()
                print("The training has recorded to database!")
            elif confirmation == "N" or confirmation == "n":
                print("Not confirmed, cancel the Training!")

                f = open("training_process.csv", "w")
                f.truncate()
                f.close()
                Welcome()
        else:
            # There is missing data in csv file. Clear the csv file and restart the training process!
            print("")
            f = open("training_process.csv", "w")
            f.truncate()
            f.close()
            Welcome()




    # Speed Training
    else:

        randomSpeed = random.randint(minTouch, maxTouch)  # Generates number of touches in 30 seconds.
        for i in range(randomSpeed):
            # print("speed ", i)
            with open(filename, 'a+') as csvFile:
                # creating a csv dict writer object
                writer = csv.DictWriter(csvFile, fieldnames=fields)

                randomData = randomDataGenerator(trainingMode)
                # light sensor
                sensorLight = randomData[0]
                # getting random response time
                responseTime = randomData[1]
                # getting random result of random attempt
                isSuccess = randomData[2]
                myDict = [{'playerID': playerID, 'trainingID': trainingID, 'sensorNum': sensorLight,
                           'responseTime': responseTime, 'isSuccess': isSuccess, 'trainingMode': trainingMode,
                           'timeStamp': timeStamp}]
                writer.writerows(myDict)
                csvFile.close()

        # Counts row in csv file if there is a missing data or not.
        if dataConfirmation(randomSpeed):
            # no need to check if input is valid or not because this is not an actual implementation.
            confirmation = input("Do you confirm the training? Y/N")
            if confirmation == "Y" or confirmation == "y":
                DBmanager.recorder()
                print("The training has recorded to database!")
            elif confirmation == "N" or confirmation == "n":
                print("Not confirmed, cancel the Training!")

                f = open("training_process.csv", "w")
                f.truncate()
                f.close()
                Welcome()
        else:
            # There is missing data in csv file. Clear the csv file and restart the training process!
            print("")
            f = open("training_process.csv", "w")
            f.truncate()
            f.close()
            Welcome()


# Generates trainingID according to training type with auto incrementation
def TrainingIDGenerator(type):
    lastIndex = DBmanager.getNextSequence("trainingID")
    trainingID = ""

    if type == 0:

        trainingID = ("A-{}")
        trainingID = (trainingID.format(lastIndex))
        # print(trainingID.format(lastIndex))
        return trainingID

    elif type == 1:

        trainingID = ("S-{}")
        trainingID = (trainingID.format(lastIndex))
        # print(trainingID.format(lastIndex))
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
    if not DBmanager.checkCoach(int(coachID)):
        # just terminate the program
        quit()
    playerID = input('Enter Player ID: ')  # Check if player exists!
    if not DBmanager.checkPlayer(playerID, coachID):
        # just terminate the program
        quit()


    print("\n\n\n")
    print("***SETUP THE PLATFORM***")
    print("\n0: Accuracy Measurement Training | 1: Speed Measurement Training")
    trainingType = int(input('Select Training Type (Press 0 or 1): '))

    print("'E': easy\n'M': medium\n'H': hard")
    # No need to check if input is valid or not because this is not an actual implementation
    difficultyType = input("Select Difficulty - E/M/H:")

    # Actual implementation will not be terminal application. Therefore no need to check if input is valid or not.
    trainingID = TrainingIDGenerator(trainingType)

    enterKey = input("Ready, Go!")
    # Checks if input is 'Enter' key or not.
    while enterKey != "":
        enterKey = ""
        continue

    print("\n\n\n")

    # Training process starts after pressed the Enter Key.
    trainingProcess(playerID, trainingID, difficultyType, timeStamp())
    print("\n\n\n")
    print("Process has finished!")




# process is completed for one step for now


def timeStamp():
    time = datetime.now()
    stamp = time.strftime("%d.%m.%Y, %H:%M")
    return stamp


Welcome()

