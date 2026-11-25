# MODIFICACION DEL CODIGO

HU1 – Registro de clientes: En esta historia se modifica la clase Cliente, que inicialmente asignaba directamente el nombre y el documento sin realizar validaciones. Se incorpora:
•	Validación del nombre.
•	Validación del documento.
•	Reutilización del constructor de la clase Persona mediante super().
•	Inicialización de la lista de mascotas.
•	Conservación de los métodos para agregar mascotas y consultar el rol del cliente.

Código inicial:

class Cliente(Persona):
    def __init__(self, nombre, documento):
        super().__init__(nombre, documento)
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_rol(self):
        return f"Cliente {self.nombre}"

Modificación:

class Cliente(Persona):
    def __init__(self, nombre, documento):

        if not nombre.strip():
            raise ValueError(
                "El nombre del cliente no puede estar vacío"
            )

        if not documento.strip():
            raise ValueError(
                "El documento del cliente es obligatorio"
            )

        super().__init__(nombre, documento)
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_rol(self):
        return f"Cliente {self.nombre}"

Explicación de los Cambios HU1:

* if not nombre.strip(): Comprueba que el nombre no este vacío ni contenga solamente espacios
* raise ValueError: Genera un error cuando se suministra un dato invalido
* super().__init__(nombre, documento): Llama al constructor de persona y reutiliza los atributos 
* self.mascotas = []: Inicializa una lista para asociar mascotas al cliente
* def agregar_mascota(self, mascota): Permite agregar mascotas a la lista del cliente
* def mostrar_rol(self): Retorna el nombre del cliente precedido por su rol



