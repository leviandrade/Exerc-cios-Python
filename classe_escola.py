class escola:
    def __init__(self,endereco,mensalidade):
        self.a=endereco
        self.b=mensalidade
e1=escola('rua silva',122)
e2=escola('rua jurema',133)
print(e1.a,e1.b)
print(e2.a,e2.b)
novo=str(input('digite novo endereço'))
novo1=int(input('digite nova mensalidade'))
e1=escola(novo,122)
e2=escola('rua jurema',novo1)
print(e1.a,e1.b)
print(e2.a,e2.b)
