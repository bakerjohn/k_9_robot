# import software and services
import os
import webiopi

import time


# import Serial driver for connecting to the arduino over serial
from webiopi.devices.serial import Serial

# initialize Serial driver
ser = Serial("ttyACM0", 9600)

# Enable debug output

webiopi.setDebug()

# referencing library

GPIO = webiopi.GPIO


# set the gpio pin reference

L1 = 17

L2 = 27

R1 = 22

R2 = 23



#imports import webiopi


# Libreria GPIO 
GPIO = webiopi . GPIO

# ------------------------------------------------- - # # Definitions constant # # ------------------------------------------- ------- #



# GPIOs left motor 
L1 = 17 # H-Bridge 1 
L2 = 27 # H-Bridge 2   

# GPIOs right motor 
R1 = 10 # H-Bridge 3 
R2 = 9 # H-Bridge 4  

# ------------------------------------------------- - # # Left motor functions # # ------------------------------------------ -------- #



def left_stop (): 
    GPIO . output ( L1 , GPIO . LOW ) 
    GPIO . output ( L2 , GPIO . LOW )
    

def left_forward (): 
    GPIO . output ( L1 , GPIO . HIGH ) 
    GPIO . output ( L2 , GPIO . LOW )
    
def left_backward (): 
    GPIO . output ( L1 , GPIO . LOW ) 
    GPIO . output ( L2 , GPIO . HIGH )

# ------------------------------------------------- - # # Motor functions right # # ------------------------------------------ -------- #



def right_stop (): 
    GPIO . output ( R1 , GPIO . LOW ) 
    GPIO . output ( R2 , GPIO . LOW )

def right_forward (): 
    GPIO . output ( R1 , GPIO . HIGH ) 
    GPIO . output ( R2 , GPIO . LOW )

def right_backward (): 
    GPIO . output ( R1 , GPIO . LOW ) 
    GPIO . output ( R2 , GPIO . HIGH )

# ------------------------------------------------- - # # Definition macro # # ------------------------------------------- ------- #



@webiopi . macro
 def go_forward (): 
    left_forward ()

@webiopi . macro
 def go_backward (): 
    left_backward ()

@webiopi . macro
 def turn_left (): 
    right_forward ()

@webiopi . macro
 def turn_right (): 
    right_backward ()

@webiopi . macro    
 def stop (): 
    left_stop () 
    right_stop ()
    
# ------------------------------------------------- - # # Iniciacializacion # # -------------------------------------------- ------ #



def setup (): # GPIOs 
    GPIO installation . setFunction ( L1 , GPIO . OUT ) 
    GPIO . setFunction ( L2 , GPIO . OUT )


    GPIO . setFunction ( R1 , GPIO . OUT ) 
    GPIO . setFunction ( R2 , GPIO . OUT )


def destroy (): # Reset the GPIO 
    GPIO functions . setFunction ( L1 , GPIO . IN ) 
    GPIO . setFunction ( L2 , GPIO . IN )
    

    GPIO . setFunction ( R1 , GPIO . IN ) 
    GPIO . setFunction ( R2 , GPIO . IN )
    

@webiopi.macro
def btn1():
    os.system("espeak 'Turning on the lights'")

    print("Sending Signal to Arduino")
    ser.writeString("1")
    webiopi.sleep(2)

@webiopi.macro
def btn2():
    print("Sending Signal to Arduino")
    ser.writeString("2")
    webiopi.sleep(2)
@webiopi.macro

def btn3():
    os.system("espeak 'Scanning the area'")
    print("Sending Signal to Arduino")
    ser.writeString("3")
    webiopi.sleep(2)

@webiopi.macro
def btn4():
    print("Sending Signal to Arduino")
    ser.writeString("4")
    webiopi.sleep(2)

@webiopi.macro
def btn5():
    print("Sending Signal to Arduino")
    ser.writeString("5")
    webiopi.sleep(2)
@webiopi.macro
def btn6():
    print("Sending Signal to Arduino")
    ser.writeString("6")

    webiopi.sleep(2)


