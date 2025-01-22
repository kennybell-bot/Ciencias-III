from Conexion import Conexion

class Estado:
    def __init__(self, id):
        self.id = id
        self.conexiones = []

    def agregarConexion(self, estadoLLegada, valor):
        conexion = Conexion(self, estadoLLegada, valor)
        self.conexiones.append(conexion)

    def getConxiones(self):
        return self.conexiones
    
    def getID(self):
        return self.id

    def __str__(self):
        conexiones_ids = [conexion.estadoLlegada.id for conexion in self.conexiones]
        return f"Estado(id={self.id}, conexiones={conexiones_ids})"