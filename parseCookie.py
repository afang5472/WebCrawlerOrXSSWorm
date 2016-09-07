#-*- coding:utf-8 -*-
#Simply Finding a way to depart Cookie Files

import urllib 

def parseCookie(cookiestr):
    
    cookies   = {}
    
    #CNZZDATA is URLEncoded Twice.
    Spart = cookiestr.split(";")
    for str in Spart:
        
        str = str.strip()
        temp= str.split("=")
        if len(temp) == 1:
            
            tag     = temp[0]
            value   = ""
        else:
            
            tag   = temp[0]
            value = temp[1]
        cookies[tag] = value
        
    #We need a formal way of parsing cookie.
    
    #print cookies.keys()
    #print cookies.values()
    return cookies
    
if __name__ == "__main__":
    
    str = ""
    parseCookie(str)
    
    
    