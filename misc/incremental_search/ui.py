"""
The MIT License (MIT)

Copyright (c) 2015 <Satyajit Sarangi>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import sys
from PySide import QtCore, QtGui
from ternary_tree import *
from trie import *
import pickle

def read_dictionary(filename):
    f = open(filename)
    words = f.readlines()
    f.close()

    new_words = []
    for word in words:
        word = word.rstrip('\n')
        new_words.append(word)

    return new_words

class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self._tree = None
        self._trie = None
        self._ternary_tree = None
        self._words = None

    def build_tree(self, words, algorithm):
        tree = None
        if algorithm == "trie":
            self._trie = Trie()
            tree = self._trie
        elif algorithm == "ternary_tree":
            self._ternary_tree = TernaryTree()
            tree = self._ternary_tree
        else:
            print("No valid algorithm")

        self.progress_bar.setFocus()
        total_words = len(words) - 1
        for idx, word in enumerate(words):
            percent = (idx / total_words) * 100
            tree.insert(word)
            self.setProgress(percent)

        self.lineedit_search_bar.setFocus()

        return tree

    def keyPress(self):
        search_string = self.lineedit_search_bar.text()
        search_string.strip()
        self.list_widget_results.clear()

        if search_string is not None and search_string != '':
            results = self._tree.search(search_string)

            for idx, result in enumerate(results):
                item = QtGui.QListWidgetItem()
                item.setText(result)
                self.list_widget_results.insertItem(idx, item)

        return False

    def load_dictionary(self):
        self._words = read_dictionary('wordsEn.txt')
        self._trie = None
        self._ternary_tree = None

        if self.radio_button_trie.isChecked():
            self._trie = self.build_tree(self._words, 'trie')
            self._tree = self._trie
        elif self.radio_button_ternary_tree.isChecked():
            self._ternary_tree = self.build_tree(self._words, 'ternary_tree')
            self._tree = self._ternary_tree

    def setProgress(self, value):
        if value > 100:
            value = 100
        self.progress_bar.setValue(value)

    def changed_radio_button(self):
        if self._words is not None:
            if self.radio_button_trie.isChecked():
                if self._trie == None:
                    self.build_tree(self._words, 'trie')
                self._tree = self._trie

            if self.radio_button_ternary_tree.isChecked():
                if self._ternary_tree == None:
                    self.build_tree(self._words, 'ternary_tree')
                self._tree = self._ternary_tree

    def initUI(self):
        self.label_search_bar = QtGui.QLabel('Search Bar')
        self.lineedit_search_bar = QtGui.QLineEdit()

        self.lineedit_search_bar.textChanged.connect(self.keyPress)

        groupBox = QtGui.QGroupBox("Exclusive Radio Buttons")
        self.radio_button_trie = QtGui.QRadioButton('Trie')
        self.radio_button_ternary_tree = QtGui.QRadioButton('Ternary Tree')
        self.radio_button_trie.setChecked(True)

        self.radio_button_trie.toggled.connect(self.changed_radio_button)
        self.radio_button_ternary_tree.toggled.connect(self.changed_radio_button)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.radio_button_trie)
        vbox.addWidget(self.radio_button_ternary_tree)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        self.label_dictionary_load = QtGui.QLabel('Dict Load')
        self.progress_bar = QtGui.QProgressBar()
        self.progress_bar.setAlignment(QtCore.Qt.AlignCenter)

        self.label_results = QtGui.QLabel('Results')
        self.list_widget_results = QtGui.QListWidget()

        self.button_dict_load = QtGui.QPushButton("Dict Load")
        self.button_dict_load.clicked.connect(self.load_dictionary)

        self.button_pickle = QtGui.QPushButton("Pickle")
        self.button_pickle.clicked.connect(self.pickle)

        self.button_unpickle = QtGui.QPushButton("UnPickle")
        self.button_unpickle.clicked.connect(self.unpickle)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.label_search_bar, 1, 0)
        grid.addWidget(self.lineedit_search_bar, 1, 1)

        grid.addWidget(self.label_dictionary_load, 2, 0)
        grid.addWidget(self.progress_bar, 2, 1)

        grid.addWidget(QtGui.QLabel("Tree Type"), 3, 0)
        grid.addWidget(groupBox, 3, 1)

        grid.addWidget(self.label_results, 4, 0)
        grid.addWidget(self.list_widget_results, 4, 1, 5, 1)

        grid.addWidget(self.button_dict_load, 5, 0)
        grid.addWidget(self.button_pickle, 6, 0)
        grid.addWidget(self.button_unpickle, 7, 0)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Incremental Search')
        self.show()

    def pickle(self):
        if self._trie is not None:
            pickle.dump(self._trie, open( "trie.pickle", "wb" ))

        if self._ternary_tree is not None:
            pickle.dump(self._ternary_tree, open( "ternary_tree.pickle", "wb" ))

    def unpickle(self):
        self._trie = pickle.load(open('trie.pickle', 'rb'))
        self._ternary_tree = pickle.load(open('ternary_tree.pickle', 'rb'))

        if self.radio_button_trie.isChecked():
            self._tree = self._trie
        elif self.radio_button_ternary_tree.isChecked():
            self._tree = self._ternary_tree

def create_main_window():
    mw = MainWindow()
    return mw
