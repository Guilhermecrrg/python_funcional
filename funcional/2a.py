entrada = lambda : [int(num) for num in input().split()]
ehPar = lambda x : True if x % 2 == 0 else False
ehImpar = lambda x : not ehPar(x)
lista_pares = lambda l : list(filter(ehPar, l))
lista_impares = lambda l : list(filter(ehImpar, l))
saida = lambda l: f"Lista de pares = {lista_pares(l)}\n" f'Lista de impares = {lista_impares(l)}'

print(saida(entrada()))