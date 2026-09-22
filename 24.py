n1:int=0
total:int=0

def mult2e3():
    global n1

    n1=int(input('Insira o valor:'))

    if(n1%2 !=0 and n1%3 !=0):
        print('Numero nao divisivel por 2 e 3')
    elif(n1%2 !=0 and n1%3 ==0):
        print('Numero nao divisivel por 2 mas divisivel 3')
    elif(n1%2 ==0 and n1%3 !=0):
        print('Numero nao divisivel por 3 mas divisivel 2')
    else:   
        print('Numero divisivel por 2 e 3')
def main():
    print(">>>Inicio")
    mult2e3()
    print(">>>Fim")
if __name__ == "__main__":
    main()