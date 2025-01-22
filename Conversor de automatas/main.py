import json
import os
from automaton_model import AFNLambdaAutomaton, AFNAutomaton, AFDAutomaton
from automaton_transformations import convert_afn_lambda_to_afn, convert_afn_to_afd
from automaton_visualization import draw_automaton

def load_automaton_from_json(file_path, automaton_type):
    """
    Carga un autómata desde un archivo JSON.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    if automaton_type == "AFN-λ":
        return AFNLambdaAutomaton(**data)
    elif automaton_type == "AFN":
        return AFNAutomaton(**data)
    elif automaton_type == "AFD":
        return AFDAutomaton(**data)
    else:
        raise ValueError("Tipo de autómata desconocido.")

def clear_screen():
    """
    Limpia la pantalla para hacer el menú más legible.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    """
    Muestra el menú principal y permite al usuario interactuar con el programa.
    """
    while True:
        clear_screen()
        print("=" * 40)
        print("          Convertidor de Autómatas")
        print("=" * 40)
        print("Opciones disponibles:")
        print("1. Cargar un archivo JSON (AFN-λ, AFN, AFD)")
        print("2. Salir")
        print("=" * 40)

        choice = input("Seleccione una opción: ")
        if choice == "1":
            handle_file_selection()
        elif choice == "2":
            print("\n¡Gracias por usar el programa!")
            break
        else:
            input("\nOpción inválida. Presione Enter para continuar...")

def handle_file_selection():
    """
    Maneja la selección de archivos JSON y las operaciones correspondientes.
    """
    clear_screen()
    print("=" * 40)
    print("          Selección de Archivo JSON")
    print("=" * 40)
    print("Archivos disponibles:")
    print("1. afnlambda.json (AFN-λ)")
    print("2. afn.json (AFN)")
    print("3. afd.json (AFD)")
    print("4. Volver al menú principal")
    print("=" * 40)

    choice = input("Seleccione un archivo: ")
    file_mapping = {"1": ("afnlambda.json", "AFN-λ"),
                    "2": ("afn.json", "AFN"),
                    "3": ("afd.json", "AFD")}
    
    if choice in file_mapping:
        file_path, automaton_type = file_mapping[choice]
        process_automaton(file_path, automaton_type)
    elif choice == "4":
        return
    else:
        input("\nOpción inválida. Presione Enter para continuar...")

def process_automaton(file_path, automaton_type):
    """
    Procesa el autómata seleccionado y permite realizar conversiones y graficarlo.
    """
    try:
        automaton = load_automaton_from_json(file_path, automaton_type)
        print(f"\nAutómata cargado exitosamente desde {file_path}.")
        draw_automaton(automaton, "origen")
        print("El autómata original ha sido graficado como 'origen.png'.")
        
        if automaton_type == "AFN-λ":
            handle_conversion_afn_lambda(automaton)
        elif automaton_type == "AFN":
            handle_conversion_afn(automaton)
        else:
            input("\nEl AFD no tiene más conversiones posibles. Presione Enter para continuar...")

    except Exception as e:
        input(f"\nError: {e}. Presione Enter para volver al menú...")

def handle_conversion_afn_lambda(automaton):
    """
    Maneja las conversiones desde un AFN-λ.
    """
    while True:
        print("\nOpciones para el AFN-λ:")
        print("1. Convertir a AFN")
        print("2. Volver al menú principal")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            afn = convert_afn_lambda_to_afn(automaton)
            draw_automaton(afn, "convertido")
            print("El autómata convertido a AFN ha sido graficado como 'convertido.png'.")
            handle_conversion_afn(afn)
            break
        elif choice == "2":
            return
        else:
            print("\nOpción inválida.")

def handle_conversion_afn(automaton):
    """
    Maneja las conversiones desde un AFN.
    """
    while True:
        print("\nOpciones para el AFN:")
        print("1. Convertir a AFD")
        print("2. Volver al menú principal")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            afd = convert_afn_to_afd(automaton)
            draw_automaton(afd, "convertido")
            print("El autómata convertido a AFD ha sido graficado como 'convertido.png'.")
            break
        elif choice == "2":
            return
        else:
            print("\nOpción inválida.")

if __name__ == "__main__":
    main_menu()
