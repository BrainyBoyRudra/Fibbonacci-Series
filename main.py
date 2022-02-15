def fib(n):
    number = [0,1]

    for i in range (2,n) :
        a=number[len(number)-1]
        b=number[len(number)-2]
 
        c = a+b
        number.append(c)
    for i in (number) :
        print(i)
fib(100)