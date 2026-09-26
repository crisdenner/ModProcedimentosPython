
def fatorial(numero):
    fat: int =1
    if numero == 1 or numero<1:
        return 1
    for i in range(1, numero+1):
        fat *= i
    return fat

def divisao(valordiv1,valordiv2):
    return valordiv1/valordiv2

def main():
    i: int = 0
    v2: int = 0
    v1: int = 0

    v1=int(input('Insira o valor 1: ' ))
    v2=int(input('Insira o valor 2: ' ))
    n=int(input("Insira o valor de N: "))
    soma:int = 1
  
    while v2<=n:

        print(f"{v1}/{v2}! + ", end="")
        fatatual = fatorial(v2)
        totaldiv = divisao(v1,fatatual)
        soma = soma + totaldiv
        v2+=1    
    
    print(f" = {soma}")
if __name__ =="__main__":
    main()