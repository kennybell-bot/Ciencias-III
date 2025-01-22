class Conexion:
    def __init__(self, estadoPartida, estadoLlegada, valor):
        self.estadoPartida = estadoPartida
        self.estadoLlegada = estadoLlegada
        self.valor = valor

    def __str__(self):
        return f"Conexion(estadoPartida={self.estadoPartida.id}, estadoLlegada={self.estadoLlegada.id}, valor={self.valor})"