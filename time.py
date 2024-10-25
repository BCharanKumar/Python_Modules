'''
#Just to print current time and information
import time
currenttime=time.localtime(time.time())
print(currenttime)
'''
import pyautogui as pa
import time

n=1
while True:
    pa.write('Hello Brother')
    time.sleep(5)
    pa.press('enter')
    
    if n==25:
        break
    

    n+=1
