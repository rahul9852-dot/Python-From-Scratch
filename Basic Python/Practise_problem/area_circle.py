'''Area of a circle can simply be evaluated using following formula.
Area = pi * r2
where r is radius of circle 
'''
from math import pi
def calc_area_of_circle(r):
    area=pi*(r**2)
    return area
print(calc_area_of_circle(5))
