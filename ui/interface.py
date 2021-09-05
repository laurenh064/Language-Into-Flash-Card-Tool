from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
import csv

'''Import ui'''
from ui.text_view import TextView
from ui.right_panel import RightPanel
from ui.left_panel import LeftPanel
from ui.table_view import TableView


class Interface(QMainWindow):
    def __init__(self, app) -> None:
        QMainWindow.__init__(self)
        self.app = app
        self.setMinimumSize(900, 800)
        self.showMaximized()

        self._initUI()
        self.connect_buttons()

    def _initUI(self) -> None:
        self.splitter = QSplitter(self)
        self.splitter.setHandleWidth(1)
        self.splitter.setSizes([300, 300])
        self.splitter.setChildrenCollapsible(False)

        left_panel = LeftPanel(self.splitter)
        right_panel = RightPanel(self.splitter)

        self.add_butt = left_panel.findChild(QPushButton, 'add_button')
        self.del_butt = left_panel.findChild(QPushButton, 'delete_button')
        self.export_butt = left_panel.findChild(QPushButton, 'export_button')
        self.table = left_panel.findChild(TableView, 'table')
        self.text_box = right_panel.findChild(TextView, 'text')

        self.setCentralWidget(self.splitter)

    def connect_buttons(self):

        # Add button
        self.add_butt.clicked.connect(
            lambda: self.table.add_row(self.text_box))
        # Delete button
        self.del_butt.clicked.connect(
            lambda: self.table.delete_row(self.text_box))
        # Export button
        self.export_butt.clicked.connect(lambda: self.export(self.table))

    def export(self, table: TableView):
        '''Exports Table as CSV'''
        path = QFileDialog.getSaveFileName(
            self, 'Export CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            with open(path[0], 'w', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file, delimiter=';')
                for row in range(table.rowCount()):
                    row_data = []
                    for column in range(table.columnCount()):
                        item = table.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)
