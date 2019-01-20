#! ../env/bin/python
# -*- coding: utf-8 -*-

import unittest
import logging
from mathsonmars.utils.fileutils import FileUtils
from mathsonmars.utils.listutils import ListUtils

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestListUtils(unittest.TestCase):
    
    

    def test_listOfListsToCapitalColumnList(self):
        logger.debug("test_getLinesFromFile")
        inFile = '../../../data/dist.female.first.txt'
        delimiter = ','
        list_of_lists = FileUtils.getLinesFromFile(inFile, delimiter)
        names = ListUtils.listOfListsToCapitalColumnList(list_of_lists, 0)
        names.sort()
        names_csv = ",".join(names )
        logger.debug("--test_listOfListsToCapitalColumnList names_csv:{0}".format(names_csv))
        self.assertEqual(4275, len(names))
        self.assertEqual('Mary', names[0])
        
    
if __name__ == "__main__":
    unittest.main()