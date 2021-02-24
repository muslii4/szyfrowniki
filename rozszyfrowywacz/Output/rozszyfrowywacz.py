# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rozszyfrowywacz.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pyperclip
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
out = ''
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(350, 234)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("rozsz.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.textIn = QtGui.QLineEdit(Form)
        self.textIn.setObjectName(_fromUtf8("textIn"))
        self.verticalLayout.addWidget(self.textIn)
        self.bWklej = QtGui.QPushButton(Form)
        self.bWklej.setObjectName(_fromUtf8("bWklej"))
        self.verticalLayout.addWidget(self.bWklej)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.keyIn = QtGui.QLineEdit(Form)
        self.keyIn.setObjectName(_fromUtf8("keyIn"))
        self.verticalLayout.addWidget(self.keyIn)
        self.bRozszyfruj = QtGui.QPushButton(Form)
        self.bRozszyfruj.setObjectName(_fromUtf8("bRozszyfruj"))
        self.verticalLayout.addWidget(self.bRozszyfruj)
        self.lOut = QtGui.QLabel(Form)
        self.lOut.setObjectName(_fromUtf8("lOut"))
        self.verticalLayout.addWidget(self.lOut)
        self.bKopiuj = QtGui.QPushButton(Form)
        self.bKopiuj.setObjectName(_fromUtf8("bKopiuj"))
        self.verticalLayout.addWidget(self.bKopiuj)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Rozszyfrowywacz", None))
        self.label.setText(_translate("Form", "Zaszyfrowany tekst:", None))
        self.bWklej.setText(_translate("Form", "Wklej ze schowka", None))
        self.label_2.setText(_translate("Form", "Klucz szyfrowania:", None))
        self.bRozszyfruj.setText(_translate("Form", "Rozszyfruj", None))
        self.lOut.setText(_translate("Form", "Tu pojawi się rozszyfrowana wiadomość.", None))
        self.bKopiuj.setText(_translate("Form", "Kopiuj wiadomość", None))
        self.bKopiuj.clicked.connect(self.skopiuj)
        self.bWklej.clicked.connect(self.wklej)
        self.bRozszyfruj.clicked.connect(self.rozszyfruj)

    def rozszyfruj(self):
    
        global out
        
        klucz = self.keyIn.text()
        zasz = self.textIn.text()
        out = ''
        szyfr1 = []
        szyfr2 = []
        lzasz = []
        m = 0
        alfabet = [chr(i) for i in range(1423)]
        for j in klucz:
            szyfr1.append(j)
        for k in range(len(szyfr1)):
            if szyfr1[k] not in szyfr2:
                szyfr2.append(szyfr1[k])
        for i in range(len(alfabet)):
            if alfabet[i] not in szyfr2:
                szyfr2.append(alfabet[i])
        for l in range(int(len(str(zasz))/4)):
            lzasz.append(zasz[m] + zasz[m + 1] + zasz[m + 2] + zasz[m + 3])
            m += 4
        try:
            for n in lzasz:
                out += szyfr2[int(n) - 1]
            
            self.lOut.setText(out)
        except:
            self.lOut.setText("Ktoś coś źle wpisał.")
    def skopiuj(self):
        pyperclip.copy(out)

    def wklej(self):
        self.textIn.setText(pyperclip.paste())

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

