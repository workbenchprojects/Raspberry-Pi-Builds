
import picamera
import requests
import time
''' The following code will be used to send a picture '''
#url_image = 'https://still-life.herokuapp.com/pagemulti'
url_image = 'localhost:4000/pagemulti'
camera = picamera.PiCamera()
camera.resolution =(640,460)
#camera.resolution = (1920, 1080)
#camera.resolution = (1087,728)
#camera.resolution = (1280,720) #suits the screens best, 650Kb file.
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
'''The image being captured here will bwe stored in the same folder as the code '''
######### Pi dies every 3 days for some unknown reason, it freezes and all the processes stop, hence we will restart is in 2 days #######
def restart():
    command = "/usr/bin/sudo /sbin/reboot "
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output

while True:
	try:
        	captureImage("Rishi","image_stream",0.01)
		#wait for 2 days and call restart()
	except Exception,e:
		print "Exception occoured",e
		restart()
