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



#Creacion de la vizualiacion del automata
figure = plt.Figure(figsize=(5, 5), dpi=100)
ax = figure.add_subplot(111)
graph = nx.DiGraph()  
pos = nx.spring_layout(graph)
nx.draw(graph, pos, ax=ax, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', font_size=16)
canvas = FigureCanvasTkAgg(figure, master=root)
canvas.get_tk_widget().pack()
canvas.draw()

#Funciones para dibujar el grafo
def agregarNodo(nodo_id):
    graph.add_node(nodo_id)
    actualizarGrafo()

def agregarEdge(nodo_partida, nodo_llegada, label):
    graph.add_edge(nodo_partida, nodo_llegada, label=label)
    actualizarGrafo()

def actualizarGrafo():
    ax.clear()
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, ax=ax, with_labels=True, node_color='skyblue', node_size=200, edge_color='k', font_size=6)
    global edge_labels
    edge_labels = nx.get_edge_attributes(graph, 'label')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, ax=ax)
    canvas.draw()

#Inicializacion del grafico
labelOPcionesGrafos = Label(root, text="Seleccione el tipo de autómata que desea visualizar")
combo = ttk.Combobox(root, values=["AFN", "AFD", "AFN-lamda"])
botonInicializar = Button(root, text="Inicializar")
labelOPcionesGrafos.pack()
combo.pack()

#Agregacion de conexion
labelAgregarConexion = Label(root, text="Agregar conexion")
labelEstadoPartida = Label(root, text="Estado de partida")
entryEstadoPartida = Entry(root)
labelEstadoConectado = Label(root, text="Estados conectados separados por coma")
entryEstadoConectado = Entry(root)
labelValorConexion = Label(root, text="Valor de la conexion")
entryValorConexion = Entry(root)
botonAgregarConexion = Button(root, text="Agregar")
labelEstadoConectado.pack()
entryEstadoConectado.pack()
labelValorConexion.pack()   
entryValorConexion.pack()   
botonAgregarConexion.pack()

def agreagarConexionNueva():
    estadosConectados = entryEstadoConectado.get().split(",")
    agregarEdge(estadosConectados[0], estadosConectados[1], entryValorConexion.get())

botonAgregarConexion.config(command=agreagarConexionNueva)

#Establecimiento del automata
estados = list(graph.nodes)
#Automata
def generarAutomata():
    agregarNodo("q0")
    estados = list(graph.nodes)
    conexiones = nx.get_edge_attributes(graph, 'label')
    return AutomataFinito(Estado(estados[0]))

automata = generarAutomata()

def agregarEstaodosAutomata():
    for i in estados:
        AutomataFinito.agregarEstado(Estado(i))

def prueba():
    agregarEstaodosAutomata()
    print("automata")

    for i in automata.getEstados():
        print(i)

botonInicializar.config(command=prueba)
botonInicializar.pack()

root.mainloop()