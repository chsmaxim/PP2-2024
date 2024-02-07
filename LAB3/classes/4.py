import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def show(self):
        print(f"coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"new coordinates: ({self.x}, {self.y})")

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance


point1 = Point(17, 1)
point2 = Point(0, 4)

point1.show()
point2.show()

distance_between_points = point1.dist(point2)
print(f"distance: {distance_between_points}")

point1.move(0, 0)
point1.show()
