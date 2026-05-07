from typing import List, Optional, Union

class Circle:
    """
    A class representing a circle.
    
    Class Attributes:
        pi (float): The value of pi (3.1415).
        all_circles (List[Circle]): A list of all created Circle instances.
    
    Instance Attributes:
        radius (float): The radius of the circle.
    """
    
    pi: float = 3.1415
    all_circles: List['Circle'] = []
    
    def __init__(self, radius: float = 1) -> None:
        """
        Initialize a new Circle instance.
        
        Args:
            radius (float, optional): The radius of the circle. Defaults to 1.
        """
        self.radius: float = radius
        Circle.all_circles.append(self)
    
    def area(self) -> float:
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (π * r²).
        """
        return Circle.pi * self.radius ** 2
    
    def __str__(self) -> str:
        """
        Return string representation of the circle's radius.
        
        Returns:
            str: The radius as a string.
        """
        return str(self.radius)
    
    @staticmethod
    def total_area() -> float:
        """
        Calculate the total area of all created circles.
        
        Returns:
            float: The sum of areas of all circles.
        """
        total: float = 0
        for circle in Circle.all_circles:
            total += circle.area()
        return total


c1 = Circle()
c2 = Circle(7)
c3 = Circle(5)
print(c2.area())
print(c3)
print(Circle.pi)
print(Circle.all_circles)
print(Circle.total_area())
print(len(c3.__class__.all_circles))
