''' The code has been written by Rishi Gaurav Bhatanagar (@rishigb) for a #stilllife project (with @justusbruns) , all code written and tested 
with Pi B/B+, in association with Workbench Projects'''
import picamera
import requests
import time
''' The following code will be used to send a picture '''
url_image = 'https://still-life.herokuapp.com/pagemulti'
camera = picamera.PiCamera()
#camera.resolution = (1920, 1080)
#camera.resolution = (1087,728)
camera.resolution = (1280,720) #suits the screens best, 650Kb file.
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
        camera.capture(initialName+'.jpeg')
        time.sleep(timeInterval)
        fileName(initialName+'.jpeg',finalName) #This function is going to add the extension to finalName
'''The image being captured here will be stored in the same folder as the code '''

captureImage("Rishi","maybethis",0.5)



