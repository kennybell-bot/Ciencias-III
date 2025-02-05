import networkx as nx

class AdaptadorDiagrama:
    def __init__(self):
        pass

    def obtener_nodos_y_adyacencias(self, automata):
        nodos = list(automata.nodes)
        adyacencias = {}
        for nodo in automata.nodes:
            adyacencias[nodo] = {}
            for adj in automata.adj[nodo]:
                label = automata[nodo][adj].get('label', '')
                if label not in adyacencias[nodo]:
                    adyacencias[nodo][label] = []
                adyacencias[nodo][label].append(adj)
        return nodos, adyacencias