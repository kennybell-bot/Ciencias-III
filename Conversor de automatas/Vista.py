from tkinter import *
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Inicializacion de la pantalla
root = Tk()
root.title("Convertidor de automatas")
root.resizable(True, True)
root.geometry("800x600") 

#Combobox de opciones grafos
labelOPcionesGrafos = Label(root, text="Seleccione el tipo de autómata que desea visualizar")
combo = ttk.Combobox(root, values=["AFN", "AFD", "AFN-lamda"])
labelOPcionesGrafos.pack()
combo.pack()

#Seccion agregar nuevo estado
labelAgregarEstados = Label(root, text="Agregar estado")
labelEstadosConectados = Label(root, text="Ingrese los estados conectados, separados por coma (,)")
entryEstadosConectados = Entry(root)
labelValorConexion = Label(root, text="Ingrese el valor de la conexión")
entryValorConexion = Entry(root)
botonAgregarEstado = Button(root, text="Agregar estado")
labelAgregarEstados.pack()
labelEstadosConectados.pack()
entryEstadosConectados.pack() 
labelValorConexion.pack()
entryValorConexion.pack()
botonAgregarEstado.pack()

#Creacion de la vizualiacion del automata
figure = plt.Figure(figsize=(5, 5), dpi=100)
ax = figure.add_subplot(111)
graph = nx.DiGraph()
graph.add_edge(1, 2, weight=4.7 )
pos = nx.spring_layout(graph)
nx.draw(graph, pos, ax=ax, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', font_size=16)
canvas = FigureCanvasTkAgg(figure, master=root)
canvas.get_tk_widget().pack()
canvas.draw()

root.mainloop()