import mysql.connector
from mysql.connector import Error
from bcrypt import hashpw, gensalt
from decimal import Decimal

class AppPetCare:
    def __init__(self):
        self.conectar()

    def conectar(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # Cambia según sea necesario
                database="petCare"
            )
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                print("Conexión establecida con la base de datos.")
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")

    def cerrarConexion(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexión cerrada con la base de datos.")

    def registrarUsuario(self):
        try:
            nombre = input("Ingrese el nombre del usuario: ")
            direccion = input("Ingrese la dirección del usuario: ")
            telefono = input("Ingrese el número de teléfono: ")
            ciudad = input("Ingrese la ciudad: ")
            correo = input("Ingrese el correo electrónico: ")

            query = "INSERT INTO CLIENTE (nombre, direccion, telefono, ciudad, correo) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(query, (nombre, direccion, telefono, ciudad, correo))
            self.conn.commit()
            print("Usuario registrado exitosamente.")
        except Error as e:
            print(f"Error de MySQL: {e}")

    def registrarMetodoPago(self):
        try:
            id_cliente = int(input("Ingrese el ID del cliente: "))
            numero_tarjeta = input("Ingrese el número de la tarjeta: ")
            fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
            tipo_tarjeta = input("Ingrese el tipo de tarjeta (crédito/débito): ")

            hashed_numero_tarjeta = hashpw(numero_tarjeta.encode(), gensalt())

            query = """
              INSERT INTO METODO_PAGO (id_cliente, numero_tarjeta, fecha_vencimiento, tipo_tarjeta)
              VALUES (%s, %s, %s, %s)
              """
            self.cursor.execute(query, (id_cliente, hashed_numero_tarjeta, fecha_vencimiento, tipo_tarjeta))
            self.conn.commit()
            print("Método de pago registrado exitosamente.")
        except Error as e:
            print(f"Error de MySQL: {e}")

    def mostrarMetodosPago(self):
        try:
            self.cursor.execute("SELECT * FROM METODO_PAGO")
            metodos_pago = self.cursor.fetchall()
            for metodo in metodos_pago:
                print(
                    f"Método de Pago ID: {metodo[0]}, Cliente ID: {metodo[1]}, Fecha Vencimiento: {metodo[3]}, Tipo: {metodo[4]}")
        except Error as e:
            print(f"Error de MySQL: {e}")

    def eliminarMetodoPago(self):
        try:
            id_metodo_pago = int(input("Ingrese el ID del método de pago que desea eliminar: "))
            query = "DELETE FROM METODO_PAGO WHERE id_metodo_pago = %s"
            self.cursor.execute(query, (id_metodo_pago,))
            self.conn.commit()
            print("Método de pago eliminado exitosamente.")
        except Error as e:
            print(f"Error de MySQL: {e}")

    def registrarMascota(self):
        try:
            id_cliente = int(input("Ingrese el ID del cliente: "))
            nombre = input("Ingrese el nombre de la mascota: ")
            especie = input("Ingrese la especie de la mascota: ")
            raza = input("Ingrese la raza de la mascota: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento de la mascota (YYYY-MM-DD): ")

            query = """
              INSERT INTO MASCOTA (id_cliente, nombre, especie, raza, fecha_nacimiento)
              VALUES (%s, %s, %s, %s, %s)
              """
            self.cursor.execute(query, (id_cliente, nombre, especie, raza, fecha_nacimiento))
            self.conn.commit()
            print("Mascota registrada exitosamente.")
        except Error as e:
            print(f"Error de MySQL: {e}")

    def mostrarMascotas(self):
        try:
            self.cursor.execute("SELECT * FROM MASCOTA")
            mascotas = self.cursor.fetchall()
            for mascota in mascotas:
                print(
                    f"Mascota ID: {mascota[0]}, Cliente ID: {mascota[1]}, Nombre: {mascota[2]}, Especie: {mascota[3]}, Raza: {mascota[4]}, Fecha de Nacimiento: {mascota[5]}")
        except Error as e:
            print(f"Error de MySQL: {e}")

    def eliminarMascota(self):
        try:
            id_mascota = int(input("Ingrese el ID de la mascota que desea eliminar: "))
            query = "DELETE FROM MASCOTA WHERE id_mascota = %s"
            self.cursor.execute(query, (id_mascota,))
            self.conn.commit()
            print("Mascota eliminada exitosamente.")
        except Error as e:
            print(f"Error de MySQL: {e}")

    def registrarProducto(self):
        try:
            descripcion = input("Ingrese la descripción del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese la cantidad en stock: "))
            id_categoria = int(input("Ingrese el ID de la categoría del producto: "))

            query = "INSERT INTO PRODUCTO (descripcion, precio, id_categoria, stock) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (descripcion, precio, id_categoria, stock))
            self.conn.commit()
            print("Producto registrado exitosamente.")
        except Error as e:
            print(f"Error de MySQL: {e}")

    def registrarDireccionEnvio(self):
        try:
            id_cliente = int(input("Ingrese el ID del cliente: "))
            direccion = input("Ingrese la dirección: ")
            ciudad = input("Ingrese la ciudad: ")
            estado = input("Ingrese el estado: ")
            codigo_postal = input("Ingrese el código postal: ")
            pais = input("Ingrese el país: ")

            query = """
            INSERT INTO DIRECCION_ENVIO (id_cliente, direccion, ciudad, estado, codigo_postal, pais)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (id_cliente, direccion, ciudad, estado, codigo_postal, pais))
            self.conn.commit()
            print("Dirección de envío registrada exitosamente.")
        except Error as e:
            print(f"Error de MySQL: {e}")

    def mostrarDireccionesEnvio(self, id_cliente):
        try:
            query = "SELECT * FROM DIRECCION_ENVIO WHERE id_cliente = %s"
            self.cursor.execute(query, (id_cliente,))
            direcciones = self.cursor.fetchall()
            for direccion in direcciones:
                print(
                    f"Dirección ID: {direccion[0]}, Dirección: {direccion[2]}, Ciudad: {direccion[3]}, Estado: {direccion[4]}, Código Postal: {direccion[5]}, País: {direccion[6]}")
        except Error as e:
            print(f"Error de MySQL: {e}")

    def mostrarPedidos(self):
        try:
            self.cursor.execute("SELECT * FROM PEDIDO")
            pedidos = self.cursor.fetchall()
            for pedido in pedidos:
                print(f"Pedido ID: {pedido[0]}, Cliente ID: {pedido[1]}, Total: {pedido[2]}")
        except Error as e:
            print(f"Error al mostrar pedidos: {e}")

    def mostrarUsuarios(self):
        try:
            self.cursor.execute("SELECT * FROM CLIENTE")
            usuarios = self.cursor.fetchall()
            for usuario in usuarios:
                print(
                    f"Usuario ID: {usuario[0]}, Nombre: {usuario[1]}, Dirección: {usuario[2]}, Teléfono: {usuario[3]}, Ciudad: {usuario[4]}, Correo: {usuario[5]}")
        except Error as e:
            print(f"Error al mostrar usuarios: {e}")

    def mostrarProductos(self):
        try:
            self.cursor.execute("SELECT * FROM PRODUCTO")
            productos = self.cursor.fetchall()
            for producto in productos:
                print(
                    f"Producto ID: {producto[0]}, Descripción: {producto[1]}, Precio: {producto[2]}, Stock: {producto[3]}, Categoría ID: {producto[4]}")
        except Error as e:
            print(f"Error al mostrar productos: {e}")

    def realizarPedido(self):
        try:
            user_id = int(input("Ingrese el ID del usuario que realiza el pedido: "))
            total = Decimal(0)
            pedido_productos = {}

            while True:
                print("\nOpciones:")
                print("1. Agregar producto")
                print("2. Eliminar producto")
                print("3. Finalizar pedido")
                opcion = input("Seleccione una opción (1/2/3): ")

                if opcion == "1":
                    producto_id = int(input("Ingrese el ID del producto que desea agregar al pedido: "))
                    cantidad = int(input("Ingrese la cantidad del producto: "))

                    # Consultar precio y stock del producto
                    self.cursor.execute("SELECT descripcion, precio, stock FROM PRODUCTO WHERE id_producto = %s",
                                        (producto_id,))
                    resultado = self.cursor.fetchone()

                    if resultado:
                        descripcion, precio, stock = resultado
                        if cantidad <= stock:
                            if producto_id in pedido_productos:
                                pedido_productos[producto_id]['cantidad'] += cantidad
                            else:
                                pedido_productos[producto_id] = {'descripcion': descripcion, 'cantidad': cantidad,
                                                                 'precio': Decimal(precio)}
                            total += Decimal(precio) * cantidad

                            # Actualizar el stock
                            self.cursor.execute("UPDATE PRODUCTO SET stock = stock - %s WHERE id_producto = %s",
                                                (cantidad, producto_id))
                            print(f"Producto '{descripcion}' agregado al pedido. Stock actualizado.")
                        else:
                            print(
                                f"No hay suficiente stock para el producto ID {producto_id}. Stock disponible: {stock}.")
                    else:
                        print("Producto no encontrado.")

                elif opcion == "2":
                    producto_id = int(input("Ingrese el ID del producto que desea eliminar del pedido: "))
                    if producto_id in pedido_productos:
                        cantidad = pedido_productos[producto_id]['cantidad']
                        precio = pedido_productos[producto_id]['precio']
                        total -= precio * cantidad

                        # Restaurar el stock
                        self.cursor.execute("UPDATE PRODUCTO SET stock = stock + %s WHERE id_producto = %s",
                                            (cantidad, producto_id))
                        print(
                            f"Producto '{pedido_productos[producto_id]['descripcion']}' eliminado del pedido. Stock restaurado.")
                        del pedido_productos[producto_id]
                    else:
                        print("Producto no encontrado en el pedido actual.")

                elif opcion == "3":
                    if pedido_productos:
                        iva = Decimal(0.15)
                        iva_total = total * iva
                        total_con_iva = total + iva_total

                        query = "INSERT INTO PEDIDO (id_cliente, total) VALUES (%s, %s)"
                        self.cursor.execute(query, (user_id, total_con_iva))
                        pedido_id = self.cursor.lastrowid

                        # Guardar los detalles del pedido
                        for producto_id, detalles in pedido_productos.items():
                            cantidad = detalles['cantidad']
                            precio = detalles['precio']
                            query_detalle = "INSERT INTO DETALLE_PEDIDO (id_pedido, id_producto, cantidad, precio) VALUES (%s, %s, %s, %s)"
                            self.cursor.execute(query_detalle, (pedido_id, producto_id, cantidad, precio))

                        self.conn.commit()

                        # Imprimir la factura
                        print("\nFactura:")
                        print(f"ID de Pedido: {pedido_id}")
                        print("Productos Comprados:")
                        for producto_id, detalles in pedido_productos.items():
                            print(
                                f" - {detalles['descripcion']}: {detalles['cantidad']} x {detalles['precio']} = {detalles['cantidad'] * detalles['precio']}")
                        print(f"\nTotal sin IVA: {total:.2f}")
                        print(f"IVA (15%): {iva_total:.2f}")
                        print(f"Total con IVA: {total_con_iva:.2f}")

                        print("Pedido finalizado con éxito.")
                    else:
                        print("No se pueden guardar pedidos vacíos.")
                    break

                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")

        except Error as e:
            print(f"Error de MySQL: {e}")

