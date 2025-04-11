def verificar_primos(lista:list)->list:
    primos:list = lista.copy()
    for i in lista:
        if int(i)==1 or int(i)==2 or int(i)==3: continue
        for n in range(2,(int(i)//2)+1):
            if int(i)%n == 0:
                primos.remove(i)
                break
    return primos

if __name__ == "__main__":
    numeros = input("Ingrese los números que desea verificar separados por espacios: ").split(",")
    print(verificar_primos(numeros))