entrada = lambda: [int(n) for n in input().split()]
ehPar = lambda x: True if (x%2==0) else False
listaPar = lambda l: list(filter(ehPar, l))
saida = lambda l: f"lista de numeros pares: {listaPar(l)}\n"
print(saida(entrada()))