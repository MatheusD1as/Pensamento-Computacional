    def trocar_elementos(l1):
   l2 = []
   for i in range(len(l1)-1,-1,-1):
       l2.append(l1[i])
   return l2

def main():
    l1 = [1, 2, 3, 4, 5]
    l2 = trocar_elementos(l1)
    print("Vetor trocado =", l2)
main()
