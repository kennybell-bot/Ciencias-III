class Estado:
    def __init__(self, id):
        self._id = id
        self._conexiones = []

    # Getters
    def get_id(self):
        return self._id

    def get_conexiones(self):
        return self._conexiones

    # Setters
    def set_id(self, id):
        self._id = id

    def set_conexiones(self, conexiones):
        self._conexiones = conexiones

    # Método para agregar una conexión
    def agregar_conexion(self, conexion):
        self._conexiones.append(conexion)