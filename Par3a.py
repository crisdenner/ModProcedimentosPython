cont:int =0
fat:int =0

def fatorial(f,c):
    while c!=0:
        f=f*c
        c=c-1
    return f

def main():
    fat=int(input('Insira o valor a ser fatorado: ' ))
    cont= fat-1
    total = fatorial(fat,cont)
    print(f"O fatorial de {fat}! = {total}")
if __name__ =="__main__":
    main()