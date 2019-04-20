#Ultra-Simple pomodoro technique based Focus App

#-------------------------------------------ITERATION 1---------------------------
#print(" focus time started ")

##focus time: sleep app for 1 minute
#import time
#time.sleep(60)

#print(" focus time ended ")

#print(" break time started ")

##break time: sleep app for 10 seconds
#time.sleep(10)

#print(" break time ended ")

#-------------------------------------------ITERATION 2---------------------------- 
#while True:
#   print(" focus time started ")
#   import time
#   time.sleep(60)
#   print(" focus time ended ")
#   print(" break time started ")
#   time.sleep(10)
#   print(" break time ended ")

#------------------------------------------ITERATION 3-----------------------------
#
##does the user want to continue?
#def userProgramContinue():
#   while True:
#       userProgramConfirmation = str(input("Do you want to continue?(Yes/No) "))
#       if(userProgramConfirmation.lower() == "yes"):
#           return True
#           break
#       elif(userProgramConfirmation.lower() == "no"):
#           return False
#           break
#       else:
#           print("invalid input. please try again.")
#
##method for alarm bell
#def alarmBell(numberOfBells):
#   import time
#   import sys
#   for i in range(1,numberOfBells):
#       sys.stdout.write('\a')
#       #to give the system some time for the alarm bell
#       time.sleep(2)
#   
##get user input
#focusTime = float(input("Enter the focus time in minutes: "))*60
#breakTime = float(input("Enter the break time in minutes: "))*60
#numberOfBells = int(input("Enter the number of bells for a notification: "))
#continueProgramOrNot = True
#
#while (continueProgramOrNot == True):
#   print(" ::Focus time started:: ")
#   import sys
#   import time 
##start focus time
#   time.sleep(focusTime)
#   print(" ::Focus time ended:: ")
#   alarmBell(numberOfBells)
#
##start break time
#   print(" ::Break time started:: ")
#   time.sleep(breakTime)
#   print(" ::Break time ended:: ")
#   alarmBell(numberOfBells)
#
#   if (userProgramContinue() == False):
#       continueProgramOrNot = False
#
#import subprocess
#subprocess.Popen([r'/mnt/c/Program Files/Notepad++/notepad++.exe'])

#-----------------------------------------------ITERATION 4------------------------------------
#
##does the user want to continue?
##def userProgramContinue():
##  while True:
##      userProgramConfirmation = str(input("Do you want to continue?(Yes/No) "))
##      if(userProgramConfirmation.lower() == "yes"):
##          return True
##          break
##      elif(userProgramConfirmation.lower() == "no"):
##          return False
##          break
##      else:
##          print("invalid input. please try again.")
#
##def userProgramContinue():
##  import time
##  autoConfirmedContinue = 10
##  doesQuestionExist = False
##  while True:
##      if(doesQuestionExist == False):
##          userProgramConfirmation = str(input("Do you want to continue?(Yes/No): "))
##          doesQuestionExist = True
##          time.sleep(1)
##          if(userProgramConfirmation.lower() == "yes"):
##              return True
##              break
##          elif(userProgramConfirmation.lower() == "no"):
##              return False
##              break
##          elif(userProgramConfirmation == ""):
##              autoConfirmedContinue -=1
##              if(autoConfirmedContinue == 1):
##                  return True
##          else:
##              print("invalid input. please try again.")
##              break
#
#def userProgramContinue():
#   import sys 
#   import select
#   while True:
#       print("Do you want to continue?(Yes/No): ")
#       in_put, out_put, error = select.select([sys.stdin],[],[],10)
#       if(in_put):
#           userProgramConfirmation = sys.stdin.readline().strip()
#           if(userProgramConfirmation.lower() == "yes"):
#               return True
#               break
#           elif(userProgramConfirmation.lower() == "no"):
#               return False
#               break
#           else:
#               print("invalid input. please try again.")
#       else:
#           print("you did not enter anything. the program continues.")
#           return True
#
##method for alarm bell
#def alarmBell(numberOfBells):
#   import time
#   import sys
#   for i in range(1,numberOfBells):
#       sys.stdout.write('\a')
#       #to give the system some time for the alarm bell
#       time.sleep(2)
#   
##get user input
#focusTime = float(input("Enter the focus time in minutes: "))*60
#breakTime = float(input("Enter the break time in minutes: "))*60
#numberOfBells = int(input("Enter the number of bells for a notification: "))
#continueProgramOrNot = True
#
#while (continueProgramOrNot == True):
#   print(" ::Focus time started:: ")
#   import sys
#   import time 
##start focus time
#   time.sleep(focusTime)
#   print(" ::Focus time ended:: ")
#   alarmBell(numberOfBells)
#
##start break time
#   print(" ::Break time started:: ")
#   time.sleep(breakTime)
#   print(" ::Break time ended:: ")
#   alarmBell(numberOfBells)
#
#   if (userProgramContinue() == False):
#       continueProgramOrNot = False
#
##import subprocess
##subprocess.Popen([r'/mnt/c/Program Files/Notepad++/notepad++.exe'])

#--------------------------------------------------------ITERATION 5---------------------------------------------------------------

