def mismos_char(lista:list):

    lista_anagramas = []
    copia_lista = lista.copy()

    for i in range(len(lista)):

        for e in range(len(lista)):

            if i==e or len(lista[i])!=len(lista[e]): continue

            for c in lista[i]:
                if c in copia_lista[e]:
                    copia_lista[e] = lista[e].replace(c, "", 1)
                    anagrama = True
                else:
                    anagrama = False
                    break

            if anagrama==True:
                lista_anagramas += [lista[i], lista[e]]
    
    lista_anagramas = list(set(lista_anagramas))
    return lista_anagramas

if __name__ == "__main__":
    lista=input("Ingrese las palabras separadas por espacios: ").split()
    print(mismos_char(lista))