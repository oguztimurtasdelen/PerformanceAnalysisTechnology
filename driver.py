"""
Izmir University of Economics Faculty of Engineering
Project Name: Performance Analysis Technology
Lecture: FENG 498 - Graduation Project II
Supervisor: İlker KORKMAZ
Project Group: Ömer EROĞLU - Fatih KOCA - Oğuz Timur TAŞDELEN

"""

# Section: 'Welcome'
print("\n***WELCOME TO PERFORMANCE ANALYSIS TECHNOLOGY SYSTEM*** \n")
print("Performance Analysis Technology is used to measure performance of players in wide range sports branch and "
      "to serve this measurements to coaches.")

enterKey = input("Press Enter to Start!")
# Checks if input is 'Enter' key or not.
while enterKey != "":
    continue

print("\n\n\n")

# Section: 'Prepare the Platform'
coachID = input('Enter Coach ID: ')  # Check if coach exists!
playerID = input('Enter Player ID: ')  # Check if player exists!

print("\n0: Accuracy Measurement Training | 1: Speed Measurement Training")
trainingType = int(input('Select Training Type (Press 0 or 1): '))
# Actual implementation will not be terminal application. Therefore no need to check if input is valid or not.


enterKey = input("\n\n\nTraining Platform is Ready! Press Enter to Start!")
# Checks if input is 'Enter' key or not.
while enterKey != "":
    continue

print("\n\n\n")


# Section: 'Define Training Methods'
def accuracyTraining():
    """
    Accuracy Training Method will be implemented here!

    """
    print("Accuracy Training Section")


def speedTraining():
    """
    Speed Training Method will be implemented here!

    """
    print("Speed Training Section")


if trainingType == 0:
    accuracyTraining()

elif trainingType == 1:
    speedTraining()
