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