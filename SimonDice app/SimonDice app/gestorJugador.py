import json
from Jugador import Jugador
class GestorJugadores:
    def __init__(self):
        self.jugadores = [] #lista vacia para almacenar jugadores 
        self.cargar_jugadores()  

    def cargar_jugadores(self):
        try:
            with open('pysimonpuntajes.json', 'r') as f:  #abre el archivo en modo lectura
                data = json.load(f)  #carga los datos del json
                for jugador_data in data:
                     # Crea una instancia de Jugador usando los datos del JSON
                    jugador = Jugador(jugador_data['player'], jugador_data['score'], jugador_data['date'], jugador_data['date'], jugador_data['level'])
                    self.jugadores.append(jugador) #agrega a la lista
                self.jugadores.sort(reverse=True) #ordena la lista orden descendente
        except FileNotFoundError:
            pass

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
        self.jugadores.sort(reverse=True)
        self.guardar_jugadores()

    def guardar_jugadores(self):
        data = []
        for jugador in self.jugadores:
            data.append({
                "player": jugador.nombre,
                "score": jugador.puntaje,
                "date": jugador.fecha,
                "hora": jugador.hora,
                "level": jugador.nivel
            })
        # Abre el archivo 'pysimonpuntajes.json' en modo escritura
        with open('pysimonpuntajes.json', 'w') as f:
            json.dump(data, f, indent=4)