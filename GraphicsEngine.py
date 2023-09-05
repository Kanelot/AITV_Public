
###############################
# GRAPHICS
###############################

#To play with window size and image placement in the future, see https://www.tutorialspoint.com/how-to-place-an-image-into-a-frame-in-tkinter

import os
# This is an export variable originally used to make this code successfully run when sshign ing
os.environ["DISPLAY"] = ":0.0"

import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt


import tkinter as tk
from PIL import Image
from os.path import exists
import configparser
import time
config = configparser.ConfigParser()

def animation(count):
    file = open("IR_RecentlyPressed.txt", "r")
    channel = file.read()
    file.close() 
    art_to_display="LocalArt" + channel + ".png"
    
    #Not the most elegant fix here for being out of frame range... could likely restructure this area to not need it
    if count >= loadingscreenframes:
        count = 0
    switchloops = False
    global anim
    image_to_display = loading_screen_frame_array[count]

    #In the future when networked channels are implemented, here's the place to check if IR data is being sent, and if so, render it and handle its counters

    loadingscreen_label.configure(image=image_to_display)
    count += 1
    if count >= loadingscreenframes:
        count = 0
        root.attributes('-fullscreen', True)

        #Loop check to see if our program has saved an decypherable image yet
        file_exists = exists(art_to_display)
        if file_exists:
            print("Oh man! The file exists! Moving into the image loop instead")
            switchloops = True

    if switchloops:
        anim = root.after(20,lambda :animation_still(count))
    else:
        anim = root.after(20,lambda :animation(count))


def animation_still(count):
    switchloops = False
    global anim
    file = open("IR_RecentlyPressed.txt", "r")
    channel = file.read()
    file.close() 
    art_to_display="LocalArt" + channel + ".png"

    try: 
        i = tk.PhotoImage(file=art_to_display,format="png")
        loadingscreen_label.configure(image=i)
        loadingscreen_label.image = i
        loadingscreen_label.pack()
    except:
        switchloops = True

    if switchloops:
        anim = root.after(20,lambda :animation(count))
        print ("Returning to loading animation loop")
    else:
        anim = root.after(20,lambda :animation_still(count))

def stop_animation():
    root.after_cancel(anim)

# A short delay to allow other python executable files to do their thing (when this was written
# the Main function needed to erase the art if it existed or this wouldn't enter the loading screen)
time.sleep(2)

root = tk.Tk()
root.title('TV Screen')

root.attributes('-fullscreen', True)
root.configure(background='black')
global in_loading_screen
in_loading_screen = True
loadingscreen="gif1.gif"
file = open("IR_RecentlyPressed.txt", "r")
channel = file.read()
file.close() 
art_to_display="LocalArt" + channel + ".png"
loadingscreeninfo = Image.open(loadingscreen)
loadingscreenframes = loadingscreeninfo.n_frames  # gives total number of frames the static gif contains

# creating list of PhotoImage objects for each frames
loading_screen_frame_array = [tk.PhotoImage(file=loadingscreen,format=f"gif -index {i}") for i in range(loadingscreenframes)]
count = 0
anim = None

#The label is the physical representation of the image on screen
loadingscreen_label = tk.Label(root,image="")
loadingscreen_label.place(relx=.5, rely=.5, anchor="center")

#Auto-start the gif
animation(count)

root.mainloop()