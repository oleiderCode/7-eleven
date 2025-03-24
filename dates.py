from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

# Configuración de la tabla
cols = 8
rows = 8
cell_width = (5.2/2) * cm
cell_height = 3.2 * cm
margin_left = 0.1 * cm  # Margen izquierdo
margin_top = 1.2 * cm   # Margen superior desde el borde superior

# Tamaño de la página en puntos
page_width, page_height = letter
start_x = margin_left
start_y = page_height - margin_top  # Ajustar según el margen superior

# Generar fechas de ejemplo
from datetime import datetime, timedelta

fecha_inicio = datetime(2025, 3, 15)
fechas = [(fecha_inicio + timedelta(days=i), fecha_inicio + timedelta(days=i+2)) for i in range(rows * cols)]

# Crear PDF
pdf_filename = "cuadricula.pdf"
c = canvas.Canvas(pdf_filename, pagesize=letter)

for row in range(rows):
    for col in range(cols):
        x = start_x + col * cell_width
        y = start_y - row * cell_height

        # Dibujar el rectángulo de la celda
        c.rect(x, y - cell_height, cell_width, cell_height)
        
        # Tamaño de la letra
        c.setFont("Helvetica", 7)

        # Obtener fechas para la celda
        entrada, salida = fechas[row * cols + col]
        texto_entrada = f"Entrada: {entrada.strftime('%d/%m/%Y')}"
        texto_salida = f"Salida: {salida.strftime('%d/%m/%Y')}"

        # Guardar el estado del canvas para rotar el texto
        c.saveState()
        c.translate(x + cell_width / 2, y - cell_height / 2)
        c.rotate(90)

        # Dibujar cada línea de texto con espaciado
        c.drawCentredString(0, 10, texto_entrada)
        c.drawCentredString(0, -10, texto_salida)

        c.restoreState()

# Guardar el PDF
c.save()
print(f"PDF generado: {pdf_filename}")
