from tkinter import *
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from AutomataFinito import AutomataFinito
from Estado import Estado
from Conexion import Conexion


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
entryEstadoNUuevo = Entry(root)
labelEstadosConectados = Label(root, text="Ingrese los estados conectados, separados por coma (,)")
entryEstadosConectados = Entry(root)
labelValorConexion = Label(root, text="Ingrese el valor de la conexión")
entryValorConexion = Entry(root)
botonAgregarEstado = Button(root, text="Agregar estado")
labelAgregarEstados.pack()
entryEstadoNUuevo.pack()
labelEstadosConectados.pack()
entryEstadosConectados.pack() 
labelValorConexion.pack()
entryValorConexion.pack()
botonAgregarEstado.pack()

#Creacion de la vizualiacion del automata
figure = plt.Figure(figsize=(5, 5), dpi=100)
ax = figure.add_subplot(111)
graph = nx.DiGraph()  
graph.add_edge(1, 4, label='a')
graph.add_edge(1, 2, label='b')
graph.add_edge(1, 3, label='c')
pos = nx.spring_layout(graph)
nx.draw(graph, pos, ax=ax, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', font_size=16)
edge_labels = nx.get_edge_attributes(graph, 'label')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, ax=ax)
canvas = FigureCanvasTkAgg(figure, master=root)
canvas.get_tk_widget().pack()
canvas.draw()

def agregarNodo(nodo_id):
    graph.add_node(nodo_id)
    actualizarGrafo()

def actualizarGrafo():
    ax.clear()
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, ax=ax, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', font_size=16)
    edge_labels = nx.get_edge_attributes(graph, 'label')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, ax=ax)
    canvas.draw()

#Prueba automata a partir del grafo
diccionario = {}

#Inicializar estados del grafo en la clase
estados = list(graph.nodes())
automataFinito = AutomataFinito(estados[0])
def agreagarEstados():
    for i in estados:
        automataFinito.agregarEstado(Estado(i))

    for i in automataFinito.getEstados():
        diccionario[i.getID()] = i


def agreagarConexiones():
    conexiones = list(graph.edges())
    for i in conexiones:
        diccionario[i[0]].agregarConexion(diccionario[i[1]], "a")

agreagarEstados()
agreagarConexiones()

for i in automataFinito.getEstados():
    print(i)

#Seccion de la conversion
labelConversion = Label(root, text="Sleccion el automata al que desea convertir")
comboConversion = ttk.Combobox(root, values=["AFN", "AFD", "AFN-lamda"])
labelConversion.pack()
comboConversion.pack()

print(edge_labels)

root.mainloop()