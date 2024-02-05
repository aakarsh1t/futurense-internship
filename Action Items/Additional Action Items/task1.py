import math
class circle:
    def area(radius):
        c_area = (math.pi)*radius*radius
        return(c_area)
    
radius = float(input("enter radius "))
calculator = circle()
calculated_area = calculator.area
print("radius =",radius," area =",calculated_area)