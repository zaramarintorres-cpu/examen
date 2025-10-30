from datetime import date

class Persona:
    def _init_(self, nombre: str, nif: str, fecha_nac: date):
        self.nombre = nombre
        self.nif = nif
        self.fecha_nac = fecha_nac

class Jugador(Persona):
    def _init_(self, nombre: str, nif: str, fecha_nac: date, num_fed: int):
        super()._init_(nombre, nif, fecha_nac)
        self.num_fed = num_fed