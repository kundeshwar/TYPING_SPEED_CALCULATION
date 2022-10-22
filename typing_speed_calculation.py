from distutils.log import error
from time import *
import random as r

def mistakes(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error += 1
        except:
            error += 1
def timespeed(time_s,time_e,userinput):
    time_d = time_e - time_s
    time_r = round(time_d,2)
    speed = len(userinput)/time_r
    return round(speed)

test = ["A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond","kundeshwar is the dog he have a no control"]
test1 = r.choice(test)
print("***********typing speed**********")
print(test1)
print()
print()
time_1 = time()
testinput = input("please Enter :-")
time_2 = time()
print("SPEED : ", timespeed(time_1,time_2,testinput),"word/sec")
print("error : ", mistakes(test1,testinput))
