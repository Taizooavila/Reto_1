def mayor_suma(lista:list):

    num1:int = 0
    num2:int = 0
    sumamax:int = 0

    for element in lista:
        num2 = int(element)
        if (num1+num2)>sumamax:
            sumamax = num1+num2
        num1 = int(element)

    return sumamax

if __name__ == "__main__":

    listastr:str = input("Ingrese los números de la lista separados por espacio: ")
    lista:list = listastr.split()
    print(f"Lista: {lista}\nLa mayor suma entre numeros consecutivos de tu lista es: {mayor_suma(lista)}")