import math
a=float(input("Введіть число а:"))

d=float(input("Введіть число d: "))

c=float(input("Введіть число с:"))

if c!=0:
    D=(-c)**2-4*c*(-(6*c+a+d))
if D>0:
    x1=(-(-c)+math.sqrt(D))/(2*c)
    x2=(-(-c)-math.sqrt(D))/(2*c)
    print("x1 =",x1)
    print("x2 =",x2)
elif D==0:
    x=-D/(2*a)
    print("x",x)
elif D==0:
    print("Рівняння не має дійсних розв'язків")
else:
    print("c=0, piвняння вироджується, х не визначено")