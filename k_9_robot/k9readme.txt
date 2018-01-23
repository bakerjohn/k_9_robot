How to make K-9





Hardware :
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
usb power cables
breadboards
lots of cardboard




The Software:
Raspbian Jesse

Python 2.7

Webiopi http://webiopi.trouch.com/Tutorial_Basis.html

MJPG-Streamer https://xsatria.wordpress.com/2014/08/26/fast-video-streaming-usi$

Arduino shell https://www.arduino.cc/en/Main/Software




Faceplants:

MJPG-Streamer
        Camera issues – some usb camera’s do not work on pi
Webiopi errors on B2
https://github.com/doublebind/raspi

To debug your script and config, you should first run WebIOPi foreground before$
sudo webiopi -d -c /etc/webiopi/config

Open issue with auto-start on webiopi



PIGPIO


wget abyz.co.uk/rpi/pigpio/pigpio.zip
unzip pigpio.zip
cd PIGPIO
make
make install
sudo systemctl enable webiopi.service
sudo systemctl start webiopi.service
tar xvzf WebIOPi-x.y.z.tar.gz
$ cd WebIOPi-x.y.z
$ sed -i 's/ python3//' setup.sh
$ sudo ./setup.sh
$ sudo webiopi-passwd
$ sudo service webiopi restart
