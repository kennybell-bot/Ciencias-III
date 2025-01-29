from Adapter import AdaptadorDiagrama

class Controlador:
    
    def adaptar_diagrama(self, automata):
        adaptador = AdaptadorDiagrama()
        nodos, adyacencias = adaptador.obtener_nodos_y_adyacencias(automata)
        print("Estados:", nodos)
        print("Conexiones:", adyacencias)

    