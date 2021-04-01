from sys import exit
from timer import *
scen_txt_1 = r'Not_code\Scenario\1_start.txt'
scen_txt_2 = r'Not_code\Scenario\0_rules.txt'
scen_txt_3 = r'Not_code\Scenario\3_cut_rope_nail.txt'
scen_txt_4 = r'Not_code\Scenario\4_choosing_window_or_door.txt'
scen_txt_5 = r'Not_code\Scenario\3_scream.txt'
scen_txt_6 = r'Not_code\Scenario\4_door.txt'
scen_txt_7 = r'Not_code\Scenario\5_check_or_wait.txt'
scen_txt_8 = r'Not_code\Scenario\5_scream.txt'
scen_txt_9 = r'Not_code\Scenario\6_peel.txt'
scen_txt_10 = r'Not_code\Scenario\7_wait.txt'
scen_txt_11 = r'Not_code\Scenario\8_choose_one_of_3_doors.txt'
scen_txt_12 = r'Not_code\Scenario\8_door_1.txt'
scen_txt_13 = r'Not_code\Scenario\8_door_2.txt'
scen_txt_14 = r'Not_code\Scenario\8_door_2_1.txt'
scen_txt_15 = r'Not_code\Scenario\8_door_2_2.txt'
scen_txt_16 = r'Not_code\Scenario\8_door_3_1.txt'
scen_txt_17 = r'Not_code\Scenario\8_door_3_2.txt'
scen_txt_18 = r'Not_code\Scenario\8_back.txt'
scen_txt_19 = r'Not_code\Scenario\9_portal.txt'
scen_txt_20 = r'Not_code\Scenario\9_1_portal.txt'
###################################################################################


def start():
    
    with open(scen_txt_1) as f:
        txt = f.read()
        print (txt)


def rules():
    
    with open(scen_txt_2) as f:
        txt = f.read()
        print (txt + "\n ") 


def rusty_nail():
    
    with open(scen_txt_3) as f:
        txt = f.read()
        print (txt + "\n ")  


def torturing_tool():
    
    with open(scen_txt_4) as f:
        txt = f.read()
        print (txt + "\n ")
        
def scream2():
    
    with open(scen_txt_8) as f:
        txt = f.read()
        print (txt + "\n ")  
        exit(0)


def scream():
    
    with open(scen_txt_5) as f:
        txt = f.read()
        print (txt + "\n ")  
        print ("Would you like to try again? Y/N ?")
        answr = input("> ")
        if answr == "y" or answr == "Y":
            start()
            qstn_trigger = False
        elif answr == "n" or answr == "N":
            exit(0)
        else:
            print ("You are a typo type...Bye.")
            exit(0)
            
def scream1():
    
    with open(scen_txt_5) as f:
        txt = f.read()
        print (txt + "\n ")  
        print ("Would you like to try again? Y/N ?")
        answr = input("> ")
        if answr == "y" or answr == "Y":
            start()
            dr_wndw = False
        elif answr == "n" or answr == "N":
            exit(0)
        else:
            print ("You are a typo type...Bye.")
            exit(0)

def door_0():
    
    with open(scen_txt_6) as f:
        txt = f.read()
        print (txt + "\n ")  
        print ("Would you like to try again? Y/N ?")
        answr = input("> ")
        if answr == "y" or answr == "Y":
            torturing_tool()
            dr_wndw = False
        elif answr == "n" or answr == "N":
            exit(0)
        else:
            print ("You are a typo type...Bye.")
            exit(0)
            
def balcony():

    with open (scen_txt_7) as f:
        txt = f.read()
        print (txt + "\n ")
        
def check():
    
    with open(scen_txt_9) as f:
        txt = f.read()
        print (txt + "\n ")  
        print ("Would you like to try again? Y/N ?")
        answr = input("> ")
        if answr == "y" or answr == "Y":
            balcony()
            wat = False
        elif answr == "n" or answr == "N":
            exit(0)
        else:
            print ("You are a typo type...But..")
            timer_smol(2)
            check()
            
def wait():

    with open (scen_txt_10) as f:
        txt = f.read()
        print (txt + "\n ")
        
def choose():

    with open (scen_txt_11) as f:
        txt = f.read()
        print (txt + "\n ")
        
def dr1():

    with open (scen_txt_12) as f:
        txt = f.read()
        print (txt + "\n ")
        
def dr2():

    with open (scen_txt_13) as f:
        txt = f.read()
        print (txt + "\n ")
        
def dr2_1():

    with open (scen_txt_14) as f:
        txt = f.read()
        print (txt + "\n ")
        
def dr2_2():

    with open (scen_txt_15) as f:
        txt = f.read()
        print (txt + "\n ")
        
def dr3_1():

    with open (scen_txt_16) as f:
        txt = f.read()
        print (txt + "\n ")
        
def dr3_2():

    with open (scen_txt_17) as f:
        txt = f.read()
        print (txt + "\n ")
        
def back_8():

    with open (scen_txt_18) as f:
        txt = f.read()
        print (txt + "\n ")

def portal():
    
    with open (scen_txt_19) as f:
        txt = f.read()
        print (txt + "\n ")
        
def portal_end():
    
    with open (scen_txt_20) as f:
        txt = f.read()
        print (txt + "\n ")
        
def nr_ver():

    anynr = input("Type CODE here: ")# here should be typed a number+ but if it is not so+ I should check it.
    print ("\tYou carefully pick up numbers")
    if anynr == "5341":
        portal()
        timer_smol(2)
        portal_end()
        awaiting_2(29)
        exit(0)   
        
    else: 
        print ("The CODE didn't fit+ door remains closed.")
        print ("[Try] again or go choose another [door]?")
        bck = input("> ")
        what = False
        while what == False:
        
            if bck == "try":
                what = True
                nr_ver()
            elif bck != "try" and bck != "door":
                print ("What?")
                what = False
                nr_ver()
            else:
                bck == "door"
                what = True
                back_8()
