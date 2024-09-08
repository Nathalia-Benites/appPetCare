from data import AppPetCare, Error

def mostrar_encabezado():
    print("="*50)
    print("\t\tBIENVENIDO A APP PETCARE")
    print("="*50)

def mostrar_menu():
    print("\n" + "-"*50)
    print("Menú Principal:")
    print("1. Usuarios")
    print("2. Mascotas")
    print("3. Productos")
    print("4. Pedidos")
    print("5. Salir")
    print("-"*50)

def menu_usuarios():
    print("\nOpciones de Usuarios:")
    print("1. Registrar Usuario")
    print("2. Mostrar Usuarios")
    print("3. Registrar Dirección de Envío")
    print("4. Mostrar Direcciones de Envío de un Usuario")
    print("5. Registrar Método de Pago")
    print("6. Mostrar Métodos de Pago")
    print("7. Eliminar Método de Pago")

def menu_mascotas():
    print("\nOpciones de Mascotas:")
    print("1. Registrar Mascota")
    print("2. Mostrar Mascotas")
    print("3. Eliminar Mascota")

def menu_productos():
    print("\nOpciones de Productos:")
    print("1. Registrar Producto")
    print("2. Mostrar Productos")

def menu_pedidos():
    print("\nOpciones de Pedidos:")
    print("1. Realizar Pedido")
    print("2. Mostrar Pedidos")

def main():
    app = AppPetCare()
    try:
        mostrar_encabezado()

        while True:
            mostrar_menu()
            try:
                opcion = int(input("Escoja una opción (1-5): \t"))
            except ValueError:
                print("❌ Error: Por favor, ingrese un número válido.")
                continue

            if opcion == 1:
                menu_usuarios()
                try:
                    sub_opcion = int(input("Escoja una opción (1-7): \t"))
                    if sub_opcion == 1:
                        app.registrarUsuario()
                        print("✔ Usuario registrado exitosamente.")
                    elif sub_opcion == 2:
                        app.mostrarUsuarios()
                    elif sub_opcion == 3:
                        app.registrarDireccionEnvio()
                        print("✔ Dirección de envío registrada exitosamente.")
                    elif sub_opcion == 4:
                        id_cliente = int(input("Ingrese el ID del cliente para mostrar sus direcciones: "))
                        app.mostrarDireccionesEnvio(id_cliente)
                    elif sub_opcion == 5:
                        app.registrarMetodoPago()
                        print("✔ Método de pago registrado exitosamente.")
                    elif sub_opcion == 6:
                        app.mostrarMetodosPago()
                    elif sub_opcion == 7:
                        app.eliminarMetodoPago()
                        print("✔ Método de pago eliminado exitosamente.")
                    else:
                        print("❌ Opción no válida.")
                except Error as e:
                    print(f"❌ Error al manejar usuarios: {e}")

            elif opcion == 2:
                menu_mascotas()
                try:
                    sub_opcion = int(input("Escoja una opción (1-3): \t"))
                    if sub_opcion == 1:
                        app.registrarMascota()
                        print("✔ Mascota registrada exitosamente.")
                    elif sub_opcion == 2:
                        app.mostrarMascotas()
                    elif sub_opcion == 3:
                        app.eliminarMascota()
                        print("✔ Mascota eliminada exitosamente.")
                    else:
                        print("❌ Opción no válida.")
                except Error as e:
                    print(f"❌ Error al manejar mascotas: {e}")

            elif opcion == 3:
                menu_productos()
                try:
                    sub_opcion = int(input("Escoja una opción (1-2): \t"))
                    if sub_opcion == 1:
                        app.registrarProducto()
                        print("✔ Producto registrado exitosamente.")
                    elif sub_opcion == 2:
                        app.mostrarProductos()
                    else:
                        print("❌ Opción no válida.")
                except Error as e:
                    print(f"❌ Error al manejar productos: {e}")

            elif opcion == 4:
                menu_pedidos()
                try:
                    sub_opcion = int(input("Escoja una opción (1-2): \t"))
                    if sub_opcion == 1:
                        app.realizarPedido()
                        print("✔ Pedido realizado exitosamente.")
                    elif sub_opcion == 2:
                        app.mostrarPedidos()
                    else:
                        print("❌ Opción no válida.")
                except Error as e:
                    print(f"❌ Error al manejar pedidos: {e}")

            elif opcion == 5:
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

if __name__ == "__main__":
    main()


