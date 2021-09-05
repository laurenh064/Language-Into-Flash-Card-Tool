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

    def on_export(self) -> None:
        '''Exports Table as CSV'''
        path = QFileDialog.getSaveFileName(
            self, 'Export CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            with open(path[0], 'w', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file, delimiter=';')
                for row in range(self.table.rowCount()):
                    row_data = []
                    for column in range(self.table.columnCount()):
                        item = self.table.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)
