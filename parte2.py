class Cliente(Usuario):
    def __init__(self, nombre, correo, numero_cliente):
        super().__init__(nombre, correo)
        self.numero_cliente = numero_cliente

#Sobre escritura
    def mostrar_datos(self):
        return f"Cliente: {self.nombre}, número: {self.numero_cliente}"


class Administrador(Usuario):
    # No define __init__: hereda el de Usuario
    def mostrar_datos(self):
        return f"Administrador: {self.nombre}"