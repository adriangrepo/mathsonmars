#http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Messenger.html

class Messenger:
    #messenger types
    QQ_ANS = "question answer"
    QQ_ANS_VARS = "questions answer variable"
    #used for chunking
    QQ_DIFF_REMAIN_ANS_CHUNKPOS = "question difference remaining answer chunkpos"
    FUN_CHUNKS = "fun chunks"
    
    def __init__(self, **kwargs):
        self.__dict__ = kwargs
        #eg m = Messenger(info="some information", b=['a', 'list'])