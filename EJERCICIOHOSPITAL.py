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

#defino clase hospital 

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


# main

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

            medico = Medico(nombre, cedula, genero, servicio, turno, especialidad)
            hospital.agregar_medico(medico)

        elif opcion == "2":
            nombre = input("Nombre: ")
            cedula = input("Cédula: ")
            genero = input("Género: ")
            servicio = input("Servicio: ")
            turno = input("Turno: ")
            rango = input("Rango: ")

            enfermera = Enfermera(nombre, cedula, genero, servicio, turno, rango)
            hospital.agregar_enfermera(enfermera)

        elif opcion == "3":
            nombre = input("Nombre: ")
            cedula = input("Cédula: ")
            genero = input("Género: ")
            servicio = input("Servicio: ")

            paciente = Paciente(nombre, cedula, genero, servicio)

            if hospital.agregar_paciente(paciente):
                print("Paciente agregado correctamente.")
            else:
                print("Ya existe un paciente con esa cédula.")

        elif opcion == "4":
            cedula_medico = input("Cédula del médico: ")
            cedula_paciente = input("Cédula del paciente: ")

            medico = hospital.buscar_medico(cedula_medico)
            paciente = hospital.buscar_paciente_por_cedula(cedula_paciente)

            if medico and paciente:
                medico.asignar_paciente(paciente)
                print("Paciente asignado correctamente.")
            else:
                print("Médico o paciente no encontrado.")

        elif opcion == "5":
            hospital.mostrar_todo()

        elif opcion == "6":
            print("Buscar por:")
            print("1. Cédula")
            print("2. Nombre")

            tipo = input("Seleccione: ")

            if tipo == "1":
                cedula = input("Ingrese cédula: ")
                paciente = hospital.buscar_paciente_por_cedula(cedula)

                if paciente:
                    print(paciente)
                else:
                    print("Paciente no encontrado.")

            elif tipo == "2":
                nombre = input("Ingrese nombre o inicio: ")
                resultados = hospital.buscar_paciente_por_nombre(nombre)

                if resultados:
                    for p in resultados:
                        print(p)
                else:
                    print("No se encontraron pacientes.")

        elif opcion == "7":
            print("Total pacientes:", hospital.total_pacientes())

        elif opcion == "8":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()