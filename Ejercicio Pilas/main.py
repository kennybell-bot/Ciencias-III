def esta_equilibrado(cadena: str) -> bool:
    """
    Verifica si los símbolos en la cadena están equilibrados.

    Args:
    cadena (str): La cadena de caracteres que contiene los símbolos a verificar.

    Returns:
    bool: True si los símbolos están equilibrados, False en caso contrario.
    """
    # Mapa de símbolos de apertura a cierre
    pares = {'(': ')', '{': '}', '[': ']'}

    # Pila para almacenar los símbolos de apertura
    pila = []

    # Recorrer cada caracter en la cadena
    for caracter in cadena:
        if caracter in pares:
            # Si es un símbolo de apertura, lo añadimos a la pila
            pila.append(caracter)
        elif caracter in pares.values():
            # Si es un símbolo de cierre
            if not pila:
                # Si la pila está vacía, no hay símbolo de apertura correspondiente
                return False
            cima = pila.pop()
            if pares[cima] != caracter:
                # Si la cima de la pila no coincide con el símbolo de cierre, error
                return False

    # Si al final la pila no está vacía, hay un error
    return len(pila) == 0


def menu():
    """
    Muestra un menú para que el usuario pueda verificar si las cadenas están equilibradas.
    """
    while True:
        print("\n--- Verificador de Equilibrado de Símbolos ---")
        cadena = input("Ingrese una cadena de símbolos para verificar (o 'salir' para terminar): ")

        if cadena.lower() == 'salir':
            print("Saliendo del programa...")
            break

        if esta_equilibrado(cadena):
            print(f"La cadena '{cadena}' está equilibrada.")
        else:
            print(f"La cadena '{cadena}' NO está equilibrada.")

        continuar = input("¿Desea verificar otra cadena? (s/n): ")
        if continuar.lower() != 's':
            print("Saliendo del programa...")
            break


# Ejecución del menú
menu()
