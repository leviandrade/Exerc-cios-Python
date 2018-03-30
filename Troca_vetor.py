#troca os valores positivos por 1 e negativos por 0


def troca(vet):
    for i in range(3):
        if vet[i] &gt;= 0:
            vet[i] = 1
        else:
            vet[i] = 0
    return vet

vet = [0]*3
for i in range(3):
    vet[i] = input('Digite um valor: ')
print vet
troca(vet)
print vet
