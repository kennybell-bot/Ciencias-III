#Variable para correr y finalizar el ciclo del programa
corriendo = True

#Lista de tareas
tareas = []

#Funcion imprimir el menú
def imprimirMenu():
    print("¿Qué desea hacer?: \n\t1.Ingresar tarea \n\t2.Eliminar tarea \n\t3.Mostrar tareas  \n\t4.Dar de alta tarea \n\t5.Salir")

#Función de dar de alta a la tarea
def darDeAlta(idTarea):
    for i in tareas:
        if idTarea == i.id:
            tareas[tareas.index(i)].setEstado(False)

#Función eliminar tarea
def eliminarTarea(idTarea):
    for i in tareas:
        if idTarea == i.getID():
            tareas.pop(tareas.index(i))

#Función mostrar tareas
def mostrarTareas():
    for tarea in tareas:
        print("Tarea: " + tarea.getID() + " Estatus: " + tarea.getEstado() + " Duración: " + tarea.duracion)

#Función ingresare tarea
def ingresarTarea():
    id = input("Id de la tarea: ")
    duracion = input("Duración de la tarea: ")
    tareaNueva = Tarea(id, duracion, True)
    tareas.append(tareaNueva)

#Función organizar tareas
def selection_sort(tareas):
    n = len(tareas)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if tareas[j].getDuracion() < tareas[min_index].getDuracion():
                min_index = j
        tareas[i], tareas[min_index] = tareas[min_index], tareas[i]


#Clase tarea
class Tarea():

    def __init__(self, id, duracion, estado):
        self.id = id
        self.duracion = duracion
        self.estado = True

    def setEstado(self, valor):
        self.estado = valor

    def getNombre(self):
        return self.nombre

    def getDuracion(self):
        return int(self.duracion)

    def getEstado(self):
        return str(self.estado)

    def getID(self):
        return str(self.id)

#Ciclo de ejecución del programa
while(corriendo):

    imprimirMenu()
    eleccion = input("Escriba su opcion: ")

    match eleccion:
        case "1":
            ingresarTarea()
        case "2":
            id = input("Id de la tarea a eliminar: ")
            eliminarTarea(id)
        case "3":
            selection_sort(tareas)
            mostrarTareas()
        case "4":
            id = input("Id de la tarea a dar de alta: ")
            darDeAlta(id)
            mostrarTareas()
        case "5":
            print("Adiós")
            corriendo = False
        case _:
            print("Opción inválida")