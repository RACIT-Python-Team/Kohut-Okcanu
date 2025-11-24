a=int(input("Ведіть число від 0 до 10: "))

if 0<a<=10:
    print()

else:
    print("Число не підходить")
    exit()

b=int(input("Ведіть задумане число:"))

if a==b:
    print("Ти вгадав")

else:
    print("Ти не вгадав спробуй ще раз")
    print(a)