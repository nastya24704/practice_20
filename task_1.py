class Circle:
    """A circle class that tracks all instances and provides area calculations."""
    
    pi = 3.1415
    all_circles = []

    def __init__(self, radius: float = 1.0) -> None:
        """
        Initialize a circle with given radius.

        Parameters:
            radius: Radius of the circle (default is 1.0)
        """
        self.radius = radius
        Circle.all_circles.append(self)

    def area(self) -> float:
        """
        Calculate area of the circle.

        Returns:
            Area value using pi * radius^2
        """
        return Circle.pi * (self.radius ** 2)

    def __str__(self) -> str:
        """
        Return string representation for printing.

        Returns:
            Radius as a string
        """
        return str(self.radius)

    def __repr__(self) -> str:
        """
        Return unambiguous string representation for debugging.

        Returns:
            Radius as a string for list and console output
        """
        return str(self.radius)

    @staticmethod
    def total_area() -> float:
        """
        Calculate total area of all created circle instances.

        Returns:
            Sum of areas for every circle in all_circles
        """
        total = 0.0
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
