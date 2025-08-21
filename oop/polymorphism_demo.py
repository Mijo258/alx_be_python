import math
class Shape:
    """Base class for all shapes."""
    def area(self):
        """Returns the area of the shape."""
        raise NotImplementedError("Subclasses must implement this method.")
    
class Rectangle(Shape):
    """Class representing a rectangle."""
    def __init__(self, length: float, width: float):
        """Initializes the rectangle with length and width."""
        self.length = length
        self.width = width
    def area(self):
        """Calculates the area of the rectangle."""
        return self.length * self.width
    
class Circle(Shape):
    """Class representing a circle."""  
    def __init__(self, radius: float):
        self.radius = radius    
    def area(self):
        """Calculates the area of the circle."""
        return math.pi * (self.radius ** 2)
    