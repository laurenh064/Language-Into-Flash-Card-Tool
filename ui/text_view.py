from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QTextCharFormat, QBrush, QColor, QTextCursor
from PyQt5.QtCore import QRegExp

class TextView(QTextEdit):

    def __init__(self, parent):
        super().__init__()
        self.setAcceptRichText(False)
        self.setTabChangesFocus(True)
        self.setReadOnly(True)
        self.setText("")

    def get_selected(self) -> str:
        '''Returns selected text'''
        cursor = self.textCursor()
        text = (cursor.selectedText()).strip()
        # Next two lines -> deselects the text
        cursor.movePosition(QTextCursor.End)
        self.setTextCursor(cursor)

        return text

    def highlight_text(self, text: str, highlight: bool) -> None:
        '''Highlights and removes highlights'''

        format = QTextCharFormat()
        if highlight == True:
            color = self.random_color()
            self.curr_colors.append(color)
            print(self.curr_colors)
            format.setBackground(QBrush(color))
        # Remove highlight
        else:
            format.setBackground(QBrush(QColor(255, 255, 255, 0)))

        cursor = self.textCursor()

        pattern = '(' + text + ')'
        regex = QRegExp(pattern)
        regex.setCaseSensitivity(False)
        pos = 0
        index = regex.indexIn(self.toPlainText(), pos)

        while(index != -1):
            cursor.setPosition(index)
            cursor.movePosition(QTextCursor.Right, 1, len(text))
            cursor.mergeCharFormat(format)
            pos = index + regex.matchedLength()
            index = regex.indexIn(self.toPlainText(), pos)
