__author__ = 'root'
import  math
class Data:
    __slots__="forwardLink","backLink","chainLink","data"

    def __init__(self,data):
        self.data=data
        self.forwardLink=None
        self.backLink=None
        self.chainLink=None

    def hashCode(self,lookup):
        power=0
        hashCode=0
        for item in self.data:
            hashCode+=hashCode*lookup[item]*math.pow(31,power)
            power+=1
        return hashCode