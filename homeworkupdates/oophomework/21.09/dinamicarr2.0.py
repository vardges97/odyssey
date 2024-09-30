import ctypes
class DynamicArray:
    def __init__(self,capacity:int = 10):
        self.currentindex = 0
        self.capacity = 10
        self.arr = self.addd(self.capacity)

    def __len__(self):
        return self.currentindex

    def capa(self):
        print(self.capacity)
        print(self.arr)

    def __getitem__(self, item):
        if not 0 <= item <= self.currentindex:
            return IndexError("item is out of bounds")
        return self.arr[item]

    # def __repr__(self):
    #     return (f"current array: ({self.arr}), with capacity: ({self.capacity}))")

    def __str__(self):
        tmp = ""
        for i in range(self.currentindex):
            tmp = tmp + str(self.arr[i]) + ","
        tmp = tmp[:-1]
        return "[" + tmp + "]"

    def __add__(self, other):
        tmp1 = ""
        tmp2 = ""
        if self.currentindex == self.capacity:
            self.arr_resize()
        for i in range(self.currentindex):
            tmp1 = tmp1 + str(self.arr[i]) + ","
        tmp1 = tmp1[:-1]
        for i in range(other.currentindex):
            tmp2 = tmp2 + str(other.arr[i])+","
        tmp2 = tmp2[:-1]
        return "[" + tmp1 + "," + tmp2 + "]"

    def __iadd__(self, other):
        if self.currentindex == self.capacity:
            self.arr_resize()
        x = self + other
        self.arr = x.arr
        return self.arr

    def __iter__(self):
        for i in self.arr:
            print(i)
    def __repr__(self):
        return str(int(self))

    def __next__(self):
        iterator = iter(self.arr)
        try:
            while True:
                element = next(iterator)
                print(element)
        except StopIteration:
            pass
    def __eq__(self, other)->bool:
        if self.arr == other.arr:
            return True
        else:
            return False

    def __ne__(self, other)->bool:
        if self.arr != other.arr:
            return True
        else:
            return False

    def __lt__(self, other) -> bool:
        for i in range(len(self.arr)):
            for j in range(len(other.arr)):
                return self.arr[i] < other[j]

    def __le__(self, other) -> bool:
        for i in range(len(self.arr)):
            for j in range(len(other.arr)):
                return self.arr[i] <= other[j]


    def __gt__(self, other) -> bool:
        for i in range(len(self.arr)):
            for j in range(len(other.arr)):
                return self.arr[i] > other[j]

    def __ge__(self, other) -> bool:
        for i in range(len(self.arr)):
            for j in range(len(other.arr)):
                return self.arr[i] >= other[j]


    def arr_resize(self):
        self.capacity *= 2
        newarr = [0] * self.capacity
        for i in range(len(self.arr)):
            newarr[i] = self.arr[i]
        self.arr = newarr
    def addd(self,newcap):
        return (newcap*ctypes.py_object)()

    def append(self,elem):
        if self.currentindex == self.capacity:
            self.arr_resize()
        self.arr[self.currentindex] = elem
        self.currentindex += 1
        # print(self.arr)

    def insert_at(self,item,index):
        if index < 0 or index > self.currentindex:
            raise IndexError("index out of bounds")
        if self.currentindex == self.capacity:
            self.arr_resize()
        for i in range(self.currentindex-1,index-1,-1):
            self.arr[i+1] = self.arr[i]
        self.arr[index]=item
        self.currentindex += 1
        return DynamicArray


myArr = DynamicArray()
myArr.append(12)
myArr.append(31)
myArr.append(15)
myArr.append(74)
myArr.append(21)
myArr.append(25)
myArr2 = DynamicArray()
myArr2.append(21)
myArr2.append(13)
myArr2.append(51)
myArr2.append(47)
myArr2.append(12)
myArr2.append(52)
print(len(myArr))
print(myArr)
print(myArr2>myArr)
