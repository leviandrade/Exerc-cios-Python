def transposta(a,m):
    for i in range(m):
        for j in range(m):
            aux=a[i][j]
            a[i][j]=a[j][i]
            a[j][i]=aux


def exibematriz(a,m):
    for i in range(m):
        print("")
        for j in range(m):
            print("%d"%a[i][j],end="")

def lematriz(a,m):
    for i in range(m):
        for j in range(m):
            a[i][j]=int(input("insira o elemento[%d][%d] da matriz:"%(i+1,j+1)))

m=int(input("digite o numero de linhas e colunas da matriz quadrada:"))
a=[[0 for j in range(m)for i in range(m)]]

lematriz(a,m)
print("\n\n exibição da matriz:")
exibematriz(a,m)
print("\n----------\n")


transposta(a,m)
print("\n\n--------exibição da matriztransposta:")

exibematriz(a,m)
