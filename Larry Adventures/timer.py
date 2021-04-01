import sys
import time
##########This one is unused cuz im too dumb to run 2x proccesses at the time:(
# def countdown(t):
    # while t >= 0:
        
        # sys.stdout.write ("\rYou have: %s seconds left" % t)
        # sys.stdout.flush
        # time.sleep(1)
        # t -= 1
       
    # print(', your time is up!')
    
#Pause enabler
def timer_smol(t):
    while t >= 0:

        time.sleep(1)
        t -= 1
#PArt where you are being patient
def awaiting(t):
    while t >= 0:
        
        sys.stdout.write ("\rWaiting..%s \t" % t)
        sys.stdout.flush
        time.sleep(1)
        t -= 1
        
def awaiting_2(t):
    while t >= 0:
        
        sys.stdout.write ("\rGame will close in..%s \t" % t)
        sys.stdout.flush
        time.sleep(1)
        t -= 1