
def Operaciones (num1, num2, operador):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    else:
        return num1 / num2

if __name__ == "__main__":
    
    num1: float = float(input("Ingrese el primer número: "))
    num2: float = float(input("Ingrese el segundo número: "))
    operador: str = input("Ingrese el símbolo de la operación que quiere realizar (+, -, *, /)")
    lista_operadores = ("+", "-", "*", "/")
    while operador not in lista_operadores:
        operador = input("inserte un operador válido (+, -, *, /)")
    print(Operaciones(num1, num2, operador))