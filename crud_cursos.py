import pyodbc

# DATOS DE CONEXIÓN
name_server ='DESKTOP-6GO61O3\\SQLEXPRESS'
database ='UDEMYTEST1'
username ='pythonconect'
password ='UDLA'
controlador_odbc ='SQL Server'

# CADENA DE CONEXIÓN
connection_string = f'''
DRIVER={controlador_odbc};
SERVER={name_server};
DATABASE={database};
UID={username};
PWD={password}
'''

# CONEXIÓN
try:
    conexion = pyodbc.connect(connection_string)
    print("✅ Conexión exitosa")

except Exception as e:
    print("❌ Error al conectar:", e)

def insertar_registro(conexion):

    try:
        nombre = input("Ingrese nombre del curso: ")
        categoria = input("Ingrese categoría: ")
        precio = float(input("Ingrese precio: "))

        cursor = conexion.cursor()

        sql = """
        INSERT INTO Cursos(NombreCurso, Categoria, Precio)
        VALUES (?, ?, ?)
        """

        cursor.execute(sql, (nombre, categoria, precio))
        conexion.commit()

        print("✅ Registro insertado correctamente")

    except Exception as e:
        print("❌ Error al insertar:", e)

def consultar_registros(conexion):

    try:
        cursor = conexion.cursor()

        sql = "SELECT * FROM Cursos"

        cursor.execute(sql)

        registros = cursor.fetchall()

        print("\n📚 LISTA DE CURSOS\n")

        for r in registros:
            print(f"""
ID: {r.IDCurso}
Curso: {r.NombreCurso}
Categoría: {r.Categoria}
Precio: {r.Precio}
-------------------------
""")

    except Exception as e:
        print("❌ Error al consultar:", e)


def actualizar_registro(conexion):

    try:
        idcurso = int(input("Ingrese ID del curso a actualizar: "))

        nuevo_nombre = input("Nuevo nombre: ")
        nueva_categoria = input("Nueva categoría: ")
        nuevo_precio = float(input("Nuevo precio: "))

        cursor = conexion.cursor()

        sql = """
        UPDATE Cursos
        SET NombreCurso = ?, Categoria = ?, Precio = ?
        WHERE IDCurso = ?
        """

        cursor.execute(sql, (nuevo_nombre, nueva_categoria, nuevo_precio, idcurso))

        conexion.commit()

        print("✅ Registro actualizado")

    except Exception as e:
        print("❌ Error al actualizar:", e)

def eliminar_registro(conexion):

    try:
        idcurso = int(input("Ingrese ID del curso a eliminar: "))

        cursor = conexion.cursor()

        sql = "DELETE FROM Cursos WHERE IDCurso = ?"

        cursor.execute(sql, (idcurso,))

        conexion.commit()

        print("✅ Registro eliminado")

    except Exception as e:
        print("❌ Error al eliminar:", e)

def mostrar_opciones_crud():

    print("\n========================")
    print("   SISTEMA CRUD CURSOS")
    print("========================")
    print("1. Insertar curso")
    print("2. Consultar cursos")
    print("3. Actualizar curso")
    print("4. Eliminar curso")
    print("5. Salir")

while True:

    mostrar_opciones_crud()

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        insertar_registro(conexion)

    elif opcion == '2':
        consultar_registros(conexion)

    elif opcion == '3':
        actualizar_registro(conexion)

    elif opcion == '4':
        eliminar_registro(conexion)

    elif opcion == '5':
        print("👋 Saliendo del sistema...")
        conexion.close()
        break

    else:
        print("❌ Opción inválida")