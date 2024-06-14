entrada = lambda x: lista([int(e) for e in input().split()]) (entrada(x-1)) if (x>0) else x
lista = lambda l: divisao(l)
divisao = lambda l: saida(l[0] / l[1]) if (l[1]!=0) else saida('divisao impossivel')
saida = lambda x: print(f"{x}\n")  

entrada(int(input())) 