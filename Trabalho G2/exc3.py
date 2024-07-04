def filtra_num(l1):
    l2 = []
    for i in range(0,len(l1)):
        n1 = l1[i] //100
        n2 = l1[i] % 100
        n3 = n1 + n2
        if n3**2 == l1[i]:
            l2.append(l1[i])
    return l2
def main():
    l1 = [3025,2025,1843,7243] 
    lista_nova = filtra_num(l1)    
    print(lista_nova)
main()
