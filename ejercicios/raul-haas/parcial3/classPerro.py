class Perro:
    #Atributos de la clase Perro
    especie = "Canis lupus familiaris"

    #Constructor de la clase Perro
    def __init__(self, nombre, raza = "Caramelo", edad= 0):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    #Método para imprimir los datos del perro
    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print(f"Especie: {self.especie}")

def main():
    #Creación de un objeto de la clase Perro
    perro1 = Perro("Firulais", "Labrador", 5)
    perro1.imprimir_datos()
    perro2 = Perro("Rex", "Pastor Alemán", 3)
    perro2.imprimir_datos() 
    print("Información del perro 2:", perro2.nombre, perro2.raza, perro2.edad)
    perro3 = Perro("Luna", "Golden Retriever", 2)
    perro3.imprimir_datos()
    perro4 = Perro("Dante")
    perro4.edad = 4
    perro4.imprimir_datos()
    perro2.raza = "Pastor Belga"
    perro2.imprimir_datos()
    perro5 = Perro("Raya", "Siames", 1)
    perro5.especie = "Felis catus"
    perro5.imprimir_datos()


if __name__ == "__main__":
    main()