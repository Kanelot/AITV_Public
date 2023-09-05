###############################
# IMAGE CAPUTURE
###############################

import cv2 as cv

#Note for future self: perhaps image quality can improve with an API argument from this list: https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gga023786be1ee68a9105bf2e48c700294dab6ac3effa04f41ed5470375c85a23504

#This function takes an image and saves image to the drive
def takephoto():
    cam = cv.VideoCapture(0)   
    s, img = cam.read()
    if s:
        cv.imwrite("LocalPhoto.jpg",img)
    
    # If captured image is corrupted, moving to else part
    else:
        print("Error: No image detected from webcam. Using the previously stored webcam image.")
        