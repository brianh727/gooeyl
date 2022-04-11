import sys

from PyQt5.QtCore import Qt, QFile
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QHBoxLayout, QLabel, 
                             QMainWindow, QToolBar, QVBoxLayout, QWidget,
                             QTabWidget, QTableWidget, QAbstractItemView)


class Main(QMainWindow):
    """Create the main window that has all the widgets"""

    def __init__(self):
        """Initialize the settings of the main window"""
        super().__init__()
        self.resize(800, 600)
        self.setFixedSize(self.size())
        self.setWindowTitle("Shopping List")

        self.main_ui()
        self.show()

        self.create_table()
    
    def create_shopping_list():
        self.shopping_list = QTableWidget()
        self.shopping_list.setColumnCount(3)
        self.shopping_list.setRowCount(6)


def main():
    """Opens the main window"""
    application = QApplication(sys.argv)
    window = SdvHelper()
    sys.exit(application.exec_())

if __name__ == "__main__":
    main()