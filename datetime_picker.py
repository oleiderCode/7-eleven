import customtkinter as tk
from tkcalendar import Calendar
from tkinter import ttk

class DateTimePicker(tk.CTkFrame):
    def __init__(self, parent, entry_widget, *args, **kwargs):
        super().__init__(parent, fg_color="white", corner_radius=5, *args, **kwargs)
        self.entry_widget = entry_widget

        # 🔥 Ajuste del tamaño de fuente en el menú desplegable
        self.option_add('*TCombobox*Listbox.font', ("Arial", 14))  # ⬅️ Agranda el texto del menú de horas

        # 🔹 Estilos del calendario y combobox
        style = ttk.Style()
        style.configure("TCalendar", font=("Arial", 16))  # ⬅️ Tamaño del texto del calendario
        style.configure("TCombobox", font=("Arial", 14))  # ⬅️ Aumenta el tamaño del campo de selección

        # 📅 Calendario
        self.calendar = Calendar(
            self, 
            selectmode="day", 
            date_pattern="yyyy-mm-dd",
            font=("Arial", 14)  # ⬅️ Aumenta el tamaño de los números de los días
        )
        self.calendar.pack(pady=5)

        # ⏰ Selector de hora
        self.hour_picker = ttk.Combobox(
            self, 
            values=[f"{h:02d}:00" for h in range(24)], 
            state="readonly",
            font=("Arial", 14)  # ⬅️ Aumenta el tamaño del selector de horas
        )
        self.hour_picker.current(0)
        self.hour_picker.pack(pady=5)

        # ✅ Botón de confirmación
        self.confirm_button = tk.CTkButton(self, text="Confirm", command=self.set_date)
        self.confirm_button.pack(pady=5)

    def set_date(self):
        """Obtiene la fecha y hora seleccionadas y las coloca en el input."""
        selected_date = self.calendar.get_date()
        selected_time = self.hour_picker.get()
        self.entry_widget.delete(0, tk.END)
        self.entry_widget.insert(0, f"{selected_date} {selected_time}")
        self.place_forget()  # Oculta el widget después de seleccionar
