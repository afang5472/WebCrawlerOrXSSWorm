#-*- coding:utf-8 -*-

import requests
from pymongo import MongoClient

#Two - Most Important Thing.

#FLags
"""
username        = ""
password_hash   = ""
EMAIL           = ""
ChineseName     = ""
sex             = ""
academic        = ""
JOB             = ""
WORK_UNIT       = ""
DEPARTMENT      = ""
PROFESSION      = ""
COMMUNICATE_ADD = ""
ENG_NAME        = ""
TITLE           = ""
AFFILIATION     = ""
"""

#Test-Pass.
class dbopt:
    
    #Pick Database
    client = MongoClient()
    db     = client.Wand
    
    @staticmethod
    def saveUserInfo(InfoCollection):
    
        dbopt.db.wand.save(InfoCollection)
    
    @staticmethod
    def InfoCollect(uname, passwd, Email,cnName, sex, academ, job, work_unit, 
                department, profession, address, eng_name , title, affliation ):
    
        InfoCollection = {}
        InfoCollection['userName']          = uname
        InfoCollection['passWordhash']      = passwd
        InfoCollection['Email']             = Email
        InfoCollection['chnName']           = cnName
        InfoCollection['Sex']               = sex
        InfoCollection['academic']          = academ
        InfoCollection['Job']               = job
        InfoCollection['work_Unit']         = work_unit
        InfoCollection['department']        = department
        InfoCollection['profession']        = profession
        InfoCollection['commun-address']    = address
        InfoCollection['english_name']      = eng_name
        InfoCollection['title']             = title
        InfoCollection['Affliation']        = affliation
    
        return InfoCollection
    
    @staticmethod
    def checkExistence(UserName):
    
        res = dbopt.db.sentMail.find_one({"userName":UserName})
        if res is None:
            return 0
        else:
            return 1
        
    @staticmethod
    def addVisited(UserName):
        
        dbopt.db.sentMail.save({"userName":UserName})
        
        