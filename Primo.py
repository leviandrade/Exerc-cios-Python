#Número primo ou não
def primo(n):
    cont=0
    b=0
    while n>=cont:
        cont=cont+1
        c=n%cont
        if c==0:
            b=b+1
    if b==2:
        print('primo')
    else:
        print('não primo')    
n=int(input('n'))
primo(n)
        
