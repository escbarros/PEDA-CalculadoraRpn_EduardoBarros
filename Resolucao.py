import re 

def resolvedor(teste):
    while True:
        try:
            procura = re.search("\(([^()]*)\)", teste)
            grupo = procura.group()
            formatado = ''.join(grupo.replace("(", "").replace(")", ""))
            resposta = int(eval(formatado[:-2].replace(" ", f'{formatado[-1]}')))
            teste = list(teste)
            teste[procura.start(): procura.end()] = str(resposta)
            teste = ''.join(teste) 
        except AttributeError:
            resposta = int(eval(teste.replace(" ", f'{teste[-1]}')))
            print(f"\nResposta: {resposta}\n")
            break


teste1 = "(2 3 +)" #Resposta 5
resolvedor(teste1)

teste2 = "(3 4 *)" #Resposta 12
resolvedor(teste2)

teste3 = "(4 2 2 /)" #Resposta 1
resolvedor(teste3)

teste4 = "((4 2 +) 3 *)" #Resposta 18
resolvedor(teste4)

teste5 = "((3 4 +) (4 2 /) *)" #Resposta 14
resolvedor(teste5)

teste6 = "((3 4 +) (4 (1 1 +) /) *)" #Resposta 14
resolvedor(teste6)
