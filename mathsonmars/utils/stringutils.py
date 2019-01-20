'''
Created on 12 Jun 2016

@author: a
'''
from mathsonmars.marslogger import logger
import re

class StringUtils(object):
    '''
    classdocs
    '''

    @classmethod
    def convertToString(cls, inString):
        outStr = "";
        try:
            outStr = str(inString)
            return outStr;
        except ValueError:
            logger.error("--convertToString() not a string: {0}".format(inString))
            return None
    
    @classmethod
    def strToBool(cls, s):
        assert(isinstance(s, str))
        if s.lower() == 'true'.lower():
             return True
        elif s.lower() == 'false'.lower():
             return False
        else:
             logger.error("--strToBool() not a boolean: {0}".format(s))
             return None
      
    @classmethod   
    def hasNumbers(cls, inputString):
        containsNumber = any(char.isdigit() for char in inputString)
        return containsNumber

    @classmethod
    def hasAlphabetics(cls, inputString):
        containsAlpha = re.search('[a-zA-Z]', inputString)
        if containsAlpha is None:
            return False
        else:
            return True
        
