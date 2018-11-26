from math import sin, cos, pi
x = pi/4.0                          #type casting float with floats
#val = sin**2(x) + cos**2(x)        #can't work like this 
print(x)
val = sin(float(x))**2 + cos(float(x))**2   #math equivalence 
print (val)