import customtkinter as tk
from datetime_picker import DateTimePicker  # ⬅️ Importa el módulo
from number_picker import NumberPicker
from tkinter import filedialog
from pdf_generator import PDFGenerator

tk.set_appearance_mode("dark")  # "dark", "light" o "system"


class App(tk.CTk):
    def __init__(self):
        super().__init__()

        self.title("o7")
        self.geometry("650x400")  # Aumentar tamaño para más secciones
        self.resizable(False, False)


        self.sections_count = 0  # Contador de secciones añadidas
        self.sections = []  # 🔹 Lista para almacenar las secciones

        # **Contenedor principal (para los frames)**
        self.main_frame = tk.CTkFrame(self)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # **Botón para agregar más secciones**
        # self.add_button = tk.CTkButton(self, text="Añadir Sección", command=self.add_section)
        # self.add_button.pack(pady=10)

        # **Primera sección**
        self.create_section()
        self.create_section()

        # Botón de Confirmar
        self.confirm_button = tk.CTkButton(self, text="Confirmar", command=self.save_pdf_dialog)
        self.confirm_button.pack(pady=10)



    def create_section(self):
        if self.sections_count > 2:
            return 0

        self.sections_count += 1

        """Crea un nuevo frame de sección con entrada de fecha y número."""
        
        # Contenedor de los dos frames
        section_container = tk.CTkFrame(self.main_frame)
        section_container.pack(pady=10, padx=10, fill="x")

        # 🔹 Frame de fechas (Izquierda)
        frame = tk.CTkFrame(section_container, width=290, height=150)
        frame.grid(row=0, column=0, padx=5, pady=5)

        # 🔹 Frame de número de tickets (Derecha)
        frame2 = tk.CTkFrame(section_container, width=290, height=150)
        frame2.grid(row=0, column=1, padx=5, pady=5)

        # 🔹 Entrada de fecha y hora de entrada
        tk.CTkLabel(frame, text="Entrada", font=("Arial", 16)).grid(row=0, column=0, pady=5, padx=10)
        date_entry = tk.CTkEntry(frame, placeholder_text="Seleccionar fecha y hora", width=200)
        date_entry.grid(row=0, column=1, pady=5)
        date_entry.bind("<Button-1>", lambda event: self.show_date_picker(event, date_entry))

        # 🔹 Entrada de fecha y hora de salida
        tk.CTkLabel(frame, text="Salida", font=("Arial", 16)).grid(row=1, column=0, pady=5, padx=10)
        date_outpost = tk.CTkEntry(frame, placeholder_text="Seleccionar fecha y hora", width=200)
        date_outpost.grid(row=1, column=1, pady=5)
        date_outpost.bind("<Button-1>", lambda event: self.show_date_picker(event, date_outpost))

        # 🔢 Selector de número de tickets
        tk.CTkLabel(frame2, text="Nro Tickets", font=("Arial", 16)).grid(row=0, column=0, pady=5, padx=10)
        number_picker = NumberPicker(frame2)
        number_picker.grid(row=0, column=1, pady=5, padx=10)

        # 🔹 Guardamos la referencia de la sección
        self.sections.append({"entrada": date_entry, "salida": date_outpost, "tickets": number_picker})
        return section_container



    def show_date_picker(self, event, entry_widget):
        """Muestra el selector de fecha y hora debajo del input correspondiente."""
        self.date_picker = DateTimePicker(self, entry_widget)
        #widget en el centro del frame principal (self)
        self.date_picker.place(x=self.winfo_width() / 2, y=self.winfo_height() / 2, anchor="center")
        # self.date_picker.place(anchor="center")
        self.date_picker.lift()

    def save_pdf_dialog(self):
        data = self.get_date_picker()
        """Abre un cuadro de diálogo para seleccionar dónde guardar el PDF."""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="Guardar como"
        )

        if file_path:
            pdf_gen = PDFGenerator(file_path)  # ✅ Crear instancia de PDFGenerator
            fechas = pdf_gen.generate_dates(data)  # ✅ Generar fechas
            pdf_gen.create_pdf(fechas)  # ✅ Crear PDF
            print(f"📄 PDF guardado en: {file_path}, con las fechas {fechas}")

    def get_date_picker(self):
        """Obtiene y muestra los datos ingresados en cada sección.
        📅 Ejemplo de fechas
        dates = {
            1: {"Entrada: 2025-03-25 00:00", "Salida: 2025-03-25 00:00", tickets: 1},
            2: {"Entrada: 2025-03-25 00:00", "Salida: 2025-03-25 00:00", tickets: 1},
        }
        """
        dates = {}
        for i, section in enumerate(self.sections):
            entrada = section["entrada"].get().strip() or ""  # Evita valores None
            salida = section["salida"].get().strip() or ""
            tickets = section["tickets"].value if hasattr(section["tickets"], "value") else 0  # Asegura que haya un valor
            dates[i] = (entrada, salida, tickets)
        print(dates)

        return dates

        # for i, section in enumerate(self.sections):
        #     entrada = section["entrada"].get()
        #     salida = section["salida"].get()
        #     tickets = section["tickets"].value  # Obtener el valor del NumberPicker

        #     print(f"Sección {i+1}:")
        #     print(f"  - Entrada: {entrada}")
        #     print(f"  - Salida: {salida}")
        #     print(f"  - Tickets: {tickets}")
        #     print("-------------")
    
    
# Ejecutar la aplicación
app = App()
app.mainloop()
