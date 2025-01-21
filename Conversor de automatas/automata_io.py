import json

def read_automaton_from_json(file_path: str) -> dict:
    """
    Lee un autómata desde un archivo JSON.

    Args:
        file_path (str): Ruta del archivo JSON.

    Returns:
        dict: Representación del autómata como un diccionario.
    """
    try:
        with open(file_path, 'r') as file:
            automaton = json.load(file)
        return automaton
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo {file_path} no existe.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error al leer el archivo JSON: {e}")

def write_automaton_to_json(file_path: str, automaton: dict):
    """
    Escribe un autómata en un archivo JSON.

    Args:
        file_path (str): Ruta del archivo JSON.
        automaton (dict): Representación del autómata.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(automaton, file, indent=4)
    except Exception as e:
        raise IOError(f"Error al escribir el archivo JSON: {e}")
