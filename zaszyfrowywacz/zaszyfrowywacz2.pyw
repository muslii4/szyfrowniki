import pyperclip
from PyQt4 import QtCore, QtGui
out = ''
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

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
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("zasz23.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.textIn = QtGui.QLineEdit(Form)
        self.textIn.setObjectName(_fromUtf8("textIn"))
        self.verticalLayout.addWidget(self.textIn)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.keyIn = QtGui.QLineEdit(Form)
        self.keyIn.setObjectName(_fromUtf8("keyIn"))
        self.verticalLayout.addWidget(self.keyIn)
        self.szyfruj = QtGui.QPushButton(Form)
        self.szyfruj.setObjectName(_fromUtf8("szyfruj"))
        self.verticalLayout.addWidget(self.szyfruj)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.kopiuj = QtGui.QPushButton(Form)
        self.kopiuj.setObjectName(_fromUtf8("kopiuj"))
        self.verticalLayout.addWidget(self.kopiuj)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Zaszyfrowywacz", None))
        self.label.setText(_translate("Form", "Tekst do zaszyfrowania:", None))
        self.label_2.setText(_translate("Form", "Klucz szyfrowania:", None))
        self.szyfruj.setText(_translate("Form", "Szyfruj", None))
        self.label_3.setText(_translate("Form", "Tutaj pojawi się zaszyfrowany tekst", None))
        self.kopiuj.setText(_translate("Form", "Kopiuj zaszyfrowany tekst", None))
        self.szyfruj.clicked.connect(self.cokolwiek)
        self.kopiuj.clicked.connect(self.skopiuj)
    def skopiuj(self):
        pyperclip.copy(out)
    
    def cokolwiek(self):
        global out
        out = ''
        klucz = self.keyIn.text()
        zasz = self.textIn.text()
        szyfr1 = []
        szyfr2 = []
        alfabet = [chr(i) for i in range(1423)]
        try:
            for j in klucz:
                szyfr1.append(j)
            for k in range(len(szyfr1)):
                if szyfr1[k] not in szyfr2:
                    szyfr2.append(szyfr1[k])
            for i in range(len(alfabet)):
                if alfabet[i] not in szyfr2:
                    szyfr2.append(alfabet[i])
            try:
                for l in zasz:
                    if szyfr2.index(l) + 1 < 10:
                        out += '000'
                    if szyfr2.index(l) + 1 < 100 and szyfr2.index(l) + 1 > 9:
                        out += '00'
                    if szyfr2.index(l) + 1 < 1000 and szyfr2.index(l) + 1 > 99:
                        out += '0'
                    out += str(szyfr2.index(l) + 1)
                self.label_3.setText(out)
            except ValueError:
                self.label_3.setText('Użyto niedopuszczalnego znaku.')
        except:
            self.label_3.setText('Coś poszło nie tak. Kod błędu: 0603260110062002')


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

