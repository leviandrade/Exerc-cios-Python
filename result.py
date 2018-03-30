
def sequ(n):
    aux1 = 2
    aux2 = 3.0
    soma = 0
 
    while aux1 &lt;= num:
        print aux1, aux2
        soma = soma + aux1/aux2
        aux1 = aux1 + 1
        aux2 = aux2 + 2
 
    return soma
 
num = input('Digite um valor: ')
while num &lt; 0:
    num = input('Digite um valor positivo: ')
 
res = sequ(num)
print res
