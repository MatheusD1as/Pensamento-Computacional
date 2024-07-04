def calcula_h(n):
    h = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            h -= 1 / i
        else:
            h += 1 / i
    return h

def main():
    n = int(input("Digite o valor de N: "))
    h = calcula_h(n)
    print("O valor de é:",h)
