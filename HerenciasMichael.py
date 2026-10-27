
# Una clase es plantilla que agrupa en un solo lugar caracteristicas y acciones
# de los elementos guardados en ella. Definición general de mi objeto.  


class Robot():
# El def significa _define_, define los metodos o las funciones 
# (agarrar los datos para luego utilizarlos)

 def partes_del_Robot(self, brazos, cabeza, circuitos, piernas):
     self.brazos = brazos
     self.cabeza = cabeza
     
 
# El __init__ es un constructor, es decir, un inicializador, 
# donde se almacenan los argumentos, (las caracteristicas de la clase)
# para que estén listos cuando se requiera llamarlos.  

def __init__(self, brazos, cabeza, circuitos, piernas):
    
# Self es la palabra que utiliza un objeto para referenciarse así mismo
#    
    self.brazos = brazos
    self.cabeza = cabeza


class Persona():
    
    def __init__(self, apellidoPat, apellidoMat, nom):
        self.apellidoPaterno = apellidoPat
        self.apellidoMaterno = apellidoMat
        self.nombres = nom
        
    def mostrarNombreCompleto(self):
        txt = "{0}, {1}, {2}"
        
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)
    
class Estudiante(Persona):
    
    def __init__(self, apellidoPat, apellidoMat, nom, pro):
        super().__init__(apellidoPat, apellidoMat, nom)
        self.profesion=pro

estu1=Estudiante("Torres", "Lopez", "Andres", "Ingeneria De Sistemas")
print(estu1.mostrarNombreCompleto())
print(estu1.profesion)
    