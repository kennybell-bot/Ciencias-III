import networkx as nx

class AdaptadorDiagrama:
    def __init__(self):
        pass

    def obtener_nodos_y_adyacencias(self, automata):
        nodos = list(automata.nodes)
        adyacencias = {}
        alfabeto = set()  # Usamos un conjunto para evitar duplicados
        estado_inicial = None
        estados_finales = []

        for nodo in automata.nodes:
            adyacencias[nodo] = {}
            for adj in automata.adj[nodo]:
                label = automata[nodo][adj].get('label', '')
                alfabeto.add(label)  # Añadimos el label al conjunto
                if label not in adyacencias[nodo]:
                    adyacencias[nodo][label] = []
                adyacencias[nodo][label].append(adj)

        # Identificar el estado inicial y los estados finales
        for nodo in nodos:
            color = automata.nodes[nodo].get('color', '')
            if color == 'red':
                estado_inicial = nodo
            elif color == 'yellow':
                estados_finales.append(nodo)

        alfabeto = list(alfabeto)  # Convertimos el conjunto a una lista
        return nodos, adyacencias, alfabeto, estado_inicial, estados_finales
