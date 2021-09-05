from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QTextCharFormat, QBrush, QColor, QTextCursor
from PyQt5.QtCore import QRegExp
import random


class TextView(QTextEdit):

    def __init__(self, parent):
        super().__init__()
        self.setAcceptRichText(False)
        self.setTabChangesFocus(True)
        # self.setReadOnly(True)
        self.setText(
            "Now here you go again, you say you want your freedom\nWell, who am I to keep you down?")
        self.curr_colors = []  # current highlighted colors in use

    def get_selected(self) -> str:
        '''Returns selected text'''
        cursor = self.textCursor()
        text = (cursor.selectedText()).strip()
        # Next two lines -> deselects the text
        cursor.movePosition(QTextCursor.End)
        self.setTextCursor(cursor)

        return text

    def random_color(self):
        '''Generate random, visible colors for highlighting'''

        hue = random.randrange(0, 333, 1)
        sat = 255
        light = random.randrange(127, 200, 1)
        color = QColor()
        color.setHsl(hue, sat, light, 100)
        return color

    #! Test Feature, not currently highlighting properly
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

        #! Need to find a way to remove selected text's color from list

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
