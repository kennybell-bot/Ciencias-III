class AutomataFinito:
    def __init__(self, estadoInicial):
        self.estadoInicial = estadoInicial
        self.estadoFinal = []
        self.conjuntoEstados = []

    def agregarEstado(self, estado):
        self.conjuntoEstados.append(estado)

    def eliminarEstado(self, estado):
        if estado in self.conjuntoEstados:
            self.conjuntoEstados.remove(estado)

    def setConjuntoEstados(self, conjuntoEstados):
        self.conjuntoEstados = conjuntoEstados

    def getEstados(self):
        return self.conjuntoEstados

    def __str__(self):
        return f"AutomataFinito(estadoInicial={self.estadoInicial}, estadoFinal={self.estadoFinal}, conjuntoEstados={self.conjuntoEstados})"