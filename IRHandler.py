###############################
# IR HANDLER
###############################

#For remotes. Right now, only used for internal channels, not switching between units. 

import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep
import os

# Static program vars
pin = 11  # Input pin of sensor (GPIO.BOARD)

# Read the values from environment variables
button_1 = int(os.getenv("BUTTON_1"))
button_2 = int(os.getenv("BUTTON_2"))
button_3 = int(os.getenv("BUTTON_3"))
button_4 = int(os.getenv("BUTTON_4"))
button_5 = int(os.getenv("BUTTON_5"))
button_6 = int(os.getenv("BUTTON_6"))
button_7 = int(os.getenv("BUTTON_7"))
button_8 = int(os.getenv("BUTTON_8"))
button_9 = int(os.getenv("BUTTON_9"))

# Create the Buttons array using the values
ButtonsNames = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]

# Sets up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN)

# Gets binary value from what we read
def getBinary():
	# Internal vars
	num1s = 0  # Number of consecutive 1s read
	binary = 1  # The binary value
	command = []  # The list to store pulse times in
	previousValue = 0  # The last value
	value = GPIO.input(pin)  # The current value

	# Waits for the sensor to pull pin low
	while value:
		sleep(0.0001) # This sleep decreases CPU utilization immensely
		value = GPIO.input(pin)
		
	# Records start time
	startTime = datetime.now()
	
	while True:
		# If change detected in value
		if previousValue != value:
			now = datetime.now()
			pulseTime = now - startTime #Calculate the time of pulse
			startTime = now #Resets start time
			command.append((previousValue, pulseTime.microseconds)) #Stores recorded data
			
		# Updates consecutive 1s variable
		if value:
			num1s += 1
		else:
			num1s = 0
		
		# Breaks program when the amount of 1s surpasses 10000
		if num1s > 10000:
			break
			
		# Re-reads pin
		previousValue = value
		value = GPIO.input(pin)
		
	# Converts times to binary
	for (typ, tme) in command:
		if typ == 1: #If looking at rest period
			if tme > 1000: #If pulse greater than 1000us
				binary = binary *10 +1 #Must be 1
			else:
				binary *= 10 #Must be 0
			
	if len(str(binary)) > 34: #Sometimes, there are some stray characters
		binary = int(str(binary)[:34])
		
	return binary
	
# Converts that value to hex
def convertHex(binaryValue):
	tmpB2 = int(str(binaryValue),2) #Temporarely propper base 2
	return hex(tmpB2)
	
while True:
	inData = convertHex(getBinary()) #Runs subs to get incoming hex value
	for button in range(len(Buttons)):#Runs through every value in list
		if hex(Buttons[button]) == inData: #Checks this against incoming
			file = open("IR_RecentlyPressed.txt", "w")
			file.write(ButtonsNames[button])
			print("File written to - Pressed was "+ ButtonsNames[button])
			file.close() 