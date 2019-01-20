#! ../env/bin/python
# -*- coding: utf-8 -*-
import sys
print("TestConfig sys.path: {0}".format(sys.path))
import unittest
from mathsonmars.auth.viewutils import getLinksInText
from mathsonmars.auth.viewutils import isEmpty

class TestViewUtils(unittest.TestCase):

    def test_getLinksInText(self):
        """ Test links in text """

        page_text = "my page with http://www.badsite.com"
        ok_text = "my page with not urls just some text and the odd www http"
        other_text = "http://lxml.de/installation.html"
        more_text = "other stuff here https://www.google.com.au/ https://realpython.com/"
        page_array = getLinksInText(page_text)
        is_empty = isEmpty(page_array)
        self.assertEqual(False, is_empty)
        
        ok_array = getLinksInText(ok_text)
        is_empty = isEmpty(ok_array)
        self.assertEqual(True, is_empty)
                
        other_array = getLinksInText(other_text)
        is_empty = isEmpty(other_array)
        self.assertEqual(False, is_empty)
        
        more_array = getLinksInText(more_text)
        is_empty = isEmpty(more_array)
        self.assertEqual(False, is_empty)
    
if __name__ == "__main__":
    unittest.main()