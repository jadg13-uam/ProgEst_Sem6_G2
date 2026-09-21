"""
    Create
    Read
    Update
    Delete
Registrar un listado de edades.
"""

edades = []

def agregarEdad(edad):
    edades.append(edad)

def mostrarEdades():
    return edades

def actualizarEdad(edad, index):
    edades[index] = edad

def eliminarEdad(edad):
    edades.remove(edad)

def menu():
    print("""1. Agregar
2. Editar
3. Eliminar
4. Mostrar
0. Salir
Digite su opcion [0 - 4]:
    """)
    op = int(input())
    return op

def pedirDato():
    dato = 0
    while True:
        try:
            dato = int(input(""))
            return dato
        
        except ValueError:
            print("Escribe un valor valido")

def seleccionarOpcion():
    op = menu()
    if op == 1:
        print("Dime una edad: ")
        edad = pedirDato()
        agregarEdad(edad)
    elif op == 2:
        print("Dime en que posición se encuentra")
        pos = pedirDato()
        print("Dime la nueva Edad: ")
        edad = pedirDato()
        actualizarEdad(edad, pos)
    elif op == 3:
        print("Dime la edad a eliminar: ")
        edad = pedirDato()
        eliminarEdad(edad)
    elif op == 4:
        print(mostrarEdades())
    elif op == 0:
        print("Adios.")
        return 0
    else:
        print("Opcion invalida")
    seleccionarOpcion()

def main():
    seleccionarOpcion()

main()

