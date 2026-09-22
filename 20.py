#Declarar
a: int = 0
b: int = 0
c: int = 0
delta: int= 0
x1: int = 0
x2: int = 0

def calculo_equ_2grau():
    global a,b,c,delta,x1,x2
    a = int(input('Insira o valor de A:'))
    b = int(input('Insira o valor de B:'))
    c = int(input('Insira o valor de C:'))

    delta = (b ** 2) - (4*a*c)
    if (delta<0):
        print("Não existem raízes reais")
    else:    
        x1 = (-b -(delta ** 0.5)) / (2 * a)
        x2 = (-b +(delta ** 0.5)) / (2 * a)
        print("As raizes são: ",x1, ' e ',x2)

def main():
    print(">>>Inicio")
    calculo_equ_2grau()
    print(">>>Fim")
if __name__ == '__main__':
    main()

 