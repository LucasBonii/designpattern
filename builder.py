from abc import abstractmethod


class Carro:
    def __init__(self):
        self.partes = []

    def add_parte(self, part):
        self.partes.append(part)

    def show(self):
        print("Partes:", ", ".join(self.partes))

class Builder:
    @abstractmethod
    def add_motor(self):
        pass

    @abstractmethod
    def add_roda(self):
        pass

    @abstractmethod
    def add_chassi(self):
        pass

    @abstractmethod
    def add_teto_solar(self):
        pass

    @abstractmethod
    def get_car(self):
        pass


class CarroBuilder(Builder):
    def __init__(self):
        self.carro = Carro()

    def reset(self):
        self.carro = Carro()  

    def add_motor(self):
        self.carro.add_parte("Motor")

    def add_roda(self):
        self.carro.add_parte("Roda")

    def add_chassi(self):
        self.carro.add_parte("Chassi")

    def add_teto_solar(self):
        self.carro.add_parte("Teto solar")

    def get_car(self):
        return self.carro


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construcao_carro_comum(self):
        self.builder.reset()
        self.builder.add_chassi()
        self.builder.add_motor()
        self.builder.add_roda()

    def construcao_carro_esportivo(self):
        self.builder.reset()
        self.builder.add_chassi()
        self.builder.add_motor()
        self.builder.add_roda()
        self.builder.add_teto_solar()
    


builder = CarroBuilder()
director = Director(builder)
director.construcao_carro_comum()
carro1 = builder.get_car()
carro1.show()
director.construcao_carro_esportivo()
carro2 = builder.get_car()
carro2.show()