a=int(input("Ведіть перше число:"))
n=int(input("Ведіть кількість чисел:"))
s=0

for i in range(n):
    x=a+5*i
    s=x+s
    print(s)