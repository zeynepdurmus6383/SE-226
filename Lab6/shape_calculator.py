import geometry_utils

calculatorDict = {'circle': 0,'rectangle': 0,'triangle': 0}
while(True):
    print("Enter Exit to exit")
    shape = input("Enter the shape:")
    if shape == "Exit":
        break
    if shape == 'circle':
        radius = int(input("Enter radius:"))
        calculatorDict[shape] = geometry_utils.circle_area(radius)
    elif shape == 'rectangle':
        width = int(input("Enter width:"))
        rectangleHight = int(input("Enter height: "))
        calculatorDict[shape] = geometry_utils.rectangle_area(width, rectangleHight)
    elif shape == 'triangle':
        base = int(input("Enter base: "))
        triangleHight = int(input("Enter height: "))
        calculatorDict[shape] = geometry_utils.triangle_area(base, triangleHight)
    else:
        print("Invalid input")
        continue
    print("Area:", calculatorDict[shape])
