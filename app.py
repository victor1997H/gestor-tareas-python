tareas = []

def mostrar_menu():
    print("*** SUPER GESTOR DE TAREAS ***")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("Cerrando aplicación... Adiós")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nueva_tarea = input("Escribe la  tarea: ")
            tareas.append(nueva_tarea)
            print("¡Tarea agregada exitosamente!")
    
        elif opcion == "2":
            print("--- TAREAS PENDIENTES ---")
            for i, tarea in enumerate(tareas):
                print(f"{i + 1}. {tarea}")
            
        elif opcion == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()