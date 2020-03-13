from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui import Ui_Form

# Create application
app = QtWidgets.QApplication(sys.argv)

# Create form and init UI
Form = QtWidgets.QDialog()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

# Hook logic



# Run main loop
sys.exit(app.exec_())