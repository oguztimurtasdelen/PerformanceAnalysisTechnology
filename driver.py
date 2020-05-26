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



def randomDataGenerator():
    #creating random sensorNum
    sensorNum=random.randint(1, 8)
    #random result of attempt
    isSuccess=random.randint(0,1)

    return(sensorNum, isSuccess)



def trainingProcess(playerID, trainingID):
    #accuracy training constant=30 times sensors will light
    ACCURACY_CONSTANT=30
    # name of csv file
    filename = "training_process.csv"
    # field names
    fields = ['playerID', 'trainingID', 'sensorNum', 'isSuccess']
    accuracyTraining=re.compile("111*")
    speedTraining=re.compile("000*")

    #it means it is a accuracy training
    if(re.match(accuracyTraining, trainingID)):
        for i in range(ACCURACY_CONSTANT):
            print("accuracy ", i)
            with open(filename, 'a+') as csvfile:
                # creating a csv dict writer object
                writer = csv.DictWriter(csvfile, fieldnames=fields)


                randomData=randomDataGenerator()
                #light sensor
                sensorLight=randomData[0]
                #getting random result of random attempt
                isSuccess=randomData[1]
                mydict = [{'playerID': playerID, 'trainingID': trainingID, 'sensorNum': sensorLight, 'isSuccess': isSuccess}]
                writer.writerows(mydict)
                csvfile.close()
    #speed training
    else:
        randomSpeed=random.randint(30,45) #Generates number of touches in 30 seconds.
        for i in range(randomSpeed):
            print("speed ", i)
            with open(filename, 'a+') as csvfile:
                # creating a csv dict writer object
                writer = csv.DictWriter(csvfile, fieldnames=fields)


                randomData = randomDataGenerator()
                # light sensor
                sensorLight = randomData[0]
                # getting random result of random attempt
                isSuccess = randomData[1]
                mydict = [
                    {'playerID': playerID, 'trainingID': trainingID, 'sensorNum': sensorLight, 'isSuccess': isSuccess}]
                writer.writerows(mydict)
                csvfile.close()


#creating random trainingID
def randomTrainingID(type):
    if type == 0:
        # We need database connection to create actual trainingID. This is just simulation
        return '1119'

    elif trainingType == 1:
        # We need database connection to create actuala trainingID. This is just simulation
        return '00011'


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

print("\n0: Accuracy Measurement Training | 1: Speed Measurement Training")
trainingType = int(input('Select Training Type (Press 0 or 1): '))
# Actual implementation will not be terminal application. Therefore no need to check if input is valid or not.
trainingID = randomTrainingID(trainingType)


enterKey = input("Press Enter to Start!")
# Checks if input is 'Enter' key or not.
while enterKey != "":
    enterKey = ""
    continue


print("\n\n\n")

# Training process starts after pressed the Enter Key.
trainingProcess(playerID, trainingID)
print("\n\n\n")
print("Process has finished!")


#process is completed for one step for now