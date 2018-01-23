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

motor1A = 17

motor1B = 27

motor2A = 22

motor2B = 23


# setup function is automatically called at WebIOPi startup
def setup():
   print("Script is now setup")
   webiopi.debug("Script with macros - Setup")

   # Setting GPIOs to output

   GPIO.setFunction(motor1A, GPIO.OUT)

   GPIO.setFunction(motor1B, GPIO.OUT)

   GPIO.setFunction(motor2A, GPIO.OUT)
   GPIO.setFunction(motor2B, GPIO.OUT)



   #Setting GPIOs to off state

   GPIO.digitalWrite(motor1A, GPIO.LOW)

   GPIO.digitalWrite(motor1B, GPIO.LOW)

   GPIO.digitalWrite(motor2A, GPIO.LOW)

   GPIO.digitalWrite(motor2B, GPIO.LOW)


# loop function is repeatedly called by WebIOPi
def loop():
        print("Script is executed")
        webiopi.sleep(1)


# destroy function is called at WebIOPi shutdown
def destroy():
    print("Script is now closed")
    ser.close()    # close the serial port
    webiopi.debug("Script with macros - Destroy")

    GPIO.setFunction(motor1A, GPIO.IN)

    GPIO.setFunction(motor1B, GPIO.IN)

    GPIO.setFunction(motor2A, GPIO.IN)

    GPIO.setFunction(motor2B, GPIO.IN)


@webiopi.macro
def MoveForward():

#   os.system("espeak 'Moving Forward'")

   GPIO.digitalWrite(motor1A, GPIO.HIGH)

   GPIO.digitalWrite(motor1B, GPIO.LOW)

   GPIO.digitalWrite(motor2A, GPIO.HIGH)

   GPIO.digitalWrite(motor2B, GPIO.LOW)


@webiopi.macro

def MoveBackward():

   GPIO.digitalWrite(motor1A, GPIO.LOW)

   GPIO.digitalWrite(motor1B, GPIO.HIGH)

   GPIO.digitalWrite(motor2A, GPIO.LOW)

   GPIO.digitalWrite(motor2B, GPIO.HIGH)
@webiopi.macro

def Stop():

   GPIO.digitalWrite(motor1A, GPIO.LOW)

   GPIO.digitalWrite(motor1B, GPIO.LOW)

   GPIO.digitalWrite(motor2A, GPIO.LOW)

   GPIO.digitalWrite(motor2B, GPIO.LOW)

@webiopi.macro

def MoveLeft():

   GPIO.digitalWrite(motor1A, GPIO.HIGH)

   GPIO.digitalWrite(motor1B, GPIO.LOW)

   GPIO.digitalWrite(motor2A, GPIO.LOW)

   GPIO.digitalWrite(motor2B, GPIO.HIGH)

@webiopi.macro

def MoveRight():

   GPIO.digitalWrite(motor1A, GPIO.LOW)

   GPIO.digitalWrite(motor1B, GPIO.HIGH)

   GPIO.digitalWrite(motor2A, GPIO.HIGH)

   GPIO.digitalWrite(motor2B, GPIO.LOW)


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


