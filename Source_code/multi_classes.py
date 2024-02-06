class Shape:
    def __init__(self):
        print("Parent  class constructor")
    def area(self):
        print("Area of Shape by default is: ", 0)

class Square(Shape):

    def __init__(self, length):
        Shape.__init__(self)
        self.length = length

    def area(self):
        print("Area of a Square is: ", self.length-2)

obj_square = Square(16)
obj_square.area()
obj_shape = Shape()
obj_shape.area()