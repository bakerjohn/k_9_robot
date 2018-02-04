How to make K-9
 

Introduction: 
I enjoy learning about all things IOT ,robots and raspberry pi. K-9 is a cardboard replica from the late 70's Doctor Who television show, It is also a mobile platform for Learning about the Internet of things through robotics.
 



Projects
AWS VPC - internal and external subnets
https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Scenario1.html
Raspberry Pi - 2 node cluster:
Reference: https://makezine.com/projects/build-a-compact-4-node-raspberry-pi-cluster/
SSh key based authorization between the cluster nodes
ref: https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md
Raspberry Pi to Arduino serial and I2c communications
Sonar obstacle avoidance: 
ref: http://www.instructables.com/id/Obstacle-Avoiding-Robot-With-Servo-Motor-Arduino/
Object Recognition
ref: http://www.instructables.com/id/Pan-Tilt-face-tracking-with-the-raspberry-pi/
Text to speech 
ref: http://espeak.sourceforge.net/
Voice Recognition
ref: http://stevenhickson.blogspot.com/2013/04/voice-control-on-raspberry-pi.html
Environment sensor detection and data storage
custom python scripts plus references below
ref: https://projects.raspberrypi.org/en/projects/sense-hat-data-logger
ref: https://github.com/adhorn/rasp-sensehat-iot
High charts ref: https://www.highcharts.com/
Raspberry Pi honey pot
 https://www.anomali.com/blog/create-an-army-of-raspberry-pi-honeypots-on-a-budget





Hardware 
QTY 2 Raspberry pi b3/b2
Arduino uno 1.5
L298N motor controller
HC-SR04 ultrasonic Distance Sensor
Sense hat
RGB Leds (lots of LEDS. Because they are awesome)
DC motors
12 volt Lipo battery
3 port cell phone charging battery
12 volt to 5 step down
7 inch touch screen
serial cables
Bluetooth speaker - with volume control 
usb power cables
breadboards
lots of cardboard




Software
Raspbian Jesse
Python 2.7
Webiopi http://webiopi.trouch.com/Tutorial_Basis.html
MJPG-Streamer https://xsatria.wordpress.com/2014/08/26/fast-video-streaming-usi$
Arduino shell https://www.arduino.cc/en/Main/Software
espeak  http://espeak.sourceforge.net/
openCV  https://opencv.org/
nmap https://braindrivendevelopment.com/2014/12/02/using-nmap-to-find-a-raspberry-pi-within-a-network/



Faceplants /learning moments:
bigger battery bank with at least 3 usb ports: ( Im running two raspberry pi plus a 7inch touchscreen.)

MJPG-Streamer:
        Camera issues – some usb camera’s do not work on pi

Webiopi:
To debug your script and config, you should first run WebIOPi foreground before$
sudo webiopi -d -c /etc/webiopi/config

$ cd WebIOPi-x.y.z
$ sed -i 's/ python3//' setup.sh
$ sudo ./setup.sh
$ sudo webiopi-passwd
$ sudo service webiopi restart







Best start script for mjpg-streamer - my setup
 /usr/local/bin/mjpg_streamer -i "/usr/local/lib/input_uvc.so -n -f 10 -r 1024x576" -o "/usr/local/lib/output_http.so -p 8080 -w /usr/local/www"