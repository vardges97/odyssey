class FoodProcessor:

    def chop(self, item):
        print(f"chopping the {item}")
    def mince(self, item):
        print(f"Minicing the {item}")


class Mincer(FoodProcessor):

    def chop(self, item):
        raise NotImplementedError
    def mince(self, item):
        super().mince(item)

"""this violates the liskov priciple because if we use both and try to use chop 
the mincer will throw an exception"""

from abc import ABC,abstractmethod
class IMince(ABC):

    @abstractmethod
    def mince(self, item):
        raise NotImplementedError
class IChopper(ABC):

    @abstractmethod
    def chop(self, item):
        raise NotImplementedError

class FoodProcessor(IMince, IChopper):

    def chop(self, item):
        print(f"chopping the {item}")

    def mince(self, item):
        print(f"Minicing the {item}")

"""thi way we follow the liskov principle which states that the child class 
can replace the parent class without breaking the code"""
