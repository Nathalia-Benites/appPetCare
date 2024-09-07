from data import AppPetCare, Error

def main():
    app = AppPetCare()
    try:
        print("\t\t\tBienvenidos a su App PetCare")

        while True:
            print("\nMenú:")
            print("1. Registrar Usuario")
            print("2. Registrar Producto")
            print("3. Realizar Pedido")
            print("4. Mostrar Pedidos")
            print("5. Mostrar Usuarios")
            print("6. Mostrar Productos")
            print("7. Salir")

            try:
                opcion = int(input("Escoja una opción (1-7): \t"))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue

            if opcion == 1:
                try:
                    app.registrarUsuario()
                except Error as e:
                    print(e)
            elif opcion == 2:
                try:
                    app.registrarProducto()
                except Error as e:
                    print(e)
            elif opcion == 3:
                try:
                    app.realizarPedido()
                except Error as e:
                    print(e)
            elif opcion == 4:
                try:
                    app.mostrarPedidos()
                except Error as e:
                    print(e)
            elif opcion == 5:
                try:
                    app.mostrarUsuarios()
                except Error as e:
                    print(e)
            elif opcion == 6:
                try:
                    app.mostrarProductos()
                except Error as e:
                    print(e)
            elif opcion == 7:
                print("Gracias por preferirnos. ¡Hasta luego!")
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")
    except Error as e:
        print(e)
    finally:
        app.cerrarConexion()

if __name__ == "__main__":
    main()


