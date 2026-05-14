class cafetera:
    def preparar_cafe(self):
        self.__hervir_agua()
        self.__moler_cafe()
        print("cafe listo!")

    def __hervir_agua(self):
        print("hirviendo el agua")
    
    def __moler_cafe(self):
        print("moliendo el cafe")

def main():
    mi_cafetera = cafetera()
    mi_cafetera.preparar_cafe()

if __name__ == "__main__":
    main()