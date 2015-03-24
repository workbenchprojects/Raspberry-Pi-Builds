#Send pictures to a server using an IOT board display them on a webpage/phone app

You will see 2 different folders here:
1. Images
2. node_modules

Images is the folder that we have created in the code when we use [FilePath:"./images/"] in the code. The get function on this server will also be related at the same link. Hence, you will see [rest.getfile('/images') ] .


node_module : It is the folder that contains all the modules required by the server to run it. Basically, all the modules that have been written in the server with 'require' in front of them will be used here. 
To automatically add all the modules to the server, you should use :
$ npm install moduleName -- save



Special thanks to Ajith N N (github.com/ajithnn) for helping me out!
