voltas:int = 0
metros:int = 0
minutos:int = 0


def media_velocidade(vol,mt,min):
    kms: int = 0
    horas: int = 0
    kmh: int = 0

    kms = (vol*mt)/1000
    horas = (min/60)
    kmh = kms/horas
    print(f"A media de velocidade foi: {kmh}")

def main():
    print(">>>Inicio")
    voltas = int(input("Insira a  quantidade de voltas: "))

    metros = int(input("Insira qual o tamanho do circuito em metros: "))

    minutos = int(input("Insira o tempo feito em minutos: "))

    media_velocidade(voltas,metros,minutos)
    print(">>>Fim")
if __name__ == "__main__":
    main()
    
