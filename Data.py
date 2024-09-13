import mysql.connector
from mysql.connector import Error

class AppPetCare:
    def __init__(self):
        self.conectarBD()

    def conectarBD(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                database='App_petCare',
                user='root',
                password=''
            )
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                print("✔ Conexión exitosa a la base de datos.")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def cerrarConexion(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("✔ Conexión a la base de datos cerrada.")

    def registrarCliente(self):
        try:
            cedula = input("Ingrese la cédula del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")
            direccion = input("Ingrese la dirección del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            correo = input("Ingrese el correo del cliente: ")
            ciudad = input("Ingrese la ciudad del cliente: ")

            query = """
                INSERT INTO CLIENTE (cedula, nombre, direccion, telefono, correo, ciudad)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (cedula, nombre, direccion, telefono, correo, ciudad))
            self.conn.commit()
            print("✔ Cliente registrado exitosamente.")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def mostrarClientes(self):
        try:
            self.cursor.execute("SELECT * FROM CLIENTE")
            clientes = self.cursor.fetchall()
            for cliente in clientes:
                print(f"Cédula: {cliente[0]}, Nombre: {cliente[1]}, Dirección: {cliente[2]}, Teléfono: {cliente[4]}, Correo: {cliente[3]}, Ciudad: {cliente[5]}")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def eliminarCliente(self):
        try:
            cedula = input("Ingrese la cédula del cliente que desea eliminar: ")
            query = "DELETE FROM CLIENTE WHERE cedula = %s"
            self.cursor.execute(query, (cedula,))
            self.conn.commit()
            print("✔ Cliente eliminado exitosamente.")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def registrarMascota(self):
        try:
            nombre = input("Ingrese el nombre de la mascota: ")
            especie = input("Ingrese la especie de la mascota: ")
            raza = input("Ingrese la raza de la mascota: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento de la mascota (YYYY-MM-DD): ")
            cedula_usuario = input("Ingrese la cédula del dueño: ")

            query = """
                INSERT INTO MASCOTA (nombre, especie, raza, fecha_nacimiento, cedula_usuario)
                VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (nombre, especie, raza, fecha_nacimiento, cedula_usuario))
            self.conn.commit()
            print("✔ Mascota registrada exitosamente.")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def mostrarMascotas(self):
        try:
            self.cursor.execute("SELECT * FROM MASCOTA")
            mascotas = self.cursor.fetchall()
            for mascota in mascotas:
                print(f"ID Mascota: {mascota[0]}, Nombre: {mascota[1]}, Especie: {mascota[2]}, Raza: {mascota[3]}, Fecha de Nacimiento: {mascota[4]}, Dueño: {mascota[5]}")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def eliminarMascota(self):
        try:
            id_mascota = int(input("Ingrese el ID de la mascota que desea eliminar: "))
            query = "DELETE FROM MASCOTA WHERE id_mascota = %s"
            self.cursor.execute(query, (id_mascota,))
            self.conn.commit()
            print("✔ Mascota eliminada exitosamente.")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def registrarProducto(self):
        try:
            descripcion = input("Ingrese la descripción del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            id_categoria = int(input("Ingrese el ID de la categoría: "))
            stock = int(input("Ingrese la cantidad en stock: "))

            query = """
                INSERT INTO PRODUCTO (descripcion, precio, id_categoria, stock)
                VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (descripcion, precio, id_categoria, stock))
            self.conn.commit()
            print("✔ Producto registrado exitosamente.")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def mostrarProductos(self):
        try:
            self.cursor.execute("SELECT * FROM PRODUCTO")
            productos = self.cursor.fetchall()
            for producto in productos:
                print(f"ID Producto: {producto[0]}, Descripción: {producto[1]}, Precio: {producto[2]}, Categoría: {producto[3]}, Stock: {producto[4]}")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def eliminarProducto(self):
        try:
            id_producto = int(input("Ingrese el ID del producto que desea eliminar: "))
            query = "DELETE FROM PRODUCTO WHERE id_producto = %s"
            self.cursor.execute(query, (id_producto,))
            self.conn.commit()
            print("✔ Producto eliminado exitosamente.")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def registrarVenta(self):
        try:
            cantidad = int(input("Ingrese la cantidad del producto vendido: "))
            cedula_cliente = input("Ingrese la cédula del cliente: ")
            id_producto = int(input("Ingrese el ID del producto: "))

            query = """
                INSERT INTO VENTA (cantidad, cedula_cliente, id_producto)
                VALUES (%s, %s, %s)
            """
            self.cursor.execute(query, (cantidad, cedula_cliente, id_producto))
            self.conn.commit()
            print("✔ Venta registrada exitosamente.")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def mostrarVentas(self):
        try:
            self.cursor.execute("SELECT * FROM VENTA")
            ventas = self.cursor.fetchall()
            for venta in ventas:
                print(f"ID Venta: {venta[0]}, Cantidad: {venta[1]}, Cliente: {venta[2]}, Producto: {venta[3]}")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def eliminarVenta(self):
        try:
            id_venta = int(input("Ingrese el ID de la venta que desea eliminar: "))
            query = "DELETE FROM VENTA WHERE id_venta = %s"
            self.cursor.execute(query, (id_venta,))
            self.conn.commit()
            print("✔ Venta eliminada exitosamente.")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def registrarCita(self):
        try:
            cedula_cliente = input("Ingrese la cédula del cliente: ")
            tipo_cita = input("Ingrese el tipo de cita (Peluqueria, Veterinaria, Vacunación, Desparasitacion): ")
            fecha = input("Ingrese la fecha de la cita (YYYY-MM-DD): ")

            query = """
                INSERT INTO CITA (tipo_cita, fecha, cedula_cliente)
                VALUES (%s, %s, %s)
            """
            self.cursor.execute(query, (tipo_cita, fecha, cedula_cliente))
            self.conn.commit()
            print("✔ Cita registrada exitosamente.")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def mostrarCitas(self):
        try:
            self.cursor.execute("SELECT * FROM CITA")
            citas = self.cursor.fetchall()
            for cita in citas:
                print(f"ID Cita: {cita[0]}, Tipo: {cita[1]}, Fecha: {cita[2]}, Cliente: {cita[3]}")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def eliminarCita(self):
        try:
            id_cita = int(input("Ingrese el ID de la cita que desea eliminar: "))
            query = "DELETE FROM CITA WHERE id_cita = %s"
            self.cursor.execute(query, (id_cita,))
            self.conn.commit()
            print("✔ Cita eliminada exitosamente.")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def registrarPedido(self):
        try:
            cedula_cliente = input("Ingrese la cédula del cliente: ")
            fecha = input("Ingrese la fecha del pedido (YYYY-MM-DD): ")
            total = float(input("Ingrese el total del pedido: "))

            query = """
                INSERT INTO PEDIDO (cedula_cliente, fecha, total)
                VALUES (%s, %s, %s)
            """
            self.cursor.execute(query, (cedula_cliente, fecha, total))
            self.conn.commit()
            print("✔ Pedido registrado exitosamente.")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def mostrarPedidos(self):
        try:
            query = """
                SELECT p.id_pedido, p.cedula_cliente, p.fecha, p.total, c.nombre
                FROM PEDIDO p
                JOIN CLIENTE c ON p.cedula_cliente = c.cedula
            """
            self.cursor.execute(query)
            pedidos = self.cursor.fetchall()
            for pedido in pedidos:
                print(f"ID Pedido: {pedido[0]}, Cliente: {pedido[4]}, Fecha: {pedido[2]}, Total: {pedido[3]}")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

    def eliminarPedido(self):
        try:
            id_pedido = int(input("Ingrese el ID del pedido que desea eliminar: "))
            query = "DELETE FROM PEDIDO WHERE id_pedido = %s"
            self.cursor.execute(query, (id_pedido,))
            self.conn.commit()
            print("✔ Pedido eliminado exitosamente.")
        except Error as e:
            print(f"❌ Error de MySQL: {e}")

# Instancia y uso de la aplicación
app = AppPetCare()

# Puedes probar las funcionalidades llamando a los métodos deseados, por ejemplo:
# app.registrarCliente()
# app.mostrarClientes()
# app.registrarPedido()
# app.mostrarPedidos()

# Recuerda cerrar la conexión al final del uso
app.cerrarConexion()