import areaCalc 
import perimCalc 
import volume
import numpy as np
# Square demo
a=5
area=areaCalc.square(a)
perimeter=perimCalc.square(a)
print('For a square of length %d, the area is %d and the perimeter %d'
%(a,area,perimeter))
#Rectangle demo
r=5
area=areaCalc.circle(r)
perimeter=perimCalc.circle(r)
print('For a circle of radius %d, the area is %d and the perimeter %d'
%(r,area,perimeter))

# Circle demo
a=5
b=8
area=areaCalc.rectangle(a,b)
perimeter=perimCalc.rectangle(a,b)
print('For a rectangle of lengths %d and %d, the area is %d and the perimeter %d'
%(a,b,area,perimeter))

# Volume demo
a=5
b=8
c=3
r=2
cube=volume.cube(a)
sphere=volume.sphere(r)
print('Volume of a cube: %d and a sphere: %d' %(cube,sphere))
