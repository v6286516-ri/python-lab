import math
radius=float(input("enter the radius of the circle:"))
area=math.pi*radius**2
circumference=2*math.pi*radius
areainteger=int(area)
print(f"Area:{area:.2f}")
print(f"circumference:{circumference:.2f}")
print(f"area as integer:{areainteger}")