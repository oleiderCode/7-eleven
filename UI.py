import customtkinter as tk
from datetime_picker import DateTimePicker  # ⬅️ Importa el módulo
from number_picker import NumberPicker

class App(tk.CTk):
    def __init__(self):
        super().__init__()

        self.title("amor me hace trabajar de gratis")
        self.geometry("700x400")
        self.resizable(False, False)

        # **Contenedor principal (para los dos frames)**
        self.main_frame = tk.CTkFrame(self)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # **Frame 1**
        self.frame1 = tk.CTkFrame(self.main_frame, width=300, height=200)
        self.frame1.grid(row=0, column=0, padx=(20, 0), pady=10)
        self.frame1.grid_propagate(False)  # ⬅️ Evita que el tamaño cambie automáticamente


        # **Frame 2**
        self.frame2 = tk.CTkFrame(self.main_frame, width=300, height=200)
        self.frame2.grid(row=0, column=1, padx=(20), pady=10)
        self.frame2.grid_propagate(False)



        # Etiqueta de título
        self.title_label = tk.CTkLabel(self.frame1, text="Entrada", font=("Arial", 20))
        self.title_label.grid(row=0, column=0, pady=(10, 10), padx=(10, 10))

        # 🔹 Input de fecha y hora
        self.date_entry = tk.CTkEntry(self.frame1, placeholder_text="Select Date & Time", width=200)
        self.date_entry.grid(row=0, column=1, pady=10)
        self.date_entry.bind("<Button-1>", self.show_date_picker)  # ⬅️ Mostrar selector al hacer clic

        # 🗓️ Selector de fecha (inicialmente oculto)
        self.date_picker = DateTimePicker(self, self.date_entry)


        # Etiqueta de título Salida
        self.title_label = tk.CTkLabel(self.frame1, text="Salida", font=("Arial", 20))
        self.title_label.grid(row=1, column=0, pady=(10, 10), padx=(10, 10))

        # 🔹 Input de fecha y hora
        self.date_outpost = tk.CTkEntry(self.frame1, placeholder_text="Select Date & Time", width=200)
        self.date_outpost.grid(row=1, column=1, pady=10)
        self.date_outpost.bind("<Button-1>", lambda event: self.show_date_picker(event, outpost=True))


        # Etiqueta de título de numero de tickets
        self.title_label = tk.CTkLabel(self.frame2, text="Nro Tickets", font=("Arial", 20))
        self.title_label.grid(row=0, column=0, pady=(10, 10), padx=(10, 10))

        # 🔢 Agregar NumberPicker directamente dentro del Frame
        self.number_picker2 = NumberPicker(self.frame2)
        self.number_picker2.grid(row=0, column=1, pady=10, padx=10)

        # boton de confirmar datos
        self.confirm_button = tk.CTkButton(self.frame2, text="Confirmar", command=self.show_number_picker)
        self.confirm_button.grid(row=1, column=0, pady=10, padx=10, columnspan=2)

    def show_date_picker(self, event=None, outpost=False):
        """Muestra el selector de fecha y hora debajo del input correspondiente."""
        if outpost:
            self.date_picker.entry_widget = self.date_outpost  
            self.date_picker.place(x=self.date_outpost.winfo_x(), y=self.date_outpost.winfo_y() + 30)
        else:
            self.date_picker.entry_widget = self.date_entry  
            self.date_picker.place(x=self.date_entry.winfo_x(), y=self.date_entry.winfo_y() + 30)
        self.date_picker.lift()

    def show_number_picker(self, event=None):
        """Muestra el selector de número debajo del input correspondiente."""
        self.number_picker2.entry_widget = self.number_entry  # Asegurar que el entry es correcto
        
        # Obtener coordenadas del Entry
        x = self.number_entry.winfo_x()
        y = self.number_entry.winfo_y() + self.number_entry.winfo_height()
        
        self.number_picker2.place(x=x, y=y)  # Colocarlo debajo
        self.number_picker2.lift()  # Traerlo al frente


app = App()
app.mainloop()
