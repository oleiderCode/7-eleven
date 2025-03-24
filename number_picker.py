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
        self.number_label.bind("<KeyRelease>", self.validate_input)

        # Botón +
        self.plus_button = tk.CTkButton(self, text="+", width=40, command=self.increase)
        self.plus_button.grid(row=0, column=2, padx=5, pady=5)

        # Botón Confirmar ✔
        # self.confirm_button = tk.CTkButton(self, text="✔", width=50, command=self.confirm)
        # self.confirm_button.grid(row=0, column=3, padx=5, pady=5)

    def increase(self):
        if self.value < 64:
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
        try:
            entered_value = int(self.number_label.get())
        except ValueError:
            entered_value = 0

        if entered_value > 64:
            entered_value = 64
        elif entered_value < 0:
            entered_value = 0

        self.value = entered_value
        self.update_value()

    def validate_input(self, event=None):
        text = self.number_label.get()
        if text.isdigit():
            num = int(text)
            if 0 <= num <= 64:
                self.value = num
        elif text == "":
            pass
        else:
            self.update_value()


