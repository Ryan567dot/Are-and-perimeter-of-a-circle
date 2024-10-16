class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
 
i = int(input("Enter radius of circle: "))

object =circle(i)

print("Area of circle:",round(object.area(),2))
print("Perimeter of circle:",round(object.perimeter(),2))
