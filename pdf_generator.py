from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from datetime import datetime

class PDFGenerator:
    def __init__(self, filename):
        """Inicializa el generador de PDF con el nombre de archivo."""
        self.filename = filename
        self.cols = 8
        self.rows = 8
        self.cell_width = (5.2 / 2) * cm
        self.cell_height = 3.2 * cm
        self.margin_left = 0.1 * cm
        self.margin_top = 1.2 * cm
        self.page_width, self.page_height = letter

    def generate_dates(self, dates):
        """Genera una lista de fechas según la cantidad de tickets especificados.

        📅 Ejemplo de entrada:
        {
            0: ('2025-03-25 00:00', '2025-03-26 00:00', 3),  # Se repetirá en 3 celdas
            1: ('2025-03-27 00:00', '2025-03-28 00:00', 2),  # Se repetirá en 2 celdas
        }

        📅 Salida esperada (lista con longitud igual a filas * columnas):
        [
            ('2025-03-25 00:00', '2025-03-26 00:00'), 
            ('2025-03-25 00:00', '2025-03-26 00:00'), 
            ('2025-03-25 00:00', '2025-03-26 00:00'), 
            ('2025-03-27 00:00', '2025-03-28 00:00'), 
            ('2025-03-27 00:00', '2025-03-28 00:00')
            ...
        ]
        """
        fechas = []
        total_celdas = self.rows * self.cols
        index = 0

        for i in range(total_celdas):
            if index in dates:
                entrada, salida, tickets = dates[index]
                for _ in range(tickets):
                    if len(fechas) < total_celdas:
                        fechas.append((entrada, salida))
                index += 1
            else:
                # fechas.append((None, None))
                #no agregar celdas vacías
                pass

        return fechas

    def create_pdf(self, fechas):
        """Crea el PDF con la cuadrícula de fechas."""
        c = canvas.Canvas(self.filename, pagesize=letter)
        start_x = self.margin_left
        start_y = self.page_height - self.margin_top

        for row in range(self.rows):
            for col in range(self.cols):
                x = start_x + col * self.cell_width
                y = start_y - row * self.cell_height

                c.rect(x, y - self.cell_height, self.cell_width, self.cell_height)  # Dibujar celda
                c.setFont("Helvetica", 7)

                # Obtener datos de la celda actual
                index = row * self.cols + col
                if index < len(fechas):
                    entrada, salida = fechas[index]

                    if isinstance(entrada, str):
                        try:
                            entrada = datetime.strptime(entrada, "%Y-%m-%d %H:%M")
                        except ValueError:
                            pass  

                    if isinstance(salida, str):
                        try:
                            salida = datetime.strptime(salida, "%Y-%m-%d %H:%M")
                        except ValueError:
                            pass  

                    texto_entrada = f"Entrada: {entrada.strftime('%d/%m/%Y')}" if isinstance(entrada, datetime) else f"Entrada: {entrada}"
                    texto_salida = f"Salida: {salida.strftime('%d/%m/%Y')}" if isinstance(salida, datetime) else f"Salida: {salida}"

                    c.saveState()
                    c.translate(x + self.cell_width / 2, y - self.cell_height / 2)
                    c.rotate(90)

                    c.drawCentredString(0, 10, texto_entrada)
                    c.drawCentredString(0, -10, texto_salida)

                    c.restoreState()

        c.save()
        print(f"📄 PDF generado: {self.filename}")
