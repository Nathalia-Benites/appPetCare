from Data import AppPetCare

def menu_principal():
    print("""
    -------------------------------
          MENÚ PRINCIPAL
    -------------------------------
    ¡Te damos la bienvenida a nuestra App!
    
    1. Gestión de Clientes
    2. Gestión de Mascotas
    3. Gestión de Productos
    4. Gestión de Ventas
    5. Gestión de Citas
    6. Gestión de Pedidos
    7. Salir
    """)

def menu_gestion_clientes():
    print("""
    -------------------------------
       GESTIÓN DE CLIENTES
    -------------------------------
    1. Registrar Cliente
    2. Mostrar Clientes
    3. Eliminar Cliente
    4. Volver al Menú Principal
    """)

def menu_gestion_mascotas():
    print("""
    -------------------------------
       GESTIÓN DE MASCOTAS
    -------------------------------
    1. Registrar Mascota
    2. Mostrar Mascotas
    3. Eliminar Mascota
    4. Volver al Menú Principal
    """)

def menu_gestion_productos():
    print("""
    -------------------------------
       GESTIÓN DE PRODUCTOS
    -------------------------------
    1. Registrar Producto
    2. Mostrar Productos
    3. Eliminar Producto
    4. Volver al Menú Principal
    """)

def menu_gestion_ventas():
    print("""
    -------------------------------
       GESTIÓN DE VENTAS
    -------------------------------
    1. Registrar Venta
    2. Mostrar Ventas
    3. Eliminar Venta
    4. Volver al Menú Principal
    """)

def menu_gestion_citas():
    print("""
    -------------------------------
       GESTIÓN DE CITAS
    -------------------------------
    1. Registrar Cita
    2. Mostrar Citas
    3. Eliminar Cita
    4. Volver al Menú Principal
    """)

def menu_gestion_pedidos():
    print("""
    -------------------------------
       GESTIÓN DE PEDIDOS
    -------------------------------
    1. Registrar Pedido
    2. Mostrar Pedidos
    3. Eliminar Pedido
    4. Volver al Menú Principal
    """)

def main():
    app = AppPetCare()

    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':  # Gestión de Clientes
            while True:
                menu_gestion_clientes()
                opcion_cliente = input("Seleccione una opción: ")

                if opcion_cliente == '1':
                    app.registrarCliente()
                elif opcion_cliente == '2':
                    app.mostrarClientes()
                elif opcion_cliente == '3':
                    app.eliminarCliente()
                elif opcion_cliente == '4':
                    break
                else:
                    print("❌ Opción no válida, intente de nuevo.")

        elif opcion == '2':  # Gestión de Mascotas
            while True:
                menu_gestion_mascotas()
                opcion_mascota = input("Seleccione una opción: ")

                if opcion_mascota == '1':
                    app.registrarMascota()
                elif opcion_mascota == '2':
                    app.mostrarMascotas()
                elif opcion_mascota == '3':
                    app.eliminarMascota()
                elif opcion_mascota == '4':
                    break
                else:
                    print("❌ Opción no válida, intente de nuevo.")

        elif opcion == '3':  # Gestión de Productos
            while True:
                menu_gestion_productos()
                opcion_producto = input("Seleccione una opción: ")

                if opcion_producto == '1':
                    app.registrarProducto()
                elif opcion_producto == '2':
                    app.mostrarProductos()
                elif opcion_producto == '3':
                    app.eliminarProducto()
                elif opcion_producto == '4':
                    break
                else:
                    print("❌ Opción no válida, intente de nuevo.")

        elif opcion == '4':  # Gestión de Ventas
            while True:
                menu_gestion_ventas()
                opcion_venta = input("Seleccione una opción: ")

                if opcion_venta == '1':
                    app.registrarVenta()
                elif opcion_venta == '2':
                    app.mostrarVentas()
                elif opcion_venta == '3':
                    app.eliminarVenta()
                elif opcion_venta == '4':
                    break
                else:
                    print("❌ Opción no válida, intente de nuevo.")

        elif opcion == '5':  # Gestión de Citas
            while True:
                menu_gestion_citas()
                opcion_cita = input("Seleccione una opción: ")

                if opcion_cita == '1':
                    app.registrarCita()
                elif opcion_cita == '2':
                    app.mostrarCitas()
                elif opcion_cita == '3':
                    app.eliminarCita()
                elif opcion_cita == '4':
                    break
                else:
                    print("❌ Opción no válida, intente de nuevo.")

        elif opcion == '6':  # Gestión de Pedidos
            while True:
                menu_gestion_pedidos()
                opcion_pedido = input("Seleccione una opción: ")

                if opcion_pedido == '1':
                    app.registrarPedido()
                elif opcion_pedido == '2':
                    app.mostrarPedidos()
                elif opcion_pedido == '3':
                    app.eliminarPedido()
                elif opcion_pedido == '4':
                    break
                else:
                    print("❌ Opción no válida, intente de nuevo.")

        elif opcion == '7':  # Salir
            app.cerrarConexion()
            print("Gracias por usar AppPetCare. ¡Hasta pronto!")
            break

        else:
            print("❌ Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
