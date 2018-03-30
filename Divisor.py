#divisão sem o operador
def divisao(a,b):
    resu=0
    while a>=b:
        a=a-b
        resu=resu+1
    
   
    return(resu)
    
numerador=int(input('digite um numerador : '))
denominador=int(input('digite um denominador : '))
    
print(divisao(numerador,denominador))
