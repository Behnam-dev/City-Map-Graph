class Linked_list:
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None
 
    def __str__(self):
        return str(self.data)


# class Hash:
#     def __init__(self, length):
    #    self.__list = [] 


class adjacent_list:
    def __init__(self, length):
        self.__list = []
        for i in range(length):
            self.__list.append(i)

    def add(self, node):
        pass


class Node:
    def __init__(self, type, code):
        pass


class Ambulance:
    def __init__(self, location, hospital):
        self.hospital = hospital
        self.location = location