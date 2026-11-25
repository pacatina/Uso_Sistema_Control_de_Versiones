from abc import ABC, abstractmethod

# CLASE PADRE PERSONA (ABSTRACTA)
class Persona(ABC):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_rol(self):
        pass

class Veterinario(Persona):
    def mostrar_rol(self):
        return f"Veterinario {self.nombre}"

class Recepcionista(Persona):
    def mostrar_rol(self):
        return f"Recepcionista {self.nombre}"
    
    def atender_mascota(self):
        return f"{self.nombre} está atendiendo a una mascota."

# CLIENTES
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

# MASCOTAS
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

#CONSULTAS        
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
    
# TRATAMIENTO
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
    
# FACTURA
class Factura:
    def __init__(self, consulta, metodo_pago):
        self.consulta = consulta
        self.metodo_pago = metodo_pago

    def calcular_total(self):
        total = self.consulta.total()
        self.metodo_pago.procesar_pago(total)
        return total
        
# PRUEBA DEL SISTEMA
if __name__ == "__main__":
    # 1. Crear cliente
    cliente = Cliente("Esperanza", "6235")
    print(cliente.mostrar_rol())
    
    # PRUEBAS HISTORIA 1
    print("\n--- PRUEBAS HU1: REGISTRO DE CLIENTES ---")

    # Prueba 1: registrar un cliente correctamente
    cliente_prueba = Cliente("Carlos", "12345")

    print("Cliente registrado:", cliente_prueba.mostrar_rol())
    print("Documento:", cliente_prueba.documento)
        
    # Prueba 2: validar nombre vacío
    try:
        Cliente("", "12345")
    except ValueError as error:
        print("Validación de nombre:", error)

    # Prueba 3: validar documento vacío
    try:
        Cliente("Carlos", "")
    except ValueError as error:
        print("Validación de documento:", error)

    # 2. Registrar dos mascotas
    masc1 = Mascota("Luna", "Perro", 5, 10)
    masc2 = Mascota("Tin", "Gato", 3, 4)

    cliente.agregar_mascota(masc1)
    cliente.agregar_mascota(masc2)

    print("\nMascotas del cliente:")
    for esp in cliente.mascotas:
        print(esp.mostrar_info())
        
    # PRUEBAS HISTORIA 2
    print("\n--- PRUEBAS HU2: REGISTRO DE MASCOTAS ---")

    # Prueba 1: crear dos mascotas
    mascota1 = Mascota("Luna", "Perro", 5, 10)
    mascota2 = Mascota("Tin", "Gato", 3, 4)

    # Prueba 2: asociar las mascotas al cliente
    cliente_prueba.agregar_mascota(mascota1)
    cliente_prueba.agregar_mascota(mascota2)

    print("Cliente:", cliente_prueba.nombre)
    print("Cantidad de mascotas:", len(cliente_prueba.mascotas))

    for mascota in cliente_prueba.mascotas:
        print("Mascota:", mascota.nombre, "-", mascota.especie)
    
    # 3. Crear veterinario
    vete = Veterinario("Dr. Marcos", "015")
    print("\n" + vete.mostrar_rol())
    
    # 4. Veterinario atiende una mascota
    print(f"{vete.nombre} atiende a {masc1.nombre}")

    # 5. Crear consulta
    consulta = Consulta(vete, masc1, "Revision periodica anual")
    
    # PRUEBAS HISTORIA 3
    print("\n--- PRUEBAS HU3: REGISTRO DE CONSULTAS ---")

    # Crear veterinario para la prueba
    veterinario_prueba = Veterinario("Dr. Marcos", "015")

    # Crear consulta para la mascota Luna
    consulta_prueba = Consulta(
        veterinario_prueba,
        mascota1,
        "Revisión anual"
    )
    print("Veterinario:", consulta_prueba.veterinario.nombre)
    print("Mascota:", consulta_prueba.mascota.nombre)
    print("Motivo:", consulta_prueba.motivo)
    
    # 6. Crear tratamientos
    consulta.crear_tratamiento("Vacuna", 50)
    consulta.crear_tratamiento("Desparasitación", 30)

    print("\nTratamientos:")
    for trat in consulta.tratamientos:
        print(trat.mostrar_tratamiento())
        
    # PRUEBAS HISTORIA 4
    print("\n--- PRUEBAS HU4: REGISTRO DE TRATAMIENTOS ---")

    # Crear y agregar tratamientos a la consulta
    consulta_prueba.crear_tratamiento("Vacunación", 50)
    consulta_prueba.crear_tratamiento("Desparasitación", 30)

    # Mostrar tratamientos registrados
    for tratamiento in consulta_prueba.tratamientos:
        print(
            "Tratamiento:",
            tratamiento.descripcion,
            "- Costo: $",
            tratamiento.costo
        )

    # 7. Calcular total
    total = consulta.total()
    print(consulta.mostrar_total())
    
    # PRUEBAS HISTORIA 5
    print("\n--- PRUEBAS HU5: CALCULO DEL TOTAL ---")

    # Prueba 1: sumar los tratamientos registrados
    print("Total de la consulta:", consulta_prueba.total())

    # Prueba 2: agregar un nuevo tratamiento
    consulta_prueba.crear_tratamiento("Curación", 20)

    print("Total actualizado:", consulta_prueba.total())

    # Prueba 3: consulta sin tratamientos
    consulta_vacia = Consulta(
        veterinario_prueba,
        mascota2,
        "Consulta de valoración"
    )
    print("Total sin tratamientos:", consulta_vacia.total())
    
   
