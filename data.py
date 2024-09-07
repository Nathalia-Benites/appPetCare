import mysql.connector
from mysql.connector import Error
from bcrypt import hashpw, gensalt
from pymsgbox import password

class AppPetCare:
    def __init__(self):
        self.conectar()

    def conectar(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
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
            contrasena = input("Ingrese la contraseña: ")
            hashed_password = hashpw(contrasena.encode(), gensalt())

            query = "INSERT INTO CLIENTE (nombre, direccion, telefono, ciudad, correo, contrasena) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(query, (nombre, direccion, telefono, ciudad, correo, hashed_password))
            self.conn.commit()
            print("Usuario registrado exitosamente.")
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

    def realizarPedido(self):
        try:
            user_id = int(input("Ingrese el ID del usuario que realiza el pedido: "))
            total = 0
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
                                                                 'precio': precio}
                            total += precio * cantidad
                            # Actualizar el stock
                            self.cursor.execute("UPDATE PRODUCTO SET stock = stock - %s WHERE id_producto = %s",
                                                (cantidad, producto_id))
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
                        del pedido_productos[producto_id]
                    else:
                        print("Producto no encontrado en el pedido.")

                elif opcion == "3":
                    if pedido_productos:
                        # Registrar pedido en la base de datos
                        query = "INSERT INTO PEDIDO (id_cliente, fecha, total) VALUES (%s, CURDATE(), %s)"
                        self.cursor.execute(query, (user_id, total))
                        pedido_id = self.cursor.lastrowid

                        # Registrar detalles del pedido
                        for producto_id, detalles in pedido_productos.items():
                            descripcion = detalles['descripcion']
                            cantidad = detalles['cantidad']
                            precio = detalles['precio']
                            query = "INSERT INTO DETALLE_PEDIDO (id_pedido, id_producto, cantidad, precio) VALUES (%s, %s, %s, %s)"
                            self.cursor.execute(query, (pedido_id, producto_id, cantidad, precio))

                        self.conn.commit()

                        # Mostrar resumen del pedido
                        print(f"\nPedido realizado con éxito. Total a pagar: ${total:.2f}")
                        print("Detalles del pedido:")
                        for producto_id, detalles in pedido_productos.items():
                            descripcion = detalles['descripcion']
                            cantidad = detalles['cantidad']
                            precio = detalles['precio']
                            print(
                                f"Producto ID: {producto_id}, Descripción: {descripcion}, Cantidad: {cantidad}, Precio unitario: ${precio:.2f}, Total: ${precio * cantidad:.2f}")
                    else:
                        print("No se han agregado productos al pedido.")
                    break

                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")

        except Error as e:
            print(f"Error de MySQL: {e}")

    def eliminarProducto(self):
        try:
            producto_id = int(input("Ingrese el ID del producto que desea eliminar: "))

            # Verificar si el producto existe antes de intentar eliminarlo
            self.cursor.execute("SELECT * FROM PRODUCTO WHERE id_producto = %s", (producto_id,))
            if self.cursor.fetchone():
                # Eliminar el producto de la base de datos
                self.cursor.execute("DELETE FROM PRODUCTO WHERE id_producto = %s", (producto_id,))
                self.conn.commit()
                print(f"Producto ID {producto_id} eliminado exitosamente.")
            else:
                print("Producto no encontrado en la base de datos.")
        except Error as e:
            print(f"Error de MySQL: {e}")

    def mostrarPedidos(self):
        try:
            self.cursor.execute("SELECT * FROM PEDIDO")
            pedidos = self.cursor.fetchall()
            for pedido in pedidos:
                print(f"Pedido ID: {pedido[0]}, Cliente ID: {pedido[1]}, Total: ${pedido[3]:.2f}, Fecha: {pedido[2]}")
        except Error as e:
            print(f"Error de MySQL: {e}")

    def mostrarUsuarios(self):
        try:
            self.cursor.execute("SELECT * FROM CLIENTE")
            usuarios = self.cursor.fetchall()
            for usuario in usuarios:
                print(f"Usuario ID: {usuario[0]}, Nombre: {usuario[1]}, Correo: {usuario[5]}, Teléfono: {usuario[3]}")
        except Error as e:
            print(f"Error de MySQL: {e}")

    def mostrarProductos(self):
        try:
            self.cursor.execute("SELECT * FROM PRODUCTO")
            productos = self.cursor.fetchall()
            for producto in productos:
                print(f"Producto ID: {producto[0]}, Descripción: {producto[1]}, Precio: ${producto[2]:.2f}, Stock: {producto[3]}, Categoría ID: {producto[4]}")
        except Error as e:
            print(f"Error de MySQL: {e}")
