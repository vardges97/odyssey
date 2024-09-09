class Employee:
    def __init__(self,id,name,salary):
        self.__id = id
        self.__name = name
        self.__salary = salary
        if salary < 0:
            raise ValueError("salary cant be negative")

    def get_attr(self):
        return (self.__id,self.__name,self.__salary)


p1 = Employee('001',"rick",120000)
# print(p1.get_attr())


class book:
    def __init__(self,title,author,price):
        self.__title = title
        self.__author = author
        self.__price = price
        if price < 20:
            raise ValueError

    def get_attr(self):
        return (self.__title,self.__author,self.__price)

b1 = book("the odyssey",'homer',45)
# print(b1.get_attr())


class student:
    def __init__(self,name,roll_num,grades):
        self.__roll_num = roll_num
        self.__name = name
        self.__grades = grades
        # self.studentlist=[]
        for i in self.__grades:
            if i < 0 or i > 100:
                raise ValueError
            else:
                print("alls well")
    def getstudent(self):
        return self.studentlist
    def gradeaverage(self):
        list = []
        for i in self.__grades:
            list.append(i)
        average = (sum(list)//len(list))
        return list,average
    def get_attr(self):
        return (self.__name, self.__roll_num, self.__grades)


s1 = student("Alice", 18, [65,85,25,105])
s2 = student("Bob", 17, [78,95,42])

print(s1.get_attr(),s1.gradeaverage())
print(s2.get_attr(),s2.gradeaverage())


class ShoppingCart:
    def __init__(self):
        self.__items = []
    def add_item(self, item_name, price):
        item = (item_name, price)
        self.__items.append(item)
    def remove_item(self, item_name):
        for item in self.__items:
            if item[0] == item_name:
                self.__items.remove(item)
                break
    def calculate_total(self):
        total = []
        for item in self.__items:
            total.append(item[0])
        return len(total)

    def returnitems(self):
        return self.__items

# cart = ShoppingCart()
#
# cart.add_item("ham", 40)
# cart.add_item("spam", 20)
# cart.add_item("cheese", 15)
# cart.remove_item("spam")
#
# print(cart.calculate_total())


class product:
    def __init__(self):
        self.__items = []
    def add_item(self, item_name, qtt,id):
        item = (item_name, qtt,id)
        self.__items.append(item)

    def remove_item(self, item_name):
        for item in self.__items:
            if item == item_name:
                self.__items.remove(item)
                break
    def calculate_total(self,item_name):
        for item in self.__items:
            if item[0] == item_name:
                return item[1]
    def remove_it_count(self,item_name,quantity):
        for item in self.__items:
            if item[0] == item_name:
                item=(item[0],item[1]-quantity,item[2])
                return item
    def add_it_count(self,item_name,quantity):
        for item in self.__items:
            if item[0] == item_name:
                item=(item[0],item[1]+quantity,item[2])
                return item
    def returnitems(self):
        return self.__items

produce = product()

# Add items to the shopping cart
produce.add_item("orange", 100,1)
produce.add_item("apple", 200,2)
produce.add_item("pear", 150,3)

# print(produce.returnitems())
# print(produce.calculate_total("apple"))
# print(produce.remove_it_count('orange',25))
# print(produce.add_it_count("apple",50))