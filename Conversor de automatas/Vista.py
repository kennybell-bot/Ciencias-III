from tkinter import *
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Controlador import Controlador  # Importar la clase Controlador

class Ventana:
    def __init__(self):
        self.root = Tk()
        self.root.title("Convertidor de automatas")
        self.root.resizable(True, True)
        self.root.geometry("800x600")

        self.figure = plt.Figure(figsize=(5, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.graph = nx.DiGraph()
        self.pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, self.pos, ax=self.ax, with_labels=True, node_color='skyblue', node_size=1000, edge_color='k', font_size=10)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

        self.estados_finales = set()  # Conjunto para almacenar los estados finales
        self.crear_botones()

    def crear_botones(self):
        frame = Frame(self.root)
        frame.pack(side=BOTTOM)

        boton_agregar_nodo = Button(frame, text="Agregar Nodo", command=self.agregar_nodo)
        boton_agregar_nodo.pack(side=LEFT)

        boton_agregar_edge = Button(frame, text="Agregar Edge", command=self.agregar_edge)
        boton_agregar_edge.pack(side=LEFT)

        boton_actualizar = Button(frame, text="Actualizar Automata", command=self.actualizar_grafo)
        boton_actualizar.pack(side=LEFT)

        boton_convertir = Button(frame, text="Convertir Diagrama", command=self.convertir_diagrama)
        boton_convertir.pack(side=LEFT)

        boton_elegir_estados_finales = Button(frame, text="Elegir estados finales", command=self.ventana_elegir_estados_finales)
        boton_elegir_estados_finales.pack(side=LEFT)

        # Campo de texto y botón "Leer expresión"
        self.expresion_entry = Entry(frame)
        self.expresion_entry.pack(side=LEFT)
        boton_leer_expresion = Button(frame, text="Leer expresión", command=self.leer_expresion)
        boton_leer_expresion.pack(side=LEFT)

    def agregar_nodo(self):
        nodo_id = str(len(self.graph.nodes) + 1)
        self.graph.add_node(nodo_id)
        self.actualizar_grafo()

    def agregar_edge(self):
        if len(self.graph.nodes) >= 2:
            self.ventana_emergente()

    def ventana_emergente(self):
        top = Toplevel(self.root)
        top.title("Seleccionar Estados")

        Label(top, text="Estado Origen:").pack()
        nodo_origen = ttk.Combobox(top, values=list(self.graph.nodes))
        nodo_origen.pack()

        Label(top, text="Estado Destino:").pack()
        nodo_destino = ttk.Combobox(top, values=list(self.graph.nodes))
        nodo_destino.pack()

        Label(top, text="Valor:").pack()
        etiqueta = Entry(top)
        etiqueta.pack()

        Button(top, text="Agregar", command=lambda: self.confirmar_agregar_edge(top, nodo_origen.get(), nodo_destino.get(), etiqueta.get())).pack()

    def confirmar_agregar_edge(self, top, nodo_origen, nodo_destino, etiqueta):
        if nodo_origen and nodo_destino:
            self.graph.add_edge(nodo_origen, nodo_destino, label=etiqueta)
            self.actualizar_grafo()
        top.destroy()

    def actualizar_grafo(self):
        self.ax.clear()
        self.pos = nx.spring_layout(self.graph)
        
        # Obtener los nodos y asignar colores
        nodes = list(self.graph.nodes)
        node_colors = []
        for i, node in enumerate(nodes):
            if i == 0:
                node_colors.append('red')
                self.graph.nodes[node]['color'] = 'red'
            elif node in self.estados_finales:
                node_colors.append('yellow')
                self.graph.nodes[node]['color'] = 'yellow'
            else:
                node_colors.append('skyblue')
                self.graph.nodes[node]['color'] = 'skyblue'
        
        nx.draw(self.graph, self.pos, ax=self.ax, with_labels=True, node_color=node_colors, node_size=1000, edge_color='k', font_size=10)
        edge_labels = nx.get_edge_attributes(self.graph, 'label')
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=edge_labels, ax=self.ax, font_size=8)
        self.canvas.draw()

    def convertir_diagrama(self):
        controlador = Controlador()
        controlador.adaptar_diagrama(self.graph)

    def ventana_elegir_estados_finales(self):
        top = Toplevel(self.root)
        top.title("Elegir Estados Finales")

        # Obtener los nodos que no son de color rojo
        nodes = list(self.graph.nodes)
        non_red_nodes = [nodes[i] for i in range(1, len(nodes))]

        Label(top, text="Seleccionar Estado Final:").pack()
        estado_final = ttk.Combobox(top, values=non_red_nodes)
        estado_final.pack()

        Button(top, text="Agregar", command=lambda: self.agregar_estado_final(estado_final.get(), top)).pack()

    def agregar_estado_final(self, estado_final, top):
        if estado_final:
            self.estados_finales.add(estado_final)
            self.actualizar_grafo()
        top.destroy()

    def leer_expresion(self):
        expresion = self.expresion_entry.get()
        print(f"Expresión leída: {expresion}")

    def getDiagrama(self):
        return self.graph

    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    ventana = Ventana()
    ventana.iniciar()