import math
a=float(input("Введіть число 1:"))
b=float(input("Введіть число 2:"))
print("a^b", math.pow(a, b))
print("b^a", math.pow(b, a))
print("a^b-1", math.pow(a, b-1))
print("b^a-1", math.pow(b, a-1))
print("(a*b)^a+b=", math.pow(a*b, a+b))