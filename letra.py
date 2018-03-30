#Usuário digita letras,caso a letra seguinte venha antes da ultima o programa encerra e mostra a quantidade de letras em sequencia q foram digitadas
cont=0
a=str(input('primeira letra Maiuscula'))
while True:
    cont=cont+1
    n=str(input('próxima letra Maiuscula'))
    if n>a:
        a=n
    else:
        print(cont)
        break
    
