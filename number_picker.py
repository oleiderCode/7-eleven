import customtkinter as tk

class NumberPicker(tk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.value = 0  # Valor inicial

        # Botón -
        self.minus_button = tk.CTkButton(self, text="-", width=40, command=self.decrease)
        self.minus_button.grid(row=0, column=0, padx=5, pady=5)

        # Label editable para el número
        self.number_label = tk.CTkEntry(self, width=50, justify="center")
        self.number_label.insert(0, str(self.value))
        self.number_label.grid(row=0, column=1, padx=5, pady=5)

        # Botón +
        self.plus_button = tk.CTkButton(self, text="+", width=40, command=self.increase)
        self.plus_button.grid(row=0, column=2, padx=5, pady=5)

        # 🔹 Bind para confirmar con Enter y al perder foco
        self.number_label.bind("<Return>", lambda event: self.confirm())  # ⏎ Enter
        self.number_label.bind("<FocusOut>", lambda event: self.confirm())  # 🖱️ Pierde el foco

    def increase(self):
        if self.value < 32:
            self.value += 1
            self.update_value()

    def decrease(self):
        if self.value > 0:
            self.value -= 1
            self.update_value()

    def update_value(self):
        self.number_label.delete(0, tk.END)
        self.number_label.insert(0, str(self.value))

    def confirm(self):
        """Valida y actualiza el valor ingresado."""
        try:
            entered_value = int(self.number_label.get())
        except ValueError:
            entered_value = 0

        # Limitar entre 0 y 32
        self.value = max(0, min(32, entered_value))
        self.update_value()

    def validate_input(self, event=None):
        text = self.number_label.get()
        if text.isdigit():
            num = int(text)
            if 0 <= num <= 32:
                self.value = num
        elif text == "":  # Permitir que quede vacío momentáneamente
            pass
        else:
            self.update_value()
