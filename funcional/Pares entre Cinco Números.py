ehPar = lambda x: True if (x % 2)==0  else False
listaPar = lambda l: list(filter(ehPar, l))
print(str(len(listaPar([int(input())for _ in range(0,5)]))) + " valores pares")