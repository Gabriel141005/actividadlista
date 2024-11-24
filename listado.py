class Nodo:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

        self.siguiente = None

class Inventario:

    def __init__(self):
        self.inicio = None

    def agregar(self, id, nombre, cantidad, precio):

        nuevo = Nodo(id, nombre, cantidad, precio)
        if not self.inicio:
            self.inicio = nuevo
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        print(f"Producto '{nombre}' anAdido al inventario")

    def eliminar(self, id):
        if not self.inicio:
            print("No hay nada")
            return
        if self.inicio.id == id:
            print(f"Producto '{self.inicio.nombre}' eliminado")
            self.inicio = self.inicio.siguiente
            return
        actual = self.inicio
        while actual.siguiente and actual.siguiente.id != id:
            actual = actual.siguiente
        if actual.siguiente:
            print(f"Producto '{actual.siguiente.nombre}' eliminado")
            actual.siguiente = actual.siguiente.siguiente
        else:
            print("No encontré el productoo")

    def buscar(self, id):
        actual = self.inicio
        while actual:
            if actual.id == id:
                print(f"Encontrado: ID: {actual.id}, Nombre: {actual.nombre}, Cantidad: {actual.cantidad}, Precio: ${actual.precio:.2f}")
                return
            actual = actual.siguiente
        print("No encontré ese producto")

    def listar(self):
        if not self.inicio:
            print("El inventario está vacío.")
            return
        actual = self.inicio
        print("Productos:")
        while actual:
            print(f"ID: {actual.id}, Nombre: {actual.nombre}, Cantidad: {actual.cantidad}, Precio: ${actual.precio:.2f}")
            actual = actual.siguiente

    def modificar(self, id, nuevo_nombre=None, nueva_cantidad=None, nuevo_precio=None):
        actual = self.inicio
        while actual:
            if actual.id == id:
                if nuevo_nombre:
                    actual.nombre = nuevo_nombre
                if nueva_cantidad:
                    actual.cantidad = nueva_cantidad
                if nuevo_precio:
                    actual.precio = nuevo_precio
                print(f"Producto con ID '{id}' actualizado")
                return
            actual = actual.siguiente
        print("No encontree el producto")

    def vaciar(self):
        self.inicio = None
        print("Inventario vacio")


if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\nmenu del inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Buscar producto")
        print("4. Listar productos")
        print("5. Modificar producto")
        print("6. Vaciar inventario")
        print("7. Salir")
        opcion = input("elija opcion ")

        if opcion == "1":
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar(id, nombre, cantidad, precio)
        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar(id)
        elif opcion == "3":
            id = input("ID del producto a buscar: ")
            inventario.buscar(id)
        elif opcion == "4":
            inventario.listar()
        elif opcion == "5":
            id = input("ID del producto a modificar: ")
            nuevo_nombre = input("Nuevo nombre (déjalo vacío si no cambia): ") or None
            nueva_cantidad = input("Nueva cantidad (déjalo vacío si no cambia): ")
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = input("Nuevo precio (déjalo vacío si no cambia): ")
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            inventario.modificar(id, nuevo_nombre, nueva_cantidad, nuevo_precio)
        elif opcion == "6":
            inventario.vaciar()
        elif opcion == "7":
            print("byeee")
            break
        else:
            print("invalido")
