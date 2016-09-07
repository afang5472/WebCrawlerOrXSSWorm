#-*- coding:utf-8 -*-

import os
import time

ISOTIMEFORMAT = '%Y-%m-%d %X'

class LOG:
    
    Filepath = ""
    Filename = ""
    
    def __init__(self,FilePath, FileName):
    
        LOG.Filename = FileName
        LOG.Filepath = FilePath
        
        if not os.path.exists(FilePath):  
            
            os.makedirs(FilePath)
        fp = open(FilePath + FileName, 'a')
        fp.write("[*] Logger Initiate At: " + time.strftime(ISOTIMEFORMAT) + '\n\n')
        fp.close()

    @staticmethod
    def WriteLog(content):
        
        fp = open(LOG.Filepath + LOG.Filename, 'a')
        fp.write(content + '\n')
        fp.close()
        
if __name__ == "__main__":
    
    logger = LOG("/home/zeroxcc/testlog/", "Cook.log")
    