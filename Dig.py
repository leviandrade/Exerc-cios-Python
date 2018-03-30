#digito mais a esquerda com função recursiva
def dig(n):
    if n<10:
        return n
    else:
        return dig(n//10)
n=float(input('n'))
print(dig(n))
