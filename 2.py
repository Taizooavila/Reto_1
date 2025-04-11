def verificación_palindromo(palabra:str)->None:
    n:int = 0
    for i in range(len(palabra)):
        if palabra[i] != palabra[(-(i + 1))]:
            print(f"La palabra {palabra} no es palindroma")
            return None
        n+=1
    if n==len(palabra):
        print(f"La palabra {palabra} es palindroma")

if __name__ == "__main__":
    palabra:str = input("Ingrese la palabra que quiere analizar: ")
    verificación_palindromo(palabra)