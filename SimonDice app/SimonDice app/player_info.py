from tkinter import *
from tkinter import ttk
from apli import Apli

# ventana inicial donde guardamos el nombre del jugador

class PlayerInfo:
    def __init__(self):
        #ventana principal para datos del jugador
        self.__ventana = Tk()
        self.__ventana.geometry('250x200')
        self.__ventana.configure(bg='white')
        self.__ventana.title('Datos del Jugador')
        
         # Crear y empaquetar el título
        self.label_title = Label(self.__ventana, text='Datos del jugador', bg='white', font=('Arial', 12))
        self.label_title.pack(pady=10)
        
         # Crear y empaquetar la etiqueta para el nombre del jugador
        self.label_player = Label(self.__ventana, text='Jugador', bg='white',fg='red', font=('Arial', 10))
        self.label_player.pack(pady=5)
        
        # Crear y empaquetar la entrada de texto para el nombre del jugador
        self.player_name = StringVar()
        self.entry_player = Entry(self.__ventana, textvariable=self.player_name)
        self.entry_player.pack(pady=5)

        # Crear y empaquetar el botón para iniciar el juego
        self.start_button = ttk.Button(self.__ventana, text='Iniciar Juego', command=self.comenzar_juego)
        self.start_button.pack(pady=10)

        self.__ventana.mainloop()

    def comenzar_juego(self):
        # Obtener el nombre del jugador desde la entrada de texto
        player_name = self.player_name.get()
        if player_name:
            # Si hay un nombre de jugador, cierra la ventana actual y abre la ventana del juego
            self.__ventana.destroy()
            Apl2(player_name)
        else:
            # Si no hay nombre de jugador, imprimir un mensaje en la consola
            print("Por favor, ingrese un nombre de jugador.")

class Apl2(Apli):
    def __init__(self, player_name):   # Inicializar la clase Apli con el nombre del jugador
        super().__init__(player_name)
        self.player_name = player_name

if __name__ == '__main__':
    player_info = PlayerInfo()