class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre
Aquí Producto hereda de models.Model; nombre y precio son campos del modelo; y __str__ define qué texto se muestra al representar el producto.