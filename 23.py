n1: int=0
n2: int=0
n3: int=0
n4: int=0

def ordem_crescente():
    global n1,n2,n3,n4
    if(n4>n1 and n4<n2):
        print('ordem crescente:',n1,n4,n2,n3)
    elif(n4>n2 and n4<n3):
        print('ordem crescente:',n1,n2,n4,n3)
    elif(n4>n3):
        print('ordem crescente:',n1,n2,n3,n4)
    else:
        print('ordem crescente:',n4,n1,n2,n3)

def main():
    print(">>>Inicio")
    global n1,n2,n3,n4

    n1=int(input('Insira numero valor 1 em ordem crescente:'))

    n2=int(input('Insira numero valor 2 em ordem crescente:'))

    n3=int(input('Insira numero valor 3 em ordem crescente:'))

    n4=int(input('insira valor 4 não necessariamente na ordem:'))

    ordem_crescente()
    print(">>>Fim")
if __name__ == '__main__':
    main()


