def pot(a , b):
    cont=0
    c=1
    while cont<b:
        cont=cont+1
        c=c*a
    return c
a=int(input('n'))
b=int(input('n'))
m=  pot(a , b)
print (m)
