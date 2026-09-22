Hi: int = 0
Mi: int = 0
Mf: int = 0
Hf: int = 0
Total: int = 0
Horas: int = 0
Minutos : int = 0

def tempo_de_jogo():
    global Hi,Mf,Mi,Hf,Total,Horas,Minutos

    Hi= int (input('Insira hora inicial:'))
    Mi= int (input('Insira minuto inicial:'))
    Hf= int (input('Insira hora final:'))
    Mf= int (input('Insira minuto final:'))

    Total=(Hf*60 + Mf)-(Hi*60+Mi)
    if(Total<0):
        Total=(Total +1440)
    Horas= int(Total/60)
    Minutos= Total-(Horas * 60)
    print('O Jogo durou',Horas,'horas e',Minutos, 'minutos')

def main():
    print(">>>Inicio")
    tempo_de_jogo()
    print(">>>Fim")
if __name__ == "__main__":
    main()
    