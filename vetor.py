def soma_vetor(a,b,c,tam):
    for i in range(tam):
        c[i]= a[i]+b[i]
    return c
tam=int(input('n'))
a=[0]*tam
b=[0]*tam
c=[0]*tam

for i in range(tam):
    a[i]=int(input('a'))
    b[i]=int(input('b'))
print(soma_vetor(a,b,c,tam))
