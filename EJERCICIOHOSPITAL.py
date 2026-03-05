# Escribi la clase personal salud como la clase padre 
class PersonalSalud:
    def __init__(self, nombre, cedula, genero, servicio):
        self.nombre = nombre.upper()
        self.cedula = cedula
        self.genero = genero.upper()
        self.servicio = servicio.upper()

    def __str__(self):
        return f"{self.nombre} | Cédula: {self.cedula}"
    
# medico, enfermera y paciente heredan de personal salud       

class Medico(PersonalSalud):
    def __init__(self, nombre, cedula, genero, servicio, turno, especialidad):
        super().__init__(nombre, cedula, genero, servicio)
        self.turno = turno.upper()
        self.especialidad = especialidad.upper()
        self.pacientes = []

    def asignar_paciente(self, paciente):
        self.pacientes.append(paciente)
        paciente.medico_asignado = self

    def __str__(self):
        return f"MÉDICO: {super().__str__()} | Especialidad: {self.especialidad}"
    
class Enfermera(PersonalSalud):
    def __init__(self, nombre, cedula, genero, servicio, turno, rango):
        super().__init__(nombre, cedula, genero, servicio)
        self.turno = turno.upper()
        self.rango = rango.upper()

    def __str__(self):
        return f"ENFERMERA: {super().__str__()} | Rango: {self.rango}"

class Paciente(PersonalSalud):
    def __init__(self, nombre, cedula, genero, servicio):
        super().__init__(nombre, cedula, genero, servicio)
        self.medico_asignado = None

    def __str__(self):
        if self.medico_asignado:
            return f"PACIENTE: {super().__str__()} | Médico: {self.medico_asignado.nombre}"
        else:
            return f"PACIENTE: {super().__str__()} | Sin médico asignado"