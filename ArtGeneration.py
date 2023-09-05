###############################
# ART GENERATION
###############################

import os
import openai

# Loads my API key from an environment variable (silly, I'm not giving you my key)
openai.api_key = os.getenv("OPENAI_API_KEY")


# The following is test code used to make sure DALL-E is working
def generateart(caption):
    try:
        response = openai.Image.create(
        prompt=(caption),
        #n is number of images, could change down the line
        n=1,
        #Images can have a size of 256x256, 512x512, or 1024x1024 pixels. Most CRTs wont display a difference, but go big or go home.
        size="1024x1024"
        )
        image_url = response['data'][0]['url']
    except:
        print ("Timeout on DALLE API call. Setting URL to error screen")
        #This displays that same error in a way users can see
        image_url = "https://i.ytimg.com/vi/hyWuQdrxJrA/maxresdefault.jpg" 
    return image_url
    