from Estado import Estado

class AutomataFinitoDeterministico:
    def __init__(self, estadoInicial):
        self.estadoInicial = estadoInicial
        self.estadosFinales = []
        self.conjuntoEstados = []

    def agregarEstado(self, estado):
        self.conjuntoEstados.add(estado)

    def eliminarEstado(self, estado):
        if estado in self.conjuntoEstados:
            self.conjuntoEstados.remove(estado)

    def __str__(self):
        return f"AutomataFinitoDeterministico(estadoInicial={self.estadoInicial}, estadoFinal={self.estadoFinal}, conjuntoEstados={self.conjuntoEstados})"