###############################
# PROMPT CREATION
###############################

#We're using a replicate model for this - gets a description of the image for us to use to generate art with later.
#We also do some modifying of that caption here

import replicate
import datetime
import os

def hostcreatecaption():
    modelunversioned = replicate.models.get("rmokady/clip_prefix_caption")

    version = modelunversioned.versions.get("9a34a6339872a03f45236f114321fb51fc7aa8269d38ae0ce5334969981e4cd8")

    #I can change the version to either coco or conceptual-captions. Coco is default but I've included it anyay
    #Optional input of use_beam_search as well. Leaving it undefined.
    #For more info, check https://replicate.com/rmokady/clip_prefix_caption/api
    clipcapresult = version.predict(image=open("LocalPhoto.jpg", "rb"), model="coco")
    return clipcapresult

#Here, we fine tune that input to add in descriptors based on the time of day
def clientperfectcaption(caption):
    tod = "at night"
    now = datetime.datetime.now()
    #hourstr is the local string of what hour it is
    hourstr = str(now.time())[:2]
    hour = int(hourstr)
    if hour > 18:
        tod = "at night"
    elif hour > 17:
        tod = "at sunset"
    elif hour > 15:
        tod = "in the afternoon"
    elif hour > 11:
        tod = "at midday"
    elif hour > 8:
        tod = "in the morning"
    elif hour > 7:
        tod = "at sunrise"
    else: 
        tod = "at night"

    file = open("IR_RecentlyPressed.txt", "r")
    channel = file.read()
    file.close() 
    
    # Defines my channels. Move to seperate file for users to customise
    default_prompts = {
        "1": "a very early 2000's 3d rendering in a vaporwave style of ",
        "2": "a sketch by Maurice Sendak of ",
        "3": "geometric abstract art of ",
        "4": "include 3 fish in the following: surrealistic art of ",
        "5": "incredibly detailed mandala depicting ",
        "6": "a sketch of a sculpture of ",
        "7": "in the style of Rene Magritte, a painting of ",
        "8": "a gustav klimt painting of ",
        "9": "a low-polygon model inspired by a sketch by Maurice Sendak of "
    }

    # Check if the channel has a custom prompt in the .env file
    custom_prompt_key = f"CHANNEL_{channel}_PROMPT"
    custom_prompt = os.getenv(custom_prompt_key)

    # Assign the prompt based on availability - and if its a no go, render a red X
    if custom_prompt:
        perfectedcaption = custom_prompt + caption[:-1]
    else:
        default_prompt = default_prompts.get(channel, "an X sign")
        perfectedcaption = default_prompt + caption[:-1]
        
    perfectedcaption = perfectedcaption + " in a house "+tod
    print ("perfected caption made: " + perfectedcaption)
    return perfectedcaption

