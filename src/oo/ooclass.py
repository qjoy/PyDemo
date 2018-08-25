
class ooclass(object):

    __param1 = 'abcdef'
    __param2 = 123

    def __init__(self, p1 = 1):
        self.__param1 = p1

        print ("create obj from " + self.__class__.__name__)

    def __del__(self):
        print ("delete obj from " + self.__class__.__name__)


    @property
    def getparam1(self):
        return self.__param1

    def __eq__(self, other):
        if isinstance(other, ooclass):
            if self.__param1 == other.__param1:
                return True
            else:
                return False
        raise Exception('The type of object must be myclass')
