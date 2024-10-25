
#Taking of the screenshot without any delay

#Here Importing the nessesary module
import pyscreenshot as ps
#Capturing of the entire screen
img=ps.grab()
#It will show after taking screen shot to user/developer
img.show()
#saving of the image at which location you want to save
img.save('C:\\Users\\kumar\\Desktop\\vasavi\\example.jpg')

'''

#Here Importing the nessesary modules
from PIL import ImageGrab
import time

# Define the screenshot function
def take_screenshot():
    # Just Print a message to indicate screenshot capture
    print("Capturing screenshot...")
    # Adding  n-seconds of  delay to ensure the screenshot captures the desired content
    time.sleep(3)
     # By using grab()/(ImageGrab.grab()) we can capture the entire screen
    img=ImageGrab.grab()
    #It will show after taking screen shot to user/developer    
    img.show()
    #saving of the screenshot at which location you want to save
    img.save('example1.png')
    #Finally giving a message to confirm screenshot save
    print("Screenshot saved as 'example1.png'")

#calling of the function
take_screenshot()
    


'''
