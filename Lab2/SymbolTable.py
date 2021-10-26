class SymbolTable:
    def __init__(self):
        self._sortedList = []
        self._size = 0

    def add(self, value):
        id = self.search(value)
        if id != -1:
            return id
        self._sortedList.append((value, self._size))
        self._size += 1
        self._sortedList = sorted(self._sortedList, key=lambda x: x[0])
        return self._size - 1


    def search(self, value):
        for i in self._sortedList:
            if i[0] == value:
                return i[1]
        return -1



    def display(self):
        for i in self._sortedList:
            print(i[0] + " " + i[1])



    def __str__(self):
        return str(self._sortedList)



