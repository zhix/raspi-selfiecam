#!/usr/bin/env python

from gpiozero import LED, Button
from signal import pause
from time import sleep

from picamera import PiCamera
from time import sleep
from datetime import datetime

import sys
from twython import Twython

# import Image

CONSUMER_KEY = 'AmVfORMpEEuT2ZNY7b3gAyo75'
CONSUMER_SECRET = 'glU63NGYMH0gIbiwYkLXlPPECApiQSmyNqZTtOS2uOfc7NUGWV'
ACCESS_KEY = '860443137768017920-o1EavrwRT2PB4XecXvwY8JQ1appHpgg'
ACCESS_SECRET = '4Le2uqnZBlbyShNTXkVgkrLRfhFPOjPpxan6GEG5rXslk'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

led1 = LED(26)
led2 = LED(13)
led3 = LED(19)

button = Button(6, pull_up=False)
camera = PiCamera()

msg = "This is a selfie camera. \nPress the button when you are ready!"
print(msg)

while True:
        
	if button.value == True:
		camera.start_preview()
		led1.on()
		sleep(1)
		camera.annotate_text = 'Get ready! \n1....'
		print("Get ready! \n1....")
		led2.on()
		sleep(1)
		camera.annotate_text = 'Get ready! \n2....'
		print("Get ready! \n2....")
		led3.on()
		sleep(1)
		camera.annotate_text = 'Get ready! \n3....'
		print("Get ready! \n3....")
		led1.off()
		led2.off()
		led3.off()
		sleep(0.5)
		camera.annotate_text = 'Say cheeeesee!'
		print("Say cheeeesee!")
		sleep(0.5)
		led1.on()
		led2.on()
		led3.on()
		sleep(0.05)
		led1.off()
		led2.off()
		led3.off()
		sleep(0.05)
		led1.on()
		led2.on()
		led3.on()
		sleep(0.05)
		led1.off()
		led2.off()
		led3.off()
		sleep(0.05)
		led1.on()
		led2.on()
		led3.on()
		sleep(0.05)
		led1.off()
		led2.off()
		led3.off()
		sleep(0.05)
		led1.on()
		led2.on()
		led3.on()
		sleep(0.05)
		led1.off()
		led2.off()
		led3.off()
		sleep(0.05)
		led1.on()
		led2.on()
		led3.on()
		sleep(0.05)
		led1.off()
		led2.off()
		led3.off()
		sleep(0.05)
		led1.on()
		led2.on()
		led3.on()
		sleep(0.05)
		led1.off()
		led2.off()
		led3.off()
		sleep(0.05)
		led1.on()
		led2.on()
		led3.on()
		sleep(0.05)
		camera.stop_preview()
		sleep(0.05)
		currentTime = str(datetime.now())
		camera.capture('/home/pi/Pictures/image%s.jpg' %currentTime)
		photo = open('/home/pi/Pictures/image%s.jpg' %currentTime,'rb')

		# img = Image.open('/home/pi/Pictures/image%s.jpg' %currentTime)
		# img.show()

		try: 
			api.update_status_with_media(media=photo, status='Come and join us on the KEMBARA #mydigitalmaker BERSAMA PINTAR bus, take a selfie and get Tweeted!')
			msg2 = "Your photo is now uploaded on Twitter! Go check it out @DigitalMakerBot"
			sleep(5)
		except: 
			msg2 = "Our network connection seems to be facing some problem. =( \nGo check it out @DigitalMakerBot"
			pass

		time.sleep(3)
		# img.show()

		print(msg2)
		print("\n\n\n\n\n\n\n\n\n\n")
		print(msg)
	
	
	if button.value == False:
		led1.off()
		led2.off()
		led3.off()
		
	sleep(0.2)

