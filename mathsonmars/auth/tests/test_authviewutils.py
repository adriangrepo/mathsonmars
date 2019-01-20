#! ../env/bin/python
# -*- coding: utf-8 -*-

import unittest
import logging
import string
import random
from random import shuffle

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestAuthViewUtils(unittest.TestCase):
    '''couldnt run unit test on external code so cpoied and pasted here'''
    
    @classmethod
    def generateUsername(cls, postfix_length, param_initials):
        """Function to generate a semi-random username"""
        assert isinstance(postfix_length, int), "Integer"
        assert (len(param_initials)==2), "2 digits"
        numbers = []
        for index in range(postfix_length):
            number_postfix = random.randint(0,9)
            numbers.append(str(number_postfix))
        str_postfix = "".join(numbers)
        username = param_initials.lower() + str_postfix
        return username
    
    @classmethod
    def generatePass(cls, pass_length):
        """Function to generate a password"""
        chars=string.ascii_letters + string.digits + string.punctuation
        password = []
        for _ in range(pass_length):
            password.append(random.choice(chars))
        return ''.join(password)
    
    @classmethod
    def generateWeakPass(cls, pass_length):
        """Function to generate a weak password"""
        digits = string.digits
        chars = string.ascii_letters
        password = []
        for _ in range(pass_length-2):
            password.append(random.choice(digits))
        for _ in range(2):
            password.append(random.choice(chars).lower())
        shuffle(password)
        return ''.join(password)
    
    @classmethod
    def generatePassLimitedPuctuation(cls, pass_length):
        """Function to generate a password with limited punctuation chars"""
        limited_punct = '#$*&!@:<>?%'
        chars=string.ascii_letters + string.digits + limited_punct
        password = []
        for _ in range(pass_length):
            password.append(random.choice(chars))
        return ''.join(password)

    def test_generateWeakPass(self):
        logger.debug("test_generateWeakPass")
        length = 6
        weak_pass = TestAuthViewUtils.generateWeakPass(length)
        self.assertEqual(6, len(weak_pass))
        logger.debug("--test_generateWeakPass: {0}".format(weak_pass))
        
    def test_generatePass(self):
        logger.debug("test_generatePass")
        length = 6
        password = TestAuthViewUtils.generatePass(length)
        self.assertEqual(6, len(password))
        logger.debug("--test_generatePass: {0}".format(password))
        
    def test_generateUserName(self):
        logger.debug("test_generateUserName")
        postfix_length = 5
        param_initials = 'ag'
        username = TestAuthViewUtils.generateUsername(postfix_length, param_initials)   
        logger.debug("--test_generateUserName() username:{0}".format(username))
            
    def test_generatePassLimitedPuctuation(self):
        logger.debug("test_generatePassLimitedPuctuation")
        length = 6
        password = TestAuthViewUtils.generatePassLimitedPuctuation(length)
        self.assertEqual(6, len(password))
        logger.debug("--test_generatePassLimitedPuctuation: {0}".format(password))
            
    ######loops###########
    
    def test_generatePass_multipletimes(self):
        logger.debug("test_generatePass_multipletimes")
        length = 6
        for i in range(10):
            logger.debug("--test_generatePass_multipletimes() count:{0}".format(i))
            TestAuthViewUtils.test_generatePass(self)
            
    def test_generateWeakPass_multipletimes(self):
        logger.debug("test_generateWeakPass_multipletimes")
        length = 6
        for i in range(10):
            logger.debug("--test_generateWeakPass_multipletimes() count:{0}".format(i))
            TestAuthViewUtils.test_generateWeakPass(self)
            

        
    def test_generatePassLimitedPuctuation_multipletimes(self):
        logger.debug("test_generatePassLimitedPuctuation_multipletimes")
        length = 6
        for i in range(10):
            logger.debug("--test_generatePassLimitedPuctuation_multipletimes() count:{0}".format(i))
            TestAuthViewUtils.test_generatePassLimitedPuctuation(self)
        

    
if __name__ == "__main__":
    unittest.main()