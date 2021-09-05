from PyQt5 import QtCore, QtWidgets, QtGui
from ui.text_view import TextView


class RightPanel(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(RightPanel, self).__init__(parent)
        self._ui()

    def _ui(self):
        '''
        Returns a panel with table and add, delete buttons
        '''
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(10)

        self.info_label = QtWidgets.QLineEdit(self)
        self.info_label.setPlaceholderText('Title')
        self.info_label.setFrame(False)

        self.text_view = TextView(self)
        self.text_view.setObjectName('text')

        layout.addWidget(self.info_label)
        layout.addWidget(self.text_view)

    def update_label(self, song, artist):
        self.info.setText(song + '|' + artist)
