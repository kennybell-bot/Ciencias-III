from Adapter import AdaptadorDiagrama

class Controlador:
    
    def adaptar_diagrama(self, automata):
        adaptador = AdaptadorDiagrama()
        nodos, adyacencias, alfabeto, estado_inicial, estados_finales = adaptador.obtener_nodos_y_adyacencias(automata)
        print("Estados:", nodos)
        print("Conexiones:", adyacencias)
        print("Alfabeto:", alfabeto)
        print("Estado inicial:", estado_inicial)
        print("Estados finales:", estados_finales)

    