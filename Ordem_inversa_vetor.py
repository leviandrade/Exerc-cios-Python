#-Verifica se b tem a ordem inversa de elementos de a O efeito da função é exibir "ordem inversa" ou as posições onde ocorre a primeira diferença.                                    |                                       
def ordem_inversa(a,b,n):
    j=1
    k=False
    for i in range(n):
        if a[i]==b[0-j]:
            k=True

        else:
            print("a[%d]=%d"%(i,a[i]))
            print("b[%d]=%d"%((0-j)*-1,b[0-j]))
            break
        j=j+1
    if k==True:
        print("ordem inversa")

n=int(input("digite quantidade de elementos"))
a=[0]*n
b=[0]*n
for i in range(n):
    a[i]=int(input("valor de a"))
for i in range(n):
    b[i]=int(input("valor de b"))
ordem_inversa(a,b,n)
