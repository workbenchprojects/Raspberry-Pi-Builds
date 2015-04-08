''' The code has been written by Rishi Gaurav Bhatanagar (@rishigb) for a #stilllife project (with @justusbruns) , all code written and tested
with Pi B/B+, in association with Workbench Projects'''
import picamera
import requests
import time
import tweepy
import os
import math
import datetime
''' The following code will be used to send a picture '''
url_image = 'http://localhost:3000/pagemulti'
camera = picamera.PiCamera()
camera.resolution =(640,360)
camera.sharpness = 5
#camera.resolution = (1920, 1080)
#camera.resolution = (1087,728)
#camera.resolution = (1280,720) #suits the screens best, 650Kb file.
camera.crop=(0.1,0.1,0.8,0.8)
camera.awb_mode ='auto'
camera.quality = 2
####################################### Image Posting #######################################################
def fileName (cur_name,post_name):
        files ={post_name:open(cur_name,'rb')}
        r = requests.post(url_image,files=files)
        if (r.status_code) ==200:
                print "Posted"
        else:
                print r.status_code

####################################Capturing Image ##########################################################
def captureImage(initialName,finalName,timeInterval):
        camera.capture(initialName+'.jpg')
        time.sleep(timeInterval)
        fileName(initialName+'.jpg',finalName) #This function is going to add the extension to finalName
	print "clicked"
'''The image being captured here will be stored in the same folder as the code '''
########################## Loop to check the time difference ##############
before = datetime.datetime.now() #Current time
#################Tweet the the image ########################
def Tweet():
        CONSUMER_KEY = ''
        CONSUMER_SECRET = ''
        ACCESS_KEY = ''
        ACCESS_SECRET = ''
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.secure = True
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        # access the Twitter API using tweepy with OAuth
        api = tweepy.API(auth)
        #getting the parameter passed via the shell command from the Arduino Sketch
        status = "Live now "
        fn = os.path.abspath('Rishi.jpg')
        #UpdateStatus of twitter called with the image file
        api.update_with_media(fn, status=status)
        print "tweet sent"



while True:
       
	try:
		captureImage("Rishi","image_stream",60)
        	after = datetime.datetime.now() 
		Check for time difference in hours, if it is more than 6 hours, click a pictur
		#Wait for 6 hours and then call Tweet()
		
	except Exception,e:
		print "restart",e
