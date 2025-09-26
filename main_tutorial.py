import sys
from PyQt6.QtWidgets import QApplication, QWidget

# 1. Preparar la aplicación
app = QApplication(sys.argv)

# 2. Crear la ventana (el widget principal)
mi_ventana = QWidget()
mi_ventana.setWindowTitle("Mi Primera GUI PyQt6") # Puedes añadir esto para darle título

# 3. Mostrar la ventana
mi_ventana.show()

# 4. Iniciar el bucle de eventos y esperar que el usuario interactúe
sys.exit(app.exec())