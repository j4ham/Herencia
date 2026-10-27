# =====================================================================
# 1. LA IMPORTACIÓN BASE
# =====================================================================
# Traemos el módulo 'models' desde los archivos internos de bases de datos de Django.
from django.db import models

# =====================================================================
# 2. LA HERENCIA (¿De quién hereda y qué gana?)
# =====================================================================
# ¿De quién hereda?: De la clase 'Model', programada por los creadores de Django.
# ¿Qué gana?: Absorbe métodos invisibles (como .save(), .delete(), .objects) 
# y todo el poder del ORM para crear tablas en la base de datos sin escribir SQL.
class Producto(models.Model):
    
    # =================================================================
    # 3. ARGUMENTOS CON NOMBRE (kwargs)
    # =================================================================
    # 'max_length=100', 'max_digits=8' y 'decimal_places=2' son argumentos con nombre.
    # Le dicen a Django las restricciones exactas y el tamaño que tendrán 
    # estas columnas en la base de datos.
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    # =================================================================
    # 4. SOBRESCRITURA DE MÉTODOS (__str__)
    # =================================================================
    # Sobrescribimos el método especial __str__ que viene por defecto en Python.
    # Si no lo hacemos, Django mostraría textos ilegibles como <Producto (1) object>.
    # Al retornar 'self.nombre', garantizamos que el panel de administrador 
    # muestre el nombre real y legible de nuestro producto.
    def __str__(self):
        return self.nombre