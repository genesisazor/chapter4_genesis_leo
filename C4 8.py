import math
def area_of_circle(r):
    a=math.pi*r**2
    return a

radius = float(input("What's the radius?"))
print("The area of the circle is ", area_of_circle(radius))
print(math.pi)

