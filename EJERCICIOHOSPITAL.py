# INCLUYO CLASE HOSPITAL

class Hospital:
    def __init__(self):
        self.medicos = []
        self.enfermeras = []
        self.pacientes = []

    # MÉDICOS
    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def buscar_medico(self, cedula):
        for medico in self.medicos:
            if medico.cedula == cedula:
                return medico
        return None

    # ENFERMERAS
    def agregar_enfermera(self, enfermera):
        self.enfermeras.append(enfermera)

    # PACIENTES
    def agregar_paciente(self, paciente):
        for p in self.pacientes:
            if p.cedula == paciente.cedula:
                return False
        self.pacientes.append(paciente)
        return True

    def buscar_paciente_por_cedula(self, cedula):
        for p in self.pacientes:
            if p.cedula == cedula:
                return p
        return None

    def buscar_paciente_por_nombre(self, nombre):
        nombre = nombre.upper()
        resultados = []
        for p in self.pacientes:
            if p.nombre.startswith(nombre):
                resultados.append(p)
        return resultados

    def total_pacientes(self):
        return len(self.pacientes)

    def mostrar_todo(self):
        print("\n--- MÉDICOS ---")
        for m in self.medicos:
            print(m)

        print("\n--- ENFERMERAS ---")
        for e in self.enfermeras:
            print(e)

        print("\n--- PACIENTES ---")
        for p in self.pacientes:
            print(p)

# MAIN 

def main():
    hospital = Hospital()

    while True:
        print("\n--- SISTEMA HOSPITALARIO ---")
        print("1. Agregar Médico")
        print("2. Agregar Enfermera")
        print("3. Agregar Paciente")
        print("4. Asignar Médico a Paciente")
        print("5. Mostrar Todo")
        print("6. Buscar Paciente")
        print("7. Ver número total de pacientes")
        print("8. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            cedula = input("Cédula: ")
            genero = input("Género: ")
            servicio = input("Servicio: ")
            turno = input("Turno: ")
            especialidad = input("Especialidad: ")
