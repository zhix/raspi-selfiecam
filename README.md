## Building your own selfie camera

### Preparing the environment 

1. Installing Twython 

```
git clone https://github.com/ryanmcgrath/twython.git
cd twython
sudo python setup.py install
```

For more information, read documentation: https://twython.readthedocs.io/en/latest/index.html

2. Enabling camera
Fix the camera into Raspberry Pi. You may follow this guide for more instruction in [setting it up physically] (https://www.raspberrypi.org/learning/getting-started-with-picamera/)

```
sudo raspi-config
```

Go to Option 5 - Interfacing Options
Select Camera to Enable it. 
If asked to reboot, press Yes. 


### Let's get started

In the same directory, run the program by ```python selfieCam.py``` 



### You may turn the python programme code into executable file 

```
chmod +x selfieCam.py
``` 

When you are done, navigate to File Manager. Look for ```selfieCamp.py``` file in the File Manager, and double click it. Click on "Execute in Terminal". And... Voila!
