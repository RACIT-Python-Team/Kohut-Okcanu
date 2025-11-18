a=float(input("Введіть число:"))

d=float(input("Введіть число:"))

x=float(input("Введіть число:"))

if a<d<x:
    print(a, "<",d, "<",x)

elif a<x<d:
    print(a,"<",x, "<",d)
elif d<a<x:
    print(d, "<",a,"<",x)
elif d<x<a:
    print(d,"<",x,"<",a)
elif x<a<d:
    print(x,"<",a,"<",d)
else:
    print(x,"<",d,"<",a)