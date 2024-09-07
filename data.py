import mysql

import mysql.connector
from decimal import Decimal
class Error(Exception):
    pass
class Cliente:
    def __init__(self, id_cliente, nombre, direccion, telefono, ciudad):
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._ciudad = ciudad
class Producto:
    def __init__(self, id_producto, descripcion, precio):
        self._id_producto = id_producto
        self._descripcion = descripcion
        self._precio = precio
class Categoria:
    def __init__(self, id_producto, descripcion, precio):
        self._id_producto = id_producto
        self._descripcion = descripcion
        self._precio = precio
class Venta:
    def __init__(self, cantidad, id_cliente, id_producto):
        self._id_venta = 0
        self._cantidad = cantidad
        self._id_cliente = id_cliente
        self._id_producto = id_producto
    def totalPagar(self, precio):
        return precio * self._cantidad
class App:
    def __init__(self):
        self._host = "localh"
        self._user = "root"
        self._password = ""
        self._database = "petCare"
    def conectar(self):
        try:
            self._conn = mysql.connector.connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database
            )
            if self._conn.is_connected():
                self._cursor = self._conn.cursor()
        except mysql.connector.Error as e:
            raise Error(f"Error de conexión: {e}")
    def cerrarConeccion(self):
        if self._conn.is_connected() and self._conn:
            self._conn.close()
            self._cursor.close()
    def registrarClientes(self):
        try:
            id_cliente = int(input("Ingrese el código de identificación del cliente: "))
            nombre = input("Ingrese sus nombres y apellidos: ")
            direccion = input("Ingrese la dirección domiciliaria: ")
            telefono = input("Ingrese el teléfono: ")
            ciudad = input("Ingrese la ciudad de residencia: ")
            query = """
                INSERT INTO cliente (id_cliente, nombre, direccion, telefono, ciudad) 
                VALUES (%s, %s, %s, %s, %s)
            """
            self._cursor.execute(query, (id_cliente, nombre, direccion, telefono, ciudad))
            print("Registro guardado exitosamente")
            self._conn.commit()
        except ValueError as e:
            raise Error(f"Error de valor: {e}")
        except mysql.connector.Error as e:
            raise Error(f"Error de MySQL: {e}")
        except Exception as e:
            raise Error(f"Ha ocurrido un error inesperado: {e}")
    def registrarProducto(self):
        try:
            id_producto = int(input("Ingrese el código del producto: "))
            descripcion = input("Ingrese la descripción del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            query = """
                INSERT INTO producto (id_producto, descripcion, precio) 
                VALUES (%s, %s, %s)
            """
            self._cursor.execute(query, (id_producto, descripcion, precio))
            print("Producto registrado exitosamente")
            self._conn.commit()
        except ValueError as e:
            raise Error(f"Error de valor: {e}")
        except mysql.connector.Error as e:
            raise Error(f"Error de MySQL: {e}")
        except Exception as e:
            raise Error(f"Ha ocurrido un error inesperado: {e}")
    def consultarCliente(self, id_cliente):
        try:
            query = "SELECT nombre FROM cliente WHERE id_cliente = %s"
            self._cursor.execute(query, (id_cliente,))
            resultado = self._cursor.fetchone()
            if resultado:
                return resultado[0]
            return None
        except mysql.connector.Error as e:
            raise Error(f"Error de MySQL: {e}")
    def consultarProducto(self, id_producto):
        try:
            query = "SELECT descripcion, precio FROM producto WHERE id_producto = %s"
            self._cursor.execute(query, (id_producto,))
            resultado = self._cursor.fetchone()
            if resultado:
                # Convertir el precio a float para evitar problemas de tipo
                precio = float(resultado[1])
                return Producto(id_producto, resultado[0], precio)
            return None
        except mysql.connector.Error as e:
            raise Error(f"Error de MySQL: {e}")
    def registrarVentaEnDB(self, venta):
        try:
            query = """
                INSERT INTO venta (cantidad, id_cliente, id_producto) 
                VALUES (%s, %s, %s)
            """
            self._cursor.execute(query, (venta._cantidad, venta._id_cliente, venta._id_producto))
            self._conn.commit()
            print("Venta registrada exitosamente")
        except mysql.connector.Error as e:
            raise Error(f"Error de MySQL al registrar la venta: {e}")
    def registrarVenta(self):
        try:
            id_cliente = int(input("Ingrese el código del cliente: "))
            cliente_nombre = self.consultarCliente(id_cliente)
            if cliente_nombre is None:
                print("Cliente no encontrado.")
                if input("¿Desea registrar al cliente? (si / no): ").lower() == 'si':
                    self.registrarClientes()
                else:
                    print("No se puede registrar la venta sin un cliente.")
                    return
            id_producto = int(input("Ingrese el código del producto: "))
            producto = self.consultarProducto(id_producto)
            if producto is None:
                print("Producto no encontrado.")
                if input("¿Desea registrar el producto? (si / no): ").lower() == 'si':
                    self.registrarProducto()
                else:
                    print("No se puede registrar la venta sin un producto.")
                    return
            cantidad = int(input("Ingrese la cantidad: "))
            venta = Venta(cantidad, id_cliente, id_producto)
            subtotal = venta.totalPagar(producto._precio)
            iva = subtotal * 0.15  # Supongamos que el IVA es del 15%
            total = subtotal + iva
            # Mostrar el detalle de la venta
            print("\n\tDetalle de la Venta:")
            print(f"Cliente: {cliente_nombre}")
            print(f"Producto: {producto._descripcion}")
            print(f"Cantidad: {cantidad}")
            print(f"Precio Unitario: ${producto._precio:.2f}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"IVA (15%): ${iva:.2f}")
            print(f"Total a pagar: ${total:.2f}")
            # Registrar la venta en la base de datos
            self.registrarVentaEnDB(venta)
        except ValueError as e:
            raise Error(f"Error de valor: {e}")
        except mysql.connector.Error as e:
            raise Error(f"Error de MySQL: {e}")
        except Exception as e:
            raise Error(f"Ha ocurrido un error inesperado: {e}")

    def consultarCompraPorCliente(self, id_cliente):
        try:
            query = """
                SELECT nombre, descripcion, cantidad, subtotal, iva, total
                FROM compra
                WHERE idCliente = %s
            """
            self._cursor.execute(query, (id_cliente,))
            resultados = self._cursor.fetchall()

            if resultados:
                print(f"Compras realizadas por el cliente {id_cliente}:")
                for row in resultados:
                    nombre, descripcion, cantidad, subtotal, iva, total = row
                    print(f"Nombre: {nombre}, Producto: {descripcion}, Cantidad: {cantidad}")
                    print(f"Subtotal: ${float(subtotal):.2f}, IVA: ${float(iva):.2f}, Total: ${float(total):.2f}\n")
            else:
                print("No se encontraron compras para el cliente.")
        except mysql.connector.Error as e:
            raise Error(f"Error de MySQL: {e}")
