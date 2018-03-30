#Numero em binário
def binario(n):
    d=1
    c=0
    while n!=0:
        c=c+((n%2)*d)
        n=n//2
        d=d*10
    print(c)
n=int(input('n: '))
binario(n)
