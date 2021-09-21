from ui.table_view import TableView
from PyQt5.QtWidgets import *
import os
import csv


class LeftPanel(QWidget):
    def __init__(self, parent):
        super(LeftPanel, self).__init__(parent)
        self._ui()

    def _ui(self) -> None:
        '''
        Returns a panel with table and add, delete buttons
        '''
        grid = QGridLayout(self)
        # Create table, buttons
        self.table = TableView(self)
        self.table.setObjectName('table')
        add_button = QPushButton('&Add')
        add_button.setObjectName('add_button')
        delete_button = QPushButton('&Delete')
        delete_button.setObjectName('delete_button')
        export_button = QPushButton('&Export')
        export_button.setObjectName('export_button')

        # Add to layout
        grid.addWidget(self.table, 0, 0, 1, 2)
        grid.addWidget(add_button, 1, 0, 1, 1)
        grid.addWidget(delete_button, 1, 1, 1, 1)
        grid.addWidget(export_button, 2, 0, 1, 2)

