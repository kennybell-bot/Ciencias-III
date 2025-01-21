import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

class AutomataVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Automata Visualizer")
        
        # Crear una figura de Matplotlib
        self.figure = plt.Figure(figsize=(5, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        
        # Crear un gráfico de NetworkX
        self.graph = nx.DiGraph()  # Puedes usar Graph() para gráficos no dirigidos
        self.graph.add_edge(1, 2, weight=4.7 )  # Ejemplo de aristas
        
        # Dibujar el gráfico de NetworkX en el eje de Matplotlib
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, ax=self.ax, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', font_size=16)
        
        # Integrar la figura de Matplotlib con Tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = AutomataVisualizer(root)
    root.mainloop()
