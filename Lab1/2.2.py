import math


a = 0.7
b = 0.05
x = 0.5


R = (x**2 * (x + 1)) / b - math.sin(x + a)**2
s = math.sqrt((x * b) / a + math.cos(x + b)**2)**3


print("R =", R)
print("s =", s)
