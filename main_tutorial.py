import sys
from PyQt6.QtWidgets import QApplication, QMainWindow # Usamos QMainWindow ahora
from PyQt6 import uic # Importamos el cargador de UI

# 1. Creamos la clase de nuestra ventana
class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Carga el diseño del archivo .ui y lo aplica a esta instancia (self)
        # uic.loadUi('chat_window.ui', self)
        uic.loadUi('chat_test.ui', self)

# 2. Preparamos la aplicación
app = QApplication(sys.argv)

# 3. Creamos la instancia de nuestra ventana personalizada
mi_ventana = ChatWindow()

# 4. Mostrar y ejecutar
mi_ventana.show()
sys.exit(app.exec())