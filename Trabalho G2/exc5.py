def trocar_elementos(l1):
   for i in range(0,len(l1)//2):
     j = len(l1) -i - 1
     l1[i],l1[j]=l1[j],l1[i]
   return l1

def main():
    l1 = [1, 2, 3, 4, 5]
    l2 = trocar_elementos(l1)
    print("Vetor trocado =", l2)
main()
