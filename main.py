###############################
# MAIN
###############################

import os
import ImageCapture
import PromptCreation
import ArtGeneration
import requests
from PIL import Image
import webbrowser
import multiprocessing
import time
from datetime import datetime, timedelta
from os.path import exists
from dotenv import load_dotenv

load_dotenv()  


def hourlyupdate():
  eraseOldArt()
  takePhoto()
  getCaption()
  makeArt()


def eraseOldArt():
    #First,remove any old art (note this indirectly trigger graphics to go into loading screen mode because no readable file will exist)---
    for o in range(9):
      i = o + 1
      try:
        os.rename("LocalArt" + str(i) + ".png", str(int(datetime.now().strftime("%Y%m%d%H%M")))+" LocalArt" + str(i) + ".png")
      except:
       print ("")
       print ("LocalArt" + str(i) + " did not exist, skipping it...")
def takePhoto():
    #Then, take a new photo---
    
    ImageCapture.takephoto()

def getCaption():
    #Now that we have a new photo, we need a caption from it. This makes the caption and stores it

    caption = PromptCreation.hostcreatecaption()
    file = open("CaptionStorage.txt", "w")
    file.write(caption)
    file.close() 
    print (caption)

def makeArt():
    #With this caption, this makes a photo based on it and the current channel, and saves it. Note that saving it triggers graphics to switch back because file is readable.
    file = open("CaptionStorage.txt", "r")
    caption = file.read()
    file.close() 
    image_url = ArtGeneration.generateart(PromptCreation.clientperfectcaption(caption))
    img = Image.open(requests.get(image_url, stream = True).raw)
    img = img.resize((627, 470)) #2nd number is 3/4 of the first to get scaled image. Abstract these numbers for future CRTs

    file = open("IR_RecentlyPressed.txt", "r")
    channel = file.read()
    file.close() 
    img.save('LocalArt' + channel +'.png')


#Perform the initial image upload
print ("Performing the initial non-hourly update")
hourlyupdate()

# The rest of this file sets future uploads to happen on the hour, every hour.
now = datetime.now()
nearest_hour = (now.replace(second=0, microsecond=0, minute=0, hour=now.hour) +timedelta(hours=1))
print("As we're starting the program, the time is "+ str(now) +" and the next update will occur at " + str(nearest_hour))

while True:
  diff = (nearest_hour - datetime.now()).total_seconds()
  if diff <= 0:
    print("We have reached the hour according to calculations. About to perform update.")
    hourlyupdate()
    now = datetime.now()
    nearest_hour = (now.replace(second=0, microsecond=0, minute=0, hour=now.hour) +timedelta(hours=1))
    diff = (nearest_hour - datetime.now()).total_seconds()
    time.sleep(1)
    #If we're getting close to approaching one hour since the last update, lets get as close to it as we can
     #Last 10 seconds shouldn't respond to a channel change to avoid creating art thats outdated and also shifting the system off the hour clock
  elif diff <= 0.1:
    time.sleep(0.001)
  elif diff <= 0.5:
    time.sleep(0.01)
  elif diff <= 1.5:
    time.sleep(0.1)
  elif diff <= 10:
    time.sleep(1)
  else:
    #If the system is on the wrong channel, populate an image for that channel
    file = open("IR_RecentlyPressed.txt", "r")
    channel = file.read()
    file.close() 
    art="LocalArt" + channel + ".png"
    file_exists = exists(art)
    if file_exists == False:
      makeArt()

    time.sleep(1)




