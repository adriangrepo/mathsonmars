#! ../env/bin/python
# -*- coding: utf-8 -*-

import unittest
import logging
import random


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestApplViewUtils(unittest.TestCase):
    '''couldnt run unit test on external code so copied and pasted here'''
    
    @classmethod
    def selectFromList(cls, data_list, total_questions):
        '''data selection from a list based on questions length
        @param data_list: list of data
        @param total_questions: int
        '''
        new_list = []
        if data_list is not None and len(data_list)>0:
            new_list = data_list.copy()
            data_list_len = len(data_list)
            if data_list_len > total_questions:
                random.shuffle(new_list)
                questions_to_remove = data_list_len-total_questions 
                for i in range(questions_to_remove): 
                    new_list.pop()
            elif data_list_len < total_questions:
                questions_to_add = total_questions - data_list_len
                for i in range(questions_to_add):
                    new_list.append(random.choice(data_list))
        return new_list
         

    def test_selectFromList_0(self):
        logger.debug("test_selectFromList_0")
        data_list = [1,2,3,4,5,6,7]
        total_questions = 4
        result_list = TestApplViewUtils.selectFromList(data_list, total_questions)
        self.assertEqual(4, len(result_list))
        self.assertEqual(True, len(result_list)==len(set(result_list)))
        
    def test_selectFromList_1(self):
        logger.debug("test_selectFromList1")
        data_list = []
        total_questions = 10
        result_list = TestApplViewUtils.selectFromList(data_list, total_questions)
        self.assertEqual(0, len(result_list))

        
    def test_selectFromList_2(self):
        logger.debug("test_selectFromList2")
        data_list = [1,2,3,4,5,6,7]
        total_questions = 10
        result_list = TestApplViewUtils.selectFromList(data_list, total_questions)
        self.assertEqual(10, len(result_list))
        self.assertEqual(False, len(result_list)==len(set(result_list)))
        
        
    
if __name__ == "__main__":
    unittest.main()