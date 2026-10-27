class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def mostrar_datos(self):
        return f"Nombre: {self.nombre} - Correo: {self.correo}"


class Cliente(Usuario):
    pass


class Administrador(Usuario):
    pass


#Diferencia principal
#- Python: class Cliente(Usuario)
#- JavaScript: class Cliente extends Usuario