tipo: int = 0
invest: float = 0.0


def calc_invest(t,inv):
    if(t==1):
        inv=inv+(inv*0.03)
        print('O valor corrigido com rendimento de 30 dias na sua Conta Poupança é:',inv)
    elif(t==2):
        inv=inv+(inv*0.05)
        print('O valor corrigido com rendimento de 30 dias na sua Conta Renda Fixa é:',inv)
    else:
        print('Tipo de conta Inválido')

def main():
    print(">>>Inicio")
    tipo= int(input('Insira o tipo de conta(sendo 1 Conta Poupança. 2 Renda Fixa): '))
    invest= float(input('Insira o valor investido: '))
    calc_invest(tipo,invest)
    print(">>>Fim")
if __name__=="__main__":
    main()