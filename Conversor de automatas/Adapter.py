import networkx as nx

class AdaptadorDiagrama:
    def __init__(self):
        pass

    def obtener_nodos_y_adyacencias(self, automata):
        nodos = list(automata.nodes)
        adyacencias = {}
        for nodo in automata.nodes:
            adyacencias[nodo] = [(adj, automata[nodo][adj].get('label', '')) for adj in automata.adj[nodo]]
        return nodos, adyacencias