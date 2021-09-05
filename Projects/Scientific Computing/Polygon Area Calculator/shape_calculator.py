class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def get_picture(self):
        if self.width > 50:
            return 'Too big for picture.'
        else:
            return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, other):
        return (self.width * self.height) // (other.width * other.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_height(self, side):
        self.height = side
        self.width = side
        
    def set_width(self, side):
        self.width = side
        self.height = side
        
    def set_side(self, side):
        self.width = side
        self.height = side
        
    def __str__(self):
        return f'Square(side={self.width})'