import math
x1 = float(input("Enter the x value of the first line"))
y1 = float(input("Enter the y value of the first line"))
x2 = float(input("Enter the x value of the second line"))
y2 = float(input("Enter the y value of the second line"))

subx = x2 - x1
suby = y2 - y1
subx **= 2
suby **= 2
total = suby + subx
result = math.sqrt(total)
print("distance: "  , result)

