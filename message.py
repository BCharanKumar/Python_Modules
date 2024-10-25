'''
#Just to print current time and information
import time
currenttime=time.localtime(time.time())
print(currenttime)
'''
#importing neccesary modules
import pyautogui as pa
import time

#Defining infinite loop
n=1
while True:
    #msg whatever we need to send for repeatedly
    pa.write('Hello Brother')

    #Adding  n-seconds of  delay to  the message  sending
    time.sleep(5)
    #just starting of sending msg's
    pa.press('enter')

    #Defining when we need to stop/break the message sending    
    if n==25:
        break
    

    n+=1
