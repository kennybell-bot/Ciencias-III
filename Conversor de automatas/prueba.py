import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from automata_io import read_automaton_from_json

class AutomataVisualizer:
    def __init__(self, root, automaton_data):
        self.root = root
        self.root.title("Automata Visualizer")
        
        # Crear una figura de Matplotlib
        self.figure = plt.Figure(figsize=(5, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        
        # Crear un gráfico de NetworkX
        self.graph = nx.DiGraph()
        self.edge_labels = {}  # Diccionario para almacenar las etiquetas de las aristas
        self._build_graph(automaton_data)
        
        # Dibujar el gráfico de NetworkX en el eje de Matplotlib
        pos = nx.spring_layout(self.graph)
        nx.draw(
            self.graph, pos, ax=self.ax, with_labels=True, 
            node_color='skyblue', node_size=2000, edge_color='k', font_size=16
        )
        
        # Dibujar las etiquetas de las aristas
        nx.draw_networkx_edge_labels(
            self.graph, pos, edge_labels=self.edge_labels, ax=self.ax, font_size=10
        )
        
        # Integrar la figura de Matplotlib con Tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    def _build_graph(self, automaton_data):
        """
        Construye el grafo de NetworkX a partir de los datos del autómata.

        Args:
            automaton_data (dict): Datos del autómata.
        """
        for state, transitions in automaton_data["transitions"].items():
            for symbol, destinations in transitions.items():
                for destination in destinations:
                    self.graph.add_edge(state, destination)
                    # Guardar la etiqueta para cada arista
                    self.edge_labels[(state, destination)] = symbol

if __name__ == "__main__":
    # Leer datos del autómata desde JSON
    automaton_file = "automata.json"
    automaton_data = read_automaton_from_json(automaton_file)

    # Inicializar la aplicación
    root = tk.Tk()
    app = AutomataVisualizer(root, automaton_data)
    root.mainloop()
