from functools import reduce 

soma = lambda x,y: x + y
ehPos = lambda x: True if (x>0) else False
listaPos = lambda l: list(filter(ehPos, l))
mediares = lambda l: reduce(soma, l) / len(l) 
saida = lambda l : f'{str(len(listaPos(l)))} valores positivos\n{float(mediares(listaPos(l)))}'
print(saida([float(input()) for _ in range(0,6)]))