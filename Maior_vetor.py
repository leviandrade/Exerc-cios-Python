#Junta dois vetores e mostra o maior elemento
def junta_vetor(a,b,c,tam1,tam2):
    for i in range(tam1):
        c[i]=a[i]
    for i in range(tam2):
        c[i+tam1]=b[i]
    return tam1+tam2
tam1=int(input('digite tamanho do vetor'))
a=[0]*tam1
tam2=int(input('digite tamanho do vetor'))
b=[0]*tam2
j=tam1+tam2
c=[0]*j
for i in range(tam1):
    a[i]=int(input('digite valor do vetor 1'))
for i in range(tam2):
    b[i]=int(input('digite valor do vetor 2'))
print(a)
print(b)
y=junta_vetor(a,b,c,tam1,tam2)
print(c)
print(y)
