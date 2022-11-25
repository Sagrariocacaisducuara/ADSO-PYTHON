num=int(input('ingrese un  numero: '))
for x in range(1,num+1):
    if num % x == 0:
        print(x)
        print(x,'es divisor de', num)

