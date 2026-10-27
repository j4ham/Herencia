usuarios = [
    Cliente("Ana", "ana@correo.com", 101),
    Administrador("Carlos", "carlos@correo.com"),
    Cliente("Luisa", "luisa@correo.com", 102)
]

for usuario in usuarios:
    print(usuario.mostrar_datos())