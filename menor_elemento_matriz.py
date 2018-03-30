#Mostra a matriz e o menor elemento dela
def minimo(a,m,n):
    menor=a[0][0]
    for i in range(m):
        for j in range(n-1):

            if a[i][j+1]<menor:
                menor=a[i][j]
        return menor

def exibematris(a,m,n):
    for i in range(m):
        print("")
        for j in range(n):
            print("%d"%a[i][j],end="")

def lematris(a,m,n):
    for i in range(m):
        for j in range(n):
            a[i][j]=int(input("insira elemento [%d][%d] da matriz"%(j+1,j+1)))

m=int(input("linhas"))
n=int(input("colunas"))

a=[[0 for j in range(n)]for i in range(m)]
lematris(a,m,n)
exibematris(a,m,n)
print("\n_________\n")
print(minimo(a,m,n))
