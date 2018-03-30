#verifica se um número é perfeito,ou seja se o número é formado pela soma de seus divisores
def numeroperfeito(n):
    cont=1
    soma=0
    while cont<n:
        if n%cont==0:
            soma=soma+cont
            cont=cont+1
        else:
            cont=cont+1
    if soma==n:
        print('numero perfeito')
    else:
        print('não')
n=int(input('n'))
numeroperfeito(n)
