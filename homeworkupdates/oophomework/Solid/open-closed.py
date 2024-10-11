class Shape:
    def __init__(self,shape,**kwargs):
        self.shape_type = shape
        if self.shape_type == 'rectangle':
            self.width = kwargs["width"]
            self.height = kwargs['height']
        elif self.shape_type == 'circle':
            self.radius = kwargs['radius']

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return 3.14 * self.radius ** 2

    """this method violates the principle which states that you should extend the code rather than modify it 
    and if we want to add another functionality to this we will have to modify it"""

from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self,shape):
        self.shape_type = shape

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        super().__init__('circle')
        self.radius = radius
    def calculate_area(self):
        return (3.14*(self.radius**2))

class rectangele(Shape):
    def __init__(self,width,height):
        super().__init__('rectangle')
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.height*self.width