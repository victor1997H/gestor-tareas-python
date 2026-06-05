tareas = []

def mostrar_menu():
    print("--- GESTOR DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nueva_tarea = input("Escribe la  tarea: ")
            tareas.append(nueva_tarea)
            print("¡Tarea agregada exitosamente!")
        elif opcion == "2":
            pass # Aquí trabajará el Estudiante A
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()