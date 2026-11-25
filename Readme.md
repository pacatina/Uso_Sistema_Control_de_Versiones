# MODIFICACION DEL CODIGO

## HU1 – Registro de clientes: 
En esta historia se modifica la clase Cliente, que inicialmente asignaba directamente el nombre y el documento sin realizar validaciones. Se incorpora:
•	Validación del nombre.
•	Validación del documento.
•	Reutilización del constructor de la clase Persona mediante super().
•	Inicialización de la lista de mascotas.
•	Conservación de los métodos para agregar mascotas y consultar el rol del cliente.

*Código inicial:

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

## HU2 – Registro de mascotas: 
En esta historia Se actualizará la clase Mascota para incorporar validaciones en los datos de registro. Se incorpora:
•	Evita registrar mascotas sin nombre y sin especie
•	Impide ingresar edades negativas, pesos negativos o iguales a cero
•	Guarda el nombre, especie, edad y peso de la mascote 
•	Permite consultar los datos de la mascota

Código inicial:

class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso
        
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}, Peso: {self.peso}"

Modificación:

class Mascota:
    def __init__(self, nombre, especie, edad, peso):

        if not nombre.strip():
            raise ValueError(
                "El nombre de la mascota es obligatorio"
            )
        if not especie.strip():
            raise ValueError(
                "La especie de la mascota es obligatoria"
            )
        if edad < 0:
            raise ValueError(
                "La edad no puede ser negativa"
            )
        if peso <= 0:
            raise ValueError(
                "El peso debe ser mayor que cero"
            )
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def mostrar_info(self):
        return (
            f"Nombre: {self.nombre}, "
            f"Especie: {self.especie}, "
            f"Edad: {self.edad}, "
            f"Peso: {self.peso} kg"
        )

Explicación de los Cambios HU2:

if not nombre.strip(): Evita registrar mascotas sin nombre.
if not especie.strip(): Evita registrar mascotas sin especie.
if edad < 0: Impide ingresar edades negativas
if peso <= 0: Impide ingresar pesos negativos o iguales a cero.
self.nombre = nombre: Guarda el nombre de la mascota.
self.especie = especie: Guarda la especie.
self.edad = edad: Guarda la edad.
self.peso = peso: Guarda el peso.
mostrar_info(): Permite consultar los datos de la mascota.

## HU3 – Registro de consulta veterinaria: 
La clase Consulta será mejorada para validar el motivo de atención y mantener organizadas las relaciones con el veterinario y la mascota. Se incorpora:
•	Verifica que el motivo no esté vacío.
•	Relaciona la consulta con el veterinario responsable.
•	Relaciona la consulta con la mascota atendida.
•	Almacena el motivo de atención
•	Inicializa la lista de tratamientos asociados.
•	Inicializa el diagnóstico como texto vacío para su futura actualización
•	Permite consultar la información de la consulta.

Código inicial:

class Consulta:
    def __init__(self, veterinario, mascota, motivo):
        self.mascota = mascota
        self.veterinario = veterinario
        self.motivo = motivo
        self.tratamientos = []
        self.diagnostico = ""

    def crear_tratamiento(self, descripcion, costo):
        tratamiento = Tratamiento(descripcion, costo)
        self.tratamientos.append(tratamiento)

    def total(self):
        return sum(t.costo for t in self.tratamientos)

Modificación:

class Consulta:
    def __init__(self, veterinario, mascota, motivo):
        if not motivo.strip():
            raise ValueError(
                "El motivo de la consulta es obligatorio"
            )
        self.veterinario = veterinario
        self.mascota = mascota
        self.motivo = motivo
        self.tratamientos = []
        self.diagnostico = ""
    def mostrar_consulta(self):
        return (
            f"Veterinario: {self.veterinario.nombre}\n"
            f"Mascota: {self.mascota.nombre}\n"
            f"Motivo: {self.motivo}"
        )
    def crear_tratamiento(self, descripcion, costo):
        tratamiento = Tratamiento(descripcion, costo)
        self.tratamientos.append(tratamiento)
    def total(self):
        return sum(
            tratamiento.costo
            for tratamiento in self.tratamientos
        )

Explicación de los Cambios HU3:

if not motivo.strip(): Verifica que el motivo no esté vacío.
self.veterinario = veterinario: Relaciona la consulta con el veterinario responsable.
self.mascota = mascota: Relaciona la consulta con la mascota atendida.
self.motivo = motivo: Almacena el motivo de atención.
self.tratamientos = []: Inicializa la lista de tratamientos asociados.
self.diagnostico = "": Inicializa el diagnóstico como texto vacío para su futura actualización.
mostrar_consulta(): Permite consultar la información de la consulta.


## HU4– Registro de tratamientos: 
La clase Tratamiento se actualizará para validar la descripción y el costo. Se incorpora:
•	Valida que el tratamiento tenga una descripción.
•	Impide registrar costos negativos.
•	Almacena el nombre o detalle del tratamiento.
•	Almacena el costo del tratamiento.
•	Muestra la descripción y el costo.

Código inicial:

class Tratamiento:
    def __init__(self, descripcion, costo):
        self.descripcion = descripcion
        self.costo = costo
        
    def mostrar_tratamiento(self):
        return f"{self.descripcion} - ${self.costo}"

Modificación: 

class Tratamiento:
    def __init__(self, descripcion, costo):

        if not descripcion.strip():
            raise ValueError(
                "La descripción del tratamiento es obligatoria"
            )
        if costo < 0:
            raise ValueError(
                "El costo no puede ser negativo"
            )
        self.descripcion = descripcion
        self.costo = costo
    def mostrar_tratamiento(self):
        return f"{self.descripcion} - ${self.costo}"
    
Explicación de los Cambios HU4:

if not descripcion.strip(): Valida que el tratamiento tenga una descripción.
if costo < 0: Impide registrar costos negativos.
self.descripcion = descripción: Almacena el nombre o detalle del tratamiento.
self.costo = costo: Almacena el costo del tratamiento.
mostrar_tratamiento(): Muestra la descripción y el costo.

## HU5– Cálculo del valor de la consulta:
En esta historia se mejorará el método total() de la clase Consulta, que ya existía en su código inicial. 
La función sum() permite calcular el total de los valores almacenados en la lista. Si la lista está vacía, retorna cero, por lo que no es necesario crear una condición adicional para la consulta sin tratamientos. Se incorpora:
•	Contiene todos los tratamientos asociados a la consulta.
•	Recorre los tratamientos registrados.
•	Obtiene el costo de cada tratamiento.
•	Suma todos los valores obtenidos.
•	Calcula el valor actual de la consulta.
•	Presenta el total en un mensaje legible.

Código inicial:

class Consulta:
    def __init__(self, veterinario, mascota, motivo):
        if not motivo.strip():
            raise ValueError(
                "El motivo de la consulta es obligatorio"
            )
        self.veterinario = veterinario
        self.mascota = mascota
        self.motivo = motivo
        self.tratamientos = []
        self.diagnostico = ""
    def mostrar_consulta(self):
        return (
            f"Veterinario: {self.veterinario.nombre}\n"
            f"Mascota: {self.mascota.nombre}\n"
            f"Motivo: {self.motivo}"
        )
    def crear_tratamiento(self, descripcion, costo):
        tratamiento = Tratamiento(descripcion, costo)
        self.tratamientos.append(tratamiento)
    def total(self):
        return sum(
            tratamiento.costo
            for tratamiento in self.tratamientos
        )

Modificación:

class Consulta:
    def __init__(self, veterinario, mascota, motivo):
        if not motivo.strip():
            raise ValueError(
                "El motivo de la consulta es obligatorio"
            )
        self.veterinario = veterinario
        self.mascota = mascota
        self.motivo = motivo
        self.tratamientos = []
        self.diagnostico = ""
    def mostrar_consulta(self):
        return (
            f"Veterinario: {self.veterinario.nombre}\n"
            f"Mascota: {self.mascota.nombre}\n"
            f"Motivo: {self.motivo}"
        )
    def crear_tratamiento(self, descripcion, costo):
        tratamiento = Tratamiento(descripcion, costo)
        self.tratamientos.append(tratamiento)
    def total(self):
        return sum(
            tratamiento.costo
            for tratamiento in self.tratamientos
        )
    def mostrar_total(self):
        return f"Total de la consulta: ${self.total()}"

Explicación de los Cambios HU5:

self.tratamientos: Contiene todos los tratamientos asociados a la consulta.
for tratamiento in self.tratamientos: Recorre los tratamientos registrados.
tratamiento.costo: Obtiene el costo de cada tratamiento.
sum(): Suma todos los valores obtenidos.
self.total(): Calcula el valor actual de la consulta.
mostrar_total(): Presenta el total en un mensaje legible





