from defines import *
from timer import *


  
rules()                     #1st from start

timer_smol(3)               #Pause from timer

start()                     #2nd from start


qstn_trigger = False                   
while qstn_trigger == False:
    answr = input("> ")
    if answr == "cut the ropes":
        print ("\n ")
        rusty_nail()
        
    elif answr == "try to reach":
        print ("\n ")
        torturing_tool()
        qstn_trigger = True
    elif answr == "screaming":
        print ("\n ")
        scream()
        
    else:
        print ("Seems like you are wasting you precious time, try again.")
        

dr_wndw = False
while dr_wndw == False:
    answr = input("> ")
    if answr == "open a door":
        print ("\n ")
        door_0()
        
    elif answr == "escape through window":
        print ("\n ")
        balcony()
        dr_wndw = True
    elif answr == "screaming":
        print ("\n ")
        scream1()
        
    else:
        print ("Time is short, choose wisely.")
        

wat = False                     
while wat == False:
    answr = input("> ")
    if answr == "check":
        print ("\n ")
        check()
        
    elif answr == "wait":
        awaiting(3)
        print ("\n ")
        wait()
        wat = True
    elif answr == "screaming":    # Zakladka:P
        print ("\n ")
        scream2()
        
    else:
        print ("Concentrate.")

choose()
chs_trg = False #Choose() trigger
fdr_cls = False #First door CLOSE trigger
sdr_cls = False #Second door CLOSE trigger
tdr_cls = False #Third door CLOSE trigger
while chs_trg == False:
    answr = input("> ")
    if answr == "1st door" and fdr_cls == False:
        print ("\n ")
        dr1()
        fdr_cls = True
    elif answr == "2nd door" and sdr_cls == False:
        print ("\n ")
        dr2()
        dr2_2()
        chs_trg = False
        sdr_cls = True
    elif answr == "3rd door":
        tdr_cls = True 
        print ("\n ")
        dr3_1()
        
        
        tdr_trg = False #Third door trigger
        while tdr_trg == False:
            answr = input("> ")
            if answr == "unlock":
                nr_ver()
                tdr_trg = True
            elif answr =="back":
                back_8()
                tdr_trg = True
            else:
                print ("What? ")
                
                tdr_trg = False
    
    elif answr == "1st door":
        print ("You have been there already, try another door.")
    
    elif answr == "2nd door":
        print ("You have been there already, but can try: ")   
        if fdr_cls == False and tdr_cls == False:
            print ("- [1st door] made of wood and you feel bad smell behind it.")
            print ("- [3rd door] covered in metal, has some kind of code locking.")
        else:
            print ("- [3rd door] covered in metal, has some kind of code locking.")
    else:
        print ("Doors..Doors..Do the choice!")
        

        
