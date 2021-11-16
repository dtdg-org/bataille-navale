from tkinter import Frame, Label, Button


# Main menu screen
class HomeView(Frame):
    def __init__(self, controller, **kw):
        super().__init__(**kw)
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

        self.main_menu_label = Label(self, text='Battleship')
        self.main_menu_label.grid(row=0, column=0, sticky="ew")

        self.new_game_button = Button(self, text='New game', command=controller.load_place_ship_view)
        self.new_game_button.grid(row=1, column=0, sticky="ew")

        self.quit_button = Button(self, text="Quit", command=self.quit)
        self.quit_button.grid(row=2, column=0, sticky="ew")

    def show(self):
        self.tkraise()
