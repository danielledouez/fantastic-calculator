import areaCalc 
import perimCalc 
import numpy as np

a=5
area=areaCalc.square(a)
perimeter=perimCalc.square(a)
print('For a square of length %d, the area is %d and the perimeter %d'
%(a,area,perimeter))

r=5
area=areaCalc.circle(r)
perimeter=perimCalc.circle(r)
print('For a circle of radius %d, the area is %d and the perimeter %d'
%(r,area,perimeter))
