class Perro:
    # Atributo de la clase perro
    especie = "canis Lups familiaris"
    #constructor de la clase perro
    def __init__(self, nombre, raza = "caramelo", edad = 0):
        self.nombre =nombre
        self.raza =raza
        self.edad =edad
    
    #metodo para imprimir los datos del perro
    def imprimirDatos(self):
        print("nombre: ",self.nombre)
        print("raza: ",self.raza)
        print("edad: ",self.edad)
        print("especie: ",self.especie)
def main():
    #crear un objeto de la clase perro
    perro1 = Perro("firulais", "labrador", 5)
    perro1.imprimirDatos()
    perro2 = Perro("Rex", "Pastor Aleman", 3)
    perro2.imprimirDatos()
    print("informacion del perro 2: ",perro2.nombre,perro2.raza,perro2.edad)
    perro3 = Perro("max", "Bulldog", 2)
    perro3.imprimirDatos()
    perro4 = Perro("Dante",)
    perro4.edad = 4
    perro4.imprimirDatos()
    perro2.raza = "pastor Belga"
    perro2.imprimirDatos()
    perro5 = Perro("Raya", "siames", 1)
    perro5.especie = "Felis catus"
    perro5.imprimirDatos()

if __name__ == "__main__":
    main()