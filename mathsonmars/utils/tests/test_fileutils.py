#! ../env/bin/python
# -*- coding: utf-8 -*-

import unittest
import logging
from mathsonmars.utils.fileutils import FileUtils

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestFileUtils(unittest.TestCase):

    def test_getLinesFromFile(self):
        logger.debug("test_getLinesFromFile")
        inFile = '../../../data/dist.female.first.txt'
        delimiter = ','
        list_of_lists = FileUtils.getLinesFromFile(inFile, delimiter)

        self.assertEqual(4275, len(list_of_lists))
    
        
    def test_resortFile(self):
        inFile = '../../../data/dist.female.first.txt'
        outFile = 'output1.txt'
        postfix = "'"
        prefix = "FEMALE_NAMES_STR = '"
        FileUtils.resortFile(inFile, outFile, prefix, postfix)
                
if __name__ == "__main__":
    unittest.main()