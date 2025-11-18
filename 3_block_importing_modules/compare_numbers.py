import math
a=float(input("Введіть перше число: "))
b=float(input("Введіть друге число: "))
if a==b:
    print("True. вони рівні")
else:
    print("False, вони не рівні")

if a!=b:
    print("True, вони не рівні")
else:
    print("False. вони рівні")

if a>b:
    print("True, перше число більше")
else:
    print("False, перше число не більше")

if a<b:
    print("True, друге число більше")
else:
    print("False, друге число не більше")

if a**2>b**2:
    print("True, квадрат першого числа більший")
else:
    print("False. квадрат першого числа не більший")

if a+b>a*b:
    print("True. сума цих чисел більва")
else:
    print("False, сума цих чисел не більва")