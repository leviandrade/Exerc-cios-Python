#zera os elementos com indice para em um vetor
def zera_ind_par(a,tam):
    for i in range (tam):
        if (i%2)==0 and i!=0:
            a[i]=0
tam=int(input("digite o tamanho do vetor"))
a=[0]*tam
for i in range(tam):
    a[i]=int(input("digite um valor"))
print(a)
zera_ind_par(a,tam)
print(a)
