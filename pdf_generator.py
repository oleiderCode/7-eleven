from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from datetime import datetime, timedelta

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

    def generate_dates(self):
        """Genera fechas de entrada y salida de ejemplo."""
        fecha_inicio = datetime(2025, 3, 15)
        return [(fecha_inicio + timedelta(days=i), fecha_inicio + timedelta(days=i+2)) for i in range(self.rows * self.cols)]

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

                entrada, salida = fechas[row * self.cols + col]
                texto_entrada = f"Entrada: {entrada.strftime('%d/%m/%Y')}"
                texto_salida = f"Salida: {salida.strftime('%d/%m/%Y')}"

                c.saveState()
                c.translate(x + self.cell_width / 2, y - self.cell_height / 2)
                c.rotate(90)

                c.drawCentredString(0, 10, texto_entrada)
                c.drawCentredString(0, -10, texto_salida)

                c.restoreState()

        c.save()
        print(f"📄 PDF generado: {self.filename}")
