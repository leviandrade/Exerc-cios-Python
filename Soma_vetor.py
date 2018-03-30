#Faz um novo vetor com a soma dos outros dois vetores
def soma_vetor(a,b,c,tam):
    for i in range(tam):
        c[i]=a[i]+b[i]
        
tam=int(input("Digite o tamanho dos vetores A e B:  "))
a=[0]*tam
b=[0]*tam
c=[0]*tam

print("\n\n\n-----Leitura do vetor A")
for i in range(tam):
    a[i]=int(input("\nInsira o %dº elemento do vetor A: "%(i+1)))
    
print("\n\n\n-----Leitura do vetor B")
for i in range(tam):
    b[i]=int(input("\nInsira o %dº elemento do vetor B: "%(i+1)))


soma_vetor(a,b,c,tam)

print("\n\n\n")
print("C:",c)
