from data import AppPetCare, Error

def mostrar_encabezado():
    print("="*50)
    print("\t\tBIENVENIDO A APP PETCARE")
    print("="*50)

def mostrar_menu():
    print("\n" + "-"*50)
    print("Menú Principal:")
    print("1. Registrar Usuario")
    print("2. Registrar Producto")
    print("3. Realizar Pedido")
    print("4. Mostrar Pedidos")
    print("5. Mostrar Usuarios")
    print("6. Mostrar Productos")
    print("7. Salir")
    print("-"*50)

def main():
    app = AppPetCare()
    try:
        mostrar_encabezado()

        while True:
            mostrar_menu()

            try:
                opcion = int(input("Escoja una opción (1-7): \t"))
            except ValueError:
                print("❌ Error: Por favor, ingrese un número válido.")
                continue

            if opcion == 1:
                try:
                    app.registrarUsuario()
                    print("✔ Usuario registrado exitosamente.")
                except Error as e:
                    print(f"❌ Error al registrar usuario: {e}")
            elif opcion == 2:
                try:
                    app.registrarProducto()
                    print("✔ Producto registrado exitosamente.")
                except Error as e:
                    print(f"❌ Error al registrar producto: {e}")
            elif opcion == 3:
                try:
                    app.realizarPedido()
                    print("✔ Pedido realizado exitosamente.")
                except Error as e:
                    print(f"❌ Error al realizar pedido: {e}")
            elif opcion == 4:
                try:
                    app.mostrarPedidos()
                except Error as e:
                    print(f"❌ Error al mostrar pedidos: {e}")
            elif opcion == 5:
                try:
                    app.mostrarUsuarios()
                except Error as e:
                    print(f"❌ Error al mostrar usuarios: {e}")
            elif opcion == 6:
                try:
                    app.mostrarProductos()
                except Error as e:
                    print(f"❌ Error al mostrar productos: {e}")
            elif opcion == 7:
                print("Gracias por preferirnos. ¡Que tenga un excelente día!")
                break
            else:
                print("❌ Opción no válida, por favor intente de nuevo.")
    except Error as e:
        print(f"❌ Error inesperado: {e}")
    finally:
        app.cerrarConexion()

if __name__ == "__main__":
    main()


