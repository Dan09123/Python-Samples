""" This is a demo that tests how python class works"""

class base(object):
    apple = 1912;
    def __init__(self, list = [], dict = ()):
        self.list=list
        self.dict =dict
    def addtolist(self,val):
        self.list.append(val)
    def addtodict(self,key,val):
        self.dict[key] = val
    def countlist(self):
        return len(self.list)
    def countdict(self):
        return len(self.dict)


class sub(base):
    def __init__(self, list = [],dict=(),sett = ([])):
        super(sub,self).__init__(list,dict)
        self.sett=set(self.list)
        self.__frame = ''
    def counter(self):
        return len(self.sett)
    def prints(self):
        print "total element", self.counter()
        print self.sett
        print self.list
        print self.dict
    @property
    def name(self):
        return self.__frame + "***"
    @name.setter
    def name(self, val):
        self.__frame = val


def test():

    ll = [1,3,5]
    hh = {}
    hh["2"] = 9
    ss = ([999,888])
    subclass = sub(ll,hh,ss)
    subclass.prints()
    print subclass.apple
    subclass.setter

if __name__=="__main__":

    test()