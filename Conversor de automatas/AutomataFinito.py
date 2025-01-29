class AutomataFinito:
    def __init__(self):
        self._estados = []
        self._estado_inicial = None
        self._estados_finales = []

    # Getters
    def get_estados(self):
        return self._estados

    def get_estado_inicial(self):
        return self._estado_inicial

    def get_estados_finales(self):
        return self._estados_finales

    # Setters
    def set_estados(self, estados):
        self._estados = estados
        if estados:
            self._estado_inicial = estados[0]

    def set_estado_inicial(self, estado_inicial):
        if estado_inicial in self._estados:
            self._estado_inicial = estado_inicial
        else:
            raise ValueError("El estado inicial debe estar en la lista de estados")

    def set_estados_finales(self, estados_finales):
        for estado in estados_finales:
            if estado not in self._estados:
                raise ValueError("Todos los estados finales deben estar en la lista de estados")
        self._estados_finales = estados_finales

    # Métodos para agregar estados
    def agregar_estado(self, estado):
        self._estados.append(estado)
        if len(self._estados) == 1:
            self._estado_inicial = estado

    def agregar_estado_final(self, estado):
        if estado in self._estados:
            self._estados_finales.append(estado)
        else:
            raise ValueError("El estado final debe estar en la lista de estados")
