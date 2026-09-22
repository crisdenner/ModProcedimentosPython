n1: int = 0
n2: int = 0

def ordem_cresc():
    global n1,n2
    n1= int (input ('Insira primeiro valor:'))
    n2= int (input ('Insira segundo valor:'))

    if(n1>n2):
        print(f'Numeros em ordem crescente:, {n2}, {n1}')
    else:
        print(f'Numeros em ordem crescente: {n1},{n2}')
def main():
    print(">>>Inicio")
    ordem_cresc()
    print(">>>Fim")
if __name__=="__main__":
    main()    


