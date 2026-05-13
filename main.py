import pyodbc
import json


class GestorEstudiantes:

    # CONSTRUCTOR
    def __init__(self):

        try:

            with open('config.json', 'r') as archivo_config:

                config = json.load(archivo_config)

            name_server = config['name_server']
            database = config['database']
            controlador_odbc = config['controlador_odbc']

            self.connection_string = f'''
            DRIVER={{{controlador_odbc}}};
            SERVER={name_server};
            DATABASE={database};
            Trusted_Connection=yes;
            '''

            self.conexion = pyodbc.connect(self.connection_string)

            print("✅ Conexión exitosa con SQL Server")

        except Exception as e:

            print("❌ Error de conexión:", e)

    # INSERTAR
    def insertar_estudiante(self):

        try:

            id_estudiante = int(input("ID Estudiante: "))
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            telefono = input("Telefono: ")

            cursor = self.conexion.cursor()

            cursor.execute("""
                EXEC sp_InsertarEstudiante ?, ?, ?, ?, ?
            """, (
                id_estudiante,
                nombre,
                apellido,
                email,
                telefono
            ))

            self.conexion.commit()

            print("✅ Estudiante insertado correctamente")

        except Exception as e:

            print("❌ Error al insertar:", e)

    # CONSULTAR
    def consultar_estudiantes(self):

        try:

            cursor = self.conexion.cursor()

            cursor.execute("EXEC sp_ConsultarEstudiantes")

            registros = cursor.fetchall()

            print("\n📚 LISTA DE ESTUDIANTES\n")

            for r in registros:

                print(f"""
ID: {r.IDEstudiante}
Nombre: {r.NombreEstudiante}
Apellido: {r.ApellidoEstudiante}
Email: {r.Email}
Telefono: {r.Telefono}
-----------------------------------
""")

        except Exception as e:

            print("❌ Error al consultar:", e)

    # ACTUALIZAR
    def actualizar_estudiante(self):

        try:

            id_estudiante = int(input("ID del estudiante a actualizar: "))

            nombre = input("Nuevo nombre: ")
            apellido = input("Nuevo apellido: ")
            email = input("Nuevo email: ")
            telefono = input("Nuevo telefono: ")

            cursor = self.conexion.cursor()

            cursor.execute("""
                EXEC sp_ActualizarEstudiante ?, ?, ?, ?, ?
            """, (
                id_estudiante,
                nombre,
                apellido,
                email,
                telefono
            ))

            self.conexion.commit()

            print("✅ Estudiante actualizado correctamente")

        except Exception as e:

            print("❌ Error al actualizar:", e)

    # ELIMINAR
    def eliminar_estudiante(self):

        try:

            id_estudiante = int(input("ID del estudiante a eliminar: "))

            cursor = self.conexion.cursor()

            cursor.execute("""
                EXEC sp_EliminarEstudiante ?
            """, (id_estudiante,))

            self.conexion.commit()

            print("✅ Estudiante eliminado correctamente")

        except Exception as e:

            print("❌ Error al eliminar:", e)

    # MENU
    def ejecutar_menu(self):

        while True:

            print("\n===================================")
            print("   SISTEMA CRUD OOP ESTUDIANTES")
            print("===================================")
            print("1. Insertar estudiante")
            print("2. Consultar estudiantes")
            print("3. Actualizar estudiante")
            print("4. Eliminar estudiante")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':

                self.insertar_estudiante()

            elif opcion == '2':

                self.consultar_estudiantes()

            elif opcion == '3':

                self.actualizar_estudiante()

            elif opcion == '4':

                self.eliminar_estudiante()

            elif opcion == '5':

                print("👋 Saliendo del sistema...")

                self.conexion.close()

                break

            else:

                print("❌ Opción inválida")


# PROGRAMA PRINCIPAL
gestor = GestorEstudiantes()
gestor.ejecutar_menu()