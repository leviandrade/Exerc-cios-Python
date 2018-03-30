#Diz se o numero é crescente ou não
def nao_decrescente(n):
    decrescente=False
    while n>10:
        d=n%10
        n=n//10
        c=n%10
        if d>n:
            decrescente= True
            break
    
    return decrescente
n=int(input('n'))
print(nao_decrescente(n))
