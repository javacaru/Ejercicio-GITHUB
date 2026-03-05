# Escribi la clase personal salud como la clase padre 
class PersonalSalud:
    def __init__(self, nombre, cedula, genero, servicio):
        self.nombre = nombre.upper()
        self.cedula = cedula
        self.genero = genero.upper()
        self.servicio = servicio.upper()

    def __str__(self):
        return f"{self.nombre} | Cédula: {self.cedula}"
    