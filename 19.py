n1: float = 0.0
n2: float = 0.0

def maior_real():
    global n1, n2
    n1= float(input('Insira o numero real 1: '))
    n2= float(input('Insira o numero real 2: '))

    if (n1>n2):
        print('O maior valor é:', n1)
    else:
        print('O maior valor é:', n2)
def main():
    print(">>>Inicio")
    maior_real()
    print(">>>Fim")

if __name__ == '__main__':
    main()


