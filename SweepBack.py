#-*- coding:utf-8 -*-

import testRequests
import urllib
import param
class Sweep:
    
    cookies     = ""
    sender      = None
    
    
    @staticmethod
    def establish(cookies):
        
        Sweep.cookies= cookies
        Sweep.sender = testRequests.LaunchRequest(Sweep.cookies)
        
    @staticmethod
    def sweep(delValue, isReceive):
        
        params = {}
        #delValue is the number to delete.
        Sweep.sender.headers['Referer'] = param.noDecComShowUnReadMessage_url
        Sweep.sender.headers['Accept']  = "*/*"
        Sweep.sender.headers['Connection'] = "close"
        params['delValues']             = delValue
        params['allMessageType']        = "0"
        
        if isReceive:
            
            params['senderFlag']        = "false"
            
        else :
            
            params['senderFlag']        = "true"
        
	#        print params
        Sweep.sender.send(param.delMail_url, params, "post", 1)
        
        
    
