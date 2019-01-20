import csv

class ListUtils(object):

    @classmethod
    def missingElements(cls, inList):
        start, end = inList[0], inList[-1]
        return sorted(set(range(start, end + 1)).difference(inList))
    
    @classmethod
    def listOfListsToCapitalColumnList(cls, list_of_lists, column_number):
        columnN = [row[column_number] for row in list_of_lists]
        stripped = []
        name = ''
        for item in columnN:
            name = item.strip()
            stripped.append(name.capitalize())
        return stripped
    
    @classmethod
    def csvStringToList(cls, paramList):
        outList = []
        if paramList is not None:
            outList = paramList.split(",")
        return list(outList)
    

    