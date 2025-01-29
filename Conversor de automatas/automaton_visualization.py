from graphviz import Digraph
from automaton_model import Automaton

def draw_automaton(automaton: Automaton, output_file: str):
    """
    Dibuja un autómata usando Graphviz y lo guarda en un archivo.

    Args:
        automaton (Automaton): El autómata a graficar.
        output_file (str): Ruta del archivo de salida (sin extensión).

    Returns:
        str: Ruta del archivo generado.
    """
    # Crear un nuevo objeto Digraph para cada llamada
    dot = Digraph(format="png")
    dot.attr(rankdir="LR")  # Dirección de izquierda a derecha
    dot.attr(dpi="150")  # Mejor calidad

    # Agregar los nodos
    for state in automaton.states:
        shape = "doublecircle" if state in automaton.final_states else "circle"
        dot.node(state, shape=shape)

    # Agregar las transiciones como aristas
    for state, transitions in automaton.transitions.items():
        for symbol, destinations in transitions.items():
            for destination in destinations:
                dot.edge(state, destination, label=symbol)

    # Agregar el nodo de estado inicial
    dot.node("", shape="none", width="0", height="0", label="")
    dot.edge("", automaton.start_state)  # Conectar al estado inicial
    
    # Generar el grafo
    file_path = dot.render(output_file, cleanup=True)  # Genera la imagen
    print(f"Automata dibujado y guardado en {file_path}")
    return file_path  # Retorna la ruta del archivo generado
