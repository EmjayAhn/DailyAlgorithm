import sys
import math

R = int(sys.stdin.readline())

#euclide
S_eu = (R**2)*math.pi
S_eu = round(S_eu,6)


#Taxi
S_taxi = 2*(R**2)

print(S_eu)
print(S_taxi)
