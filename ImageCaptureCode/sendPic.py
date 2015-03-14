import picamera
import requests
import time
''' The following code will be used to send a picture '''
url_image = 'https://still-life.herokuapp.com/pagemulti'

####################################### Image Posting #######################################################
def fileName (cur_name,post_name):
        files ={post_name:open(cur_name,'rb')}
        r = requests.post(url_image,files=files)
        if (r.status_code) ==200:
                print "Posted"
        else:
                print r.status_code

#val = raw_input("Enter the current value of the file with the extension: ")
#val1 = raw_input ("Please enter the filename you want to keep after posting: ")
#fileName(val,val1)

####################################Capturing Image ##########################################################
nameOfValue = raw_input("Enter the name you want to give the file, with extension: ")
camera = picamera.PiCamera()
camera.capture('stilllife.jpg')
time.sleep(2)
fileName('stilllife.jpg','stilllife')

