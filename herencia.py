class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def mostrar_datos(self):
        return f"Nombre: {self.nombre} - Correo: {self.correo}"


class Cliente(Usuario):
    def __init__(self, nombre, correo, numero_cliente):
        super().__init__(nombre, correo)
        self.numero_cliente = numero_cliente

    def mostrar_datos(self):
        return f"Cliente: {self.nombre}, número: {self.numero_cliente}"


class Administrador(Usuario):
    # No define __init__: hereda el de Usuario
    def mostrar_datos(self):
        return f"Administrador: {self.nombre}"


# Crear una lista con objetos de diferentes clases
usuarios = [
    Cliente("Ana", "ana@correo.com", 101),
    Administrador("Carlos", "carlos@correo.com"),
    Cliente("Luisa", "luisa@correo.com", 102)
]

# Recorrer la lista con un solo for
for usuario in usuarios:
    print(usuario.mostrar_datos())