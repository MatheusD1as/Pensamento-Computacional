def imparOuPar(n,c):
    vetPar = []
    if c == "i":
        for i in range(1,n,2):
            vetPar.append(i)
        return vetPar
    elif c == "p":
def main():
    n = int(input("i:"))
    c = input("p | i:").lower()
    imparOuPar(n,c)
