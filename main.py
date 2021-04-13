# import the time module
import time


# define the countdown func.
def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}'.format(secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	print('Lift off!!')


# Lets prepare the flight to the Moon 
print("Lets prepare your flight")
# input payload in tons
p = input("What is the payload?")
#p = 63000
# input liquid oxygen for first stage
lo1 = input("How many gallons of liquid oxygen are you using for the first stage?")
#lo1 = 39000
# input liquid oxygen for first stage
k1 = input("How many gallons of kerosene are you using for the first stage?")
#k1 = 25000
# input liquid oxygen for second stage
lo2 = input("How many gallons of liquid oxygen are you using for the first stage?")
#lo2 = 7300
# input liquid oxygen for first stage
k2 = input("How many gallons of kerosene are you using for the first stage?")
#k2 = 4600


# input time in seconds10
t = input("Lift in t minus seconds: ")
#t = 10

# function call
countdown(int(t))

