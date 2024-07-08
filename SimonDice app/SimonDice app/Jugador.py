class Jugador:
    def __init__(self, nombre, puntaje, fecha, hora, nivel):
        self.nombre = nombre
        self.puntaje = puntaje
        self.fecha = fecha
        self.hora = hora
        self.nivel = nivel

    def __gt__(self, other):
        return self.puntaje > other.puntaje