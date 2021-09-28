class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__next = None
    
    def __del__(self):
        print("{} is deleted".format(self.data))

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data
    
    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next = n