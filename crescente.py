#Função que verifica se o número é crescente ou não
def nao_decrescente(n):
    i=0
    while n!=0:
        i=n%10
        n=n//10
        if i<n%10 and n!=0:
            return False
    return True
n=int(input('n'))
j=nao_decrescente(n)
if j==True:
    print('não decrescente')
else:
    print('decrescente')
