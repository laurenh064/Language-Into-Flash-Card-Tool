from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QAbstractScrollArea, QTableWidget
from PyQt5.QtCore import *
from ui.text_view import TextView


class TableView(QTableWidget):

    def __init__(self, parent) -> None:
        QTableWidget.__init__(self, 1, 2)

        self.setHorizontalHeaderLabels(['Front', 'Back'])
        self.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustToContents)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setWordWrap(True)

    def add_row(self, source_text: TextView) -> None:
        text = source_text.get_selected()

        # Add Highlight
        if text != '':
            source_text.highlight_text(text, True)

        # Add new row
        row_count = self.rowCount()
        self.setRowCount(row_count + 1)
        # Add row to 1st column
        self.setItem(row_count, 0, QTableWidgetItem(text))
        self.resizeRowsToContents()

    def delete_row(self, text: TextView) -> None:
        selected = self.selectedIndexes()
        # if selected is not None:
        # Remove highlight
        text_rm = []
        for item in selected:
            if item.column() == 0 and item.data():
                text_rm.append(item.data())

        for item in text_rm:
            text.highlight_text(item, False)

        for item in selected:
            row = item.row()
            self.removeRow(row)
