import requests
import time
import json
url_ack = 'http://localhost:3000/ack'
def postRequest(inp):
    headers = {'content-type': 'application/json'} #All provided in the documentation
    r = requests.post(url_ack,data=json.dumps(inp),headers = headers) 
    print (r.text)
    r = requests.get(url_ack)
    r.status_code
    #print curValue
    if (r.status_code==200):
        print "Posted ", r.status_code
    else:
       print "Error Response Code",r.status_code
def ackPost(cmd):
    postRequest({"value":cmd})

ackPost("f")