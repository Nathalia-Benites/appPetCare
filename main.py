from data import App, Error
def main():
    app = App()
    try:
        app.conectar()
        print("Bienvenidos a su App PetCare")
        while True:
            print("\nMenú:")
            print("1. Registro de Cliente")
            print("2. Registro de Producto")
            print("3. Registro de la Venta")
            print("4. Buscar compras realizadas por un cliente")
            print("5. Salir")
            try:
                opcion = int(input("Escoja una opción (1-5): \t"))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue
            if opcion == 1:
                try:
                    app.registrarClientes()
                except Error as e:
                    print(e)
            elif opcion == 2:
                try:
                    app.registrarProducto()
                except Error as e:
                    print(e)
            elif opcion == 3:
                try:
                    app.registrarVenta()
                except Error as e:
                    print(e)
            elif opcion == 4:
                try:
                    id_cliente = int(input("Ingrese el código del cliente: "))
                    app.buscarComprasPorCliente(id_cliente)
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                except Error as e:
                    print(e)
            elif opcion == 5:
                print("Gracias por preferirnos")
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")
    except Error as e:
        print(e)
    finally:
        app.cerrarConeccion()
if __name__ == "__main__":
    main()
