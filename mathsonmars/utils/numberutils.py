'''
Created on 9 Jan 2016

@author: a
'''
from mathsonmars.marslogger import logger

class NumberUtils(object):
    '''
    classdocs
    '''

    @classmethod
    def isFloat(cls, x):
        try:
            a = float(x)
        except ValueError:
            return False
        else:
            return True
        
    @classmethod
    def isInt(cls, x):
        try:
            a = float(x)
            b = int(a)
        except ValueError:
            return False
        else:
            return a == b
        
    @classmethod 
    def representsInt(cls, s):
        try: 
            int(s)
            return True
        except ValueError:
            return False
        
    @classmethod
    def convertToInt(cls, s):
        i = 0;
        try:
            i = int(s)
            return i;
        except ValueError:
            logger.error("--convertToInt() not an int: {0}".format(s))
            return None
        
    @classmethod
    def representsFloat(cls, s):
        try: 
            float(s)
            return True
        except ValueError:
            return False
       
    @classmethod 
    def convertToFloat(cls, s):
        i = 0.0;
        if (s is not None):
            try:
                i = float(s)
                return i;
            except ValueError:
                logger.error("--convertToFloat() not a float: {0}".format(s))
                return None
        else:
            return None
        
    @classmethod 
    def reconstructBooleanList(cls, listLength, intArray):
        '''creates a boolean list with true values at locations specified in intArray'''
        vals = [False] * listLength
        for i, item in enumerate(intArray):
            index = NumberUtils.convertToInt(intArray[i])
            vals[index] = True
        return vals