def sequencial(l,x):
    achou = False 
    i = 0
    while i < len(l) and not achou:
        if(l[i] == x):
            achou = True
            pos = i
        else:
            i += 1
    return pos
def binaria(l, x, ini, fim):
    if ini > fim:
        return -1
    meio = ini + (fim - ini) // 2
    if l[meio] == x:
        return meio
    elif l[meio] > x:
        return binaria(l, x, ini, meio - 1)
    else:
        return binaria(l, x, meio + 1, fim)

def main():
    l = [1,2,3,4,5,6,7,8]
    x = int(input("Digite um número que quer procurar entre 1 e 8:"))
    while x < 1 or x > 8:
        x = int(input("Digite novamente o número precisa estar entre 1 e 8:"))
    pos = sequencial(l,x)
    print("O número",x,"se encontra na posição",pos)
    l.sort
    pos_bin = binaria(l, x, 0, len(l) - 1)
    if pos_bin != -1:
         print("O número",x,"se encontra na posição",pos)
main()
