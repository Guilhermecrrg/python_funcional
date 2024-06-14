from functools import reduce 

entrada = lambda: (input().split())  
caixa_alta = lambda l: list(x.upper() for x in l)
maior_palavra = lambda s1, s2: s1 if len(s1)>len(s2) else s2
maior = lambda l: reduce(maior_palavra, l)
saida = lambda l: f"Palavra em caixa alta = {caixa_alta(l)}\nMaior palavra = {maior(l)}"

print(saida(entrada()))