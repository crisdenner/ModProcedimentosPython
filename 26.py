n1:int=0
n2:int=0
total:int=0
maior:int=0
menor:int=0

def mult_ma_mn():
    global n1,n2,total,maior,menor
    n1=int(input('Insira o primeiro valor:'))
    n2=int(input('Insira o segundo valor:'))

    if(n1>n2):
        maior=n1
        menor=n2
    else:
        maior=n2
        menor=n1
    total=maior%menor

    if(total!=0):
        print('O valor',maior,'Não e multiplo de ',menor)     
    else:
        print('O valor',maior,'É multiplo de ',menor)    
def main():
    print(">>>Inicio")
    mult_ma_mn()
    print(">>>Fim")
if __name__ == "__main__":
    main()



