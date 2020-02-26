class AirCondition():
    modelo = None
    potencia = None
    marca = None
    color = None
    estado = False

    def __init__(self, modelo, potencia, marca, color):  # Constructor
        self.modelo = modelo
        self.potencia = potencia
        self.marca = marca
        self.color = color

    def interruptor(self):
        if self.estado == False:
            self.estado = True
            print("Encendido")
        else:
            self.estado=False
            print("Apagado")


aire1 = AirCondition("2020", "16000 BTU", "LG", "Blanco")
aire1.interruptor()

