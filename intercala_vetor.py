def intercala(a,b,c,m,n):
    mule=[]
    k=0
    if m<=n:
        for i in range (m):
            mule.append(a[i])
            mule.append(b[i])
        for i in range(m,n,1):
            mule.append(b[i])
        
    else:
        for i in range (n):
            mule.append(a[i])
            mule.append(b[i])
     
        for i in range(n,m,1):
            mule.append(a[i])
  
    for i in mule:
        if i not in c:
            c.append(i)
            k=k+1
    return k 
tam1=int(input('digite tamanho do vetor:'))
tam2=int(input('digite tamanho do vetor:'))
a=[]
b=[]
c=[]

for i in range(tam1):
    a.append(int(input('digite valor do vetor 1:')))
for i in range(tam2):
    b.append(int(input('digite valor do vetor 2:')))
print(a)
print(b)
a.sort()
b.sort()
print (a)
print (b)
intercala(a,b,c,tam1,tam2)
print(c)


