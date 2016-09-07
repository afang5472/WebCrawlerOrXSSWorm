#-*- coding:utf-8 -*-

import re
import logs
import email
import UserInfo
    
class parsehtml:
    
    ptnforUname = re.compile("window.open\(\'\/(.+?)\',\'_blank\'\);")
    ptnforSex   = re.compile('checked=\"checked\" value="(.+?)"')
    ptnforDegree= re.compile("name=\"profile.degree\" id=\"degree\" value=\"(.+?)\"")
    
    @staticmethod
    def patternGen(middlestr):
        
        temp_patternstr = "name=\"" + middlestr + '\" value=\"(.+?)\"'
        return re.compile(temp_patternstr)
    @staticmethod
    def parse(htmlcontent):
        
        InfoCol         = {}
        USERNAME        = parsehtml.check(parsehtml.ptnforUname,htmlcontent)
        PASSWORD        = parsehtml.check(parsehtml.patternGen("account.password"),htmlcontent)
        if USERNAME == "" and PASSWORD == "":
            
            logs.LOG.WriteLog("[*] HTML Parsing Failed At " + USERNAME + PASSWORD)
            return None
        
        Email           = parsehtml.check(parsehtml.patternGen("profile.workEmail"),htmlcontent)
        ChnName         = parsehtml.check(parsehtml.patternGen("profile.chineseName"),htmlcontent)
        Sex             = parsehtml.check(parsehtml.ptnforSex, htmlcontent)
        Academic        = parsehtml.check(parsehtml.ptnforDegree,htmlcontent)
        Job             = parsehtml.check(parsehtml.patternGen("profile.scholarTitle"),htmlcontent)
        Work_unit       = parsehtml.check(parsehtml.patternGen("profile.workUnit"),htmlcontent)
        Department      = parsehtml.check(parsehtml.patternGen("profile.workDepartment"),htmlcontent)
        Profession      = parsehtml.check(parsehtml.patternGen("scholarFieldFirst"),htmlcontent)
        Address         = parsehtml.check(parsehtml.patternGen("profile.address"),htmlcontent)
        EngName         = parsehtml.check(parsehtml.patternGen("profile.englishName"),htmlcontent)
        Title           = parsehtml.check(parsehtml.patternGen("profile.scholarTitleEn"),htmlcontent)
        Affiliation     = parsehtml.check(parsehtml.patternGen("profile.workUnitEn"),htmlcontent)
        
        InfoCol = UserInfo.dbopt.InfoCollect(USERNAME, PASSWORD, Email, ChnName, Sex, Academic, 
                                             Job, Work_unit, Department, Profession,
                                              Address, EngName, Title, Affiliation)
        return InfoCol
    @staticmethod
    def check(regex, htmlcontent):
        
        temp = regex.findall(htmlcontent)
        vari = ""
        if len(temp) == 0:
            
            return vari
        
        else:
            return temp[0]
    
    @staticmethod
    def findFriends(ajaxcontent):
        
        regex1 = re.compile('\"profileUsername\":\"(.+?)\",')
        res    = list(set(regex1.findall(ajaxcontent)))
        return res
    
    @staticmethod
    def findRecommend(htmlcontent):
        
        regex1 = re.compile('username\":\"(.+?)\"')
        res     = list(set(regex1.findall(htmlcontent)))
        return res
        