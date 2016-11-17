# coding=utf-8

"""
   Date: 18/11/2016
   Author: qinjiangbo@github.io
   stop words for the documents, which will be removed in the process
"""


class StopWords(object):
    set = set()  # hash set for storing stop words
    INSTANCE = None  # singleton

    def get_instance(self):
        if self.INSTANCE == None:
            self.INSTANCE = StopWords()
        return self.INSTANCE
