def par(n):
    if n%2==0:
        return True
    else:
        return False
n=int(input('n'))
if par(n):
    print('é par')
else:
    print('não é par')
