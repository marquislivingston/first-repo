import math

a = int(input("input a side of a right triangle: "))
b = int(input("input the second side of a right triangle: "))
c = math.sqrt((a*a)+(b*b))
print(f"hypotenuse: {c}")
