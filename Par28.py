preco:float = 0.0
vendas:int = 0

def checa_preco(v,p):
    if(v<500 and p<30.0):
        p=p+(p*0.1)
        print('Novo preço é: ',p)
    elif(v>=500 and v<1000 and p>=30.0 and p<80.0):
        p=p+(p*0.15)
        print('Novo preço é: ',p)
    elif(v>=1000 and p>=80.0):
        p=p-(p*0.05)
        print('Novo preço é: ',p)
    else:
        print('O preço deve se manter igual')
def main():
    print(">>>Inicio")
    preco=float(input("Insira preço atual do produto: "))
    vendas=int(input("Insira as vendas mensais do produto "))

    checa_preco(vendas,preco)
    print(">>>Fim")
if __name__=="__main__":
    main()