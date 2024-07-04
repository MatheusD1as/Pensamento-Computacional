
def gerar_intervalo(n,i):
    if n < 0 or i<0:
        return None
    vet = []
    for v in range(0,n+1,i):
        vet.append(v)
    return vet
def main():
    n = int(input("n:"))
    i = int(input("i:"))
    vet = gerar_intervalo(n,i)
    print(vet)
main()
