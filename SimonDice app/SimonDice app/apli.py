from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import random
from gestorJugador import GestorJugadores
from Jugador import Jugador
from datetime import datetime
import time


class Apli:  # Inicializa el gestor de jugadores
    def __init__(self,player_name):
        self.gestor_jugadores = GestorJugadores()
        self.score = 0
        self.sequence = []
        self.current_step = 0
        self.level = "Principiante"
        self.colors = ['blue', 'red', 'yellow', 'green']
        self.tiempo_nivel = {"Principiante": 1, "Experto": 0.5, "Super Experto": 0.3}
        self.tiempo_restante = self.tiempo_nivel[self.level]
        self.timer = None
        self.player_name = player_name

        # Configuración de la ventana principal
        self.__ventana = Tk()
        self.__ventana.geometry('300x400')
        self.__ventana.configure(bg='white')
        self.__ventana.title('PySimon-Game')
        
        # Frame para los datos del jugador
        self.frame_datos = Frame(self.__ventana, bg='white')
        self.frame_datos.pack(side=TOP, pady=10)

        # Botón para iniciar el juego
        self.boton_iniciar = ttk.Button(self.frame_datos, text='Iniciar Juego', command=self.iniciar_juego)
        self.boton_iniciar.pack(side=LEFT, padx=10)

        # Frame para mostrar el puntaje y nivel
        self.score_frame = Frame(self.__ventana, bg='white')
        self.score_frame.pack(side=TOP, pady=10)

        # Etiqueta para mostrar el nombre del jugador
        self.score_label = Label(self.score_frame, text=f'{player_name}:', bg='white', fg='red', font=('Arial', 12))
        self.score_label.pack(side=LEFT)

        # Etiqueta para mostrar el puntaje
        self.score_value = Label(self.score_frame, text='0', bg='white', fg='black', font=('Arial', 12))
        self.score_value.pack(side=LEFT)

        # Etiqueta para mostrar el nivel
        self.level_label = Label(self.score_frame, text='Nivel:', bg='white', fg='red', font=('Arial', 12))
        self.level_label.pack(side=LEFT, padx=10)

        # Menú desplegable para seleccionar el nivel
        self.level_var = StringVar()
        self.level_var.set(self.level)
        self.level_menu = ttk.OptionMenu(self.frame_datos, self.level_var, "Principiante", "Experto", "Super Experto", command=self.set_level)
        self.level_menu.pack(side=LEFT, padx=10)

        self.level_value = Label(self.score_frame, text=self.level, bg='white', font=('Arial', 12))
        self.level_value.pack(side=LEFT)

        # Frame para los botones de colores
        self.frame = Frame(self.__ventana, bg='black')
        self.frame.pack(expand=True, pady=10)

        # Configuración de los botones de colores
        colors = ['blue', 'red', 'yellow', 'green']
        self.buttons = []
        button_size = 100
        positions = [(0, 0), (0, 1), (1, 0), (1, 1)]

        for i, (color, pos) in enumerate(zip(colors, positions)):
            canvas = Canvas(self.frame, width=button_size, height=button_size, bg=color)
            canvas.grid(row=pos[0], column=pos[1], padx=5, pady=5)
            canvas.bind("<Button-1>", lambda event, index=i: self.button_clicked(index))
            self.buttons.append(canvas)
        
        # Menú de opciones
        self.menu_bar = Menu(self.__ventana)
        self.__ventana.config(menu=self.menu_bar)

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Opciones", menu=self.file_menu)
        self.file_menu.add_command(label="Ver Puntajes", command=self.mostrar_puntajes)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.__ventana.quit)

        self.__ventana.mainloop()

    def iniciar_juego(self):
        self.comenzar_juego()

    def set_level(self, level):  # Establece el nivel del juego y actualiza el tiempo restante
        self.level = level
        self.tiempo_restante = self.tiempo_nivel[self.level]
        self.update_level()

    def update_level(self): # Actualiza la etiqueta de nivel
        self.level_value.config(text=self.level)

    def comenzar_juego(self):  # Resetea los valores iniciales para empezar el juego
        self.score = 0
        self.sequence = []
        self.current_step = 0
        self.level = "Principiante"
        self.tiempo_restante = self.tiempo_nivel[self.level]
        self.update_score()
        self.update_level()
        self.genera_sequence()
        self.show_sequence()

    def genera_sequence(self):  # Genera una nueva secuencia añadiendo un número aleatorio entre 0 y 3
        self.sequence.append(random.randint(0, 3))

    def show_sequence(self): # Muestra la secuencia de colores a seguir
        self.current_step = 0
        for i in range(len(self.sequence)):
            if i<len(self.sequence):
               self.buttons[self.sequence[i]].config(bg='white')
               self.__ventana.update()
               time.sleep(self.tiempo_nivel[self.level])
               self.buttons[self.sequence[i]].config(bg=self.get_color(self.sequence[i]))
               self.__ventana.update()
        if self.level == "Experto" or self.level == "Super Experto":
            self.start_timer()
    
    def start_timer(self):  # Inicia el temporizador para niveles avanzados
        self.timer = self.__ventana.after(1000, self.check_timer)

    def check_timer(self): # Verifica el tiempo restante y termina el juego si se acaba el tiempo
        self.tiempo_restante -= 1
        if self.tiempo_restante <= 0:
            self.game_over()
        else:
            self.timer = self.__ventana.after(1000, self.check_timer)

    def button_clicked(self, index):  # Verifica si el botón clickeado es el correcto en la secuencia
        if self.current_step < len(self.sequence) and index == self.sequence[self.current_step]:
            self.current_step += 1
            if self.current_step == len(self.sequence):
                self.score += 1
                self.update_score()
                self.genera_sequence()
                self.show_sequence()
        else:
            self.game_over()

    def game_over(self):  # Muestra el mensaje de Game Over y guarda el puntaje
        tkinter.messagebox.showinfo("Game Over", f"Game Over! Puntaje: {self.score}")
        self.guarda_score()
        self.reset_game()

    def guarda_score(self):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        jugador = Jugador(self.player_name, self.score, timestamp, timestamp, self.level)
        self.gestor_jugadores.agregar_jugador(jugador)

    def reset_game(self): # Resetea el juego para una nueva partida
        self.score = 0
        self.sequence = []
        self.current_step = 0
        self.level = "Principiante"
        self.tiempo_restante = self.tiempo_nivel[self.level]
        self.update_score()
        self.update_level()

    def update_score(self):
        self.score_value.config(text=self.score)

    def update_level(self):
        self.level_value.config(text=self.level)

    def get_color(self, index):
        colors = ['blue', 'red', 'yellow', 'green']
        return colors[index]

    
    def mostrar_puntajes(self):
        # Muestra la ventana de puntajes
        top = tkinter.Toplevel(self.__ventana)
        top.title("Puntajes")

        frame = tkinter.Frame(top, padx=10, pady=10, bg='white')
        frame.pack(pady=10)

        label = tkinter.Label(frame, text="Galería de Puntajes", font=('Arial', 12), bg='white')
        label.pack(pady=10)

        columns = ('Jugador', 'Fecha', 'Hora', 'Puntaje')
        tree = ttk.Treeview(frame, columns=columns, show='headings')

        # Definir los encabezados
        tree.heading('Jugador', text='Jugador')
        tree.heading('Fecha', text='Fecha')
        tree.heading('Hora', text='Hora')
        tree.heading('Puntaje', text='Puntaje')

        # Ajustar el tamaño de las columnas
        tree.column('Jugador', width=100, anchor='center')
        tree.column('Fecha', width=100, anchor='w')  # Align left
        tree.column('Hora', width=100, anchor='w')   # Align left
        tree.column('Puntaje', width=100, anchor='center')

        # Agregar los datos
        for jugador in self.gestor_jugadores.jugadores:
            tree.insert('', tkinter.END, values=(jugador.nombre, jugador.fecha, jugador.hora, jugador.puntaje))

        tree.pack(pady=5)

        scrollbar = tkinter.Scrollbar(frame, orient=tkinter.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        cerrar_btn = tkinter.Button(frame, text="Cerrar", command=top.destroy)
        cerrar_btn.pack(pady=5)

