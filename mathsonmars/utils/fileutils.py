'''
Created on 17 Jun 2016

@author: a
'''
import csv
from mathsonmars.utils.listutils import ListUtils

class FileUtils(object):
    
    @classmethod
    def getLinesFromFile(cls, inFile, delimiter):
        #tab delimiter='\t'
        data = list(csv.reader(open(inFile), delimiter=delimiter))
        return data
    
        
    @classmethod
    def resortFile(cls, inFile, outFile, prefix, postfix):
        f = open(outFile, 'w')
        delimiter = ','
        list_of_lists = FileUtils.getLinesFromFile(inFile, delimiter)
        names = ListUtils.listOfListsToCapitalColumnList(list_of_lists, 0)
        names.sort()
        names_csv = ",".join(names )
        with open(outFile, "w") as text_file:
            text_file.write(prefix+names_csv +postfix)
