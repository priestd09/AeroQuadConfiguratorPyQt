# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReceiverCalibrationPanel.ui'
#
# Created: Wed Apr 24 17:24:11 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_ReceiverCalibrationPanel(object):
    def setupUi(self, ReceiverCalibrationPanel):
        ReceiverCalibrationPanel.setObjectName(_fromUtf8("ReceiverCalibrationPanel"))
        ReceiverCalibrationPanel.resize(800, 600)
        self.transmitterOutput = QtGui.QGraphicsView(ReceiverCalibrationPanel)
        self.transmitterOutput.setGeometry(QtCore.QRect(77, 166, 300, 120))
        self.transmitterOutput.setMaximumSize(QtCore.QSize(16777215, 300))
        self.transmitterOutput.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0.548, y1:0.0170455, x2:0.548, y2:1, stop:0 rgba(30, 30, 30, 255), stop:1 rgba(66, 66, 66, 255))"))
        self.transmitterOutput.setFrameShape(QtGui.QFrame.Box)
        self.transmitterOutput.setFrameShadow(QtGui.QFrame.Plain)
        self.transmitterOutput.setLineWidth(2)
        self.transmitterOutput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.transmitterOutput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.transmitterOutput.setObjectName(_fromUtf8("transmitterOutput"))
        self.leftTransmitter = QtGui.QGraphicsView(ReceiverCalibrationPanel)
        self.leftTransmitter.setGeometry(QtCore.QRect(77, 10, 147, 150))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftTransmitter.sizePolicy().hasHeightForWidth())
        self.leftTransmitter.setSizePolicy(sizePolicy)
        self.leftTransmitter.setMinimumSize(QtCore.QSize(147, 150))
        self.leftTransmitter.setMaximumSize(QtCore.QSize(147, 150))
        self.leftTransmitter.setFrameShape(QtGui.QFrame.Box)
        self.leftTransmitter.setFrameShadow(QtGui.QFrame.Plain)
        self.leftTransmitter.setLineWidth(2)
        self.leftTransmitter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.leftTransmitter.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.leftTransmitter.setObjectName(_fromUtf8("leftTransmitter"))
        self.rightTransmitter = QtGui.QGraphicsView(ReceiverCalibrationPanel)
        self.rightTransmitter.setGeometry(QtCore.QRect(230, 10, 147, 150))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightTransmitter.sizePolicy().hasHeightForWidth())
        self.rightTransmitter.setSizePolicy(sizePolicy)
        self.rightTransmitter.setMinimumSize(QtCore.QSize(147, 150))
        self.rightTransmitter.setMaximumSize(QtCore.QSize(147, 150))
        self.rightTransmitter.setFrameShape(QtGui.QFrame.Box)
        self.rightTransmitter.setFrameShadow(QtGui.QFrame.Plain)
        self.rightTransmitter.setLineWidth(2)
        self.rightTransmitter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rightTransmitter.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rightTransmitter.setObjectName(_fromUtf8("rightTransmitter"))
        self.start = QtGui.QPushButton(ReceiverCalibrationPanel)
        self.start.setGeometry(QtCore.QRect(450, 510, 100, 31))
        self.start.setObjectName(_fromUtf8("start"))
        self.cancel = QtGui.QPushButton(ReceiverCalibrationPanel)
        self.cancel.setGeometry(QtCore.QRect(570, 510, 101, 31))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.next = QtGui.QPushButton(ReceiverCalibrationPanel)
        self.next.setGeometry(QtCore.QRect(690, 510, 101, 31))
        self.next.setObjectName(_fromUtf8("next"))
        self.progressBar_RCmode = QtGui.QProgressBar(ReceiverCalibrationPanel)
        self.progressBar_RCmode.setGeometry(QtCore.QRect(140, 306, 231, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(False)
        self.progressBar_RCmode.setFont(font)
        self.progressBar_RCmode.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressBar_RCmode.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_RCmode.setMinimum(1000)
        self.progressBar_RCmode.setMaximum(2000)
        self.progressBar_RCmode.setProperty("value", 1000)
        self.progressBar_RCmode.setTextVisible(True)
        self.progressBar_RCmode.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_RCmode.setInvertedAppearance(False)
        self.progressBar_RCmode.setObjectName(_fromUtf8("progressBar_RCmode"))
        self.progressBar_RCAux1 = QtGui.QProgressBar(ReceiverCalibrationPanel)
        self.progressBar_RCAux1.setGeometry(QtCore.QRect(140, 336, 231, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.progressBar_RCAux1.setFont(font)
        self.progressBar_RCAux1.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressBar_RCAux1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_RCAux1.setMinimum(1000)
        self.progressBar_RCAux1.setMaximum(2000)
        self.progressBar_RCAux1.setProperty("value", 1000)
        self.progressBar_RCAux1.setTextVisible(True)
        self.progressBar_RCAux1.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_RCAux1.setInvertedAppearance(False)
        self.progressBar_RCAux1.setObjectName(_fromUtf8("progressBar_RCAux1"))
        self.progressBar_RCAux2 = QtGui.QProgressBar(ReceiverCalibrationPanel)
        self.progressBar_RCAux2.setGeometry(QtCore.QRect(140, 366, 231, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.progressBar_RCAux2.setFont(font)
        self.progressBar_RCAux2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressBar_RCAux2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_RCAux2.setMinimum(1000)
        self.progressBar_RCAux2.setMaximum(2000)
        self.progressBar_RCAux2.setProperty("value", 1000)
        self.progressBar_RCAux2.setTextVisible(True)
        self.progressBar_RCAux2.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_RCAux2.setInvertedAppearance(False)
        self.progressBar_RCAux2.setObjectName(_fromUtf8("progressBar_RCAux2"))
        self.progressBar_RCAux3 = QtGui.QProgressBar(ReceiverCalibrationPanel)
        self.progressBar_RCAux3.setGeometry(QtCore.QRect(140, 396, 231, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.progressBar_RCAux3.setFont(font)
        self.progressBar_RCAux3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressBar_RCAux3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_RCAux3.setMinimum(1000)
        self.progressBar_RCAux3.setMaximum(2000)
        self.progressBar_RCAux3.setProperty("value", 1000)
        self.progressBar_RCAux3.setTextVisible(True)
        self.progressBar_RCAux3.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_RCAux3.setInvertedAppearance(False)
        self.progressBar_RCAux3.setObjectName(_fromUtf8("progressBar_RCAux3"))
        self.commLog = QtGui.QTextBrowser(ReceiverCalibrationPanel)
        self.commLog.setGeometry(QtCore.QRect(450, 10, 341, 461))
        self.commLog.setFrameShadow(QtGui.QFrame.Sunken)
        self.commLog.setObjectName(_fromUtf8("commLog"))
        self.progressBar_RCAux4 = QtGui.QProgressBar(ReceiverCalibrationPanel)
        self.progressBar_RCAux4.setGeometry(QtCore.QRect(140, 426, 231, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(False)
        self.progressBar_RCAux4.setFont(font)
        self.progressBar_RCAux4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressBar_RCAux4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_RCAux4.setMinimum(1000)
        self.progressBar_RCAux4.setMaximum(2000)
        self.progressBar_RCAux4.setProperty("value", 1000)
        self.progressBar_RCAux4.setTextVisible(True)
        self.progressBar_RCAux4.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_RCAux4.setInvertedAppearance(False)
        self.progressBar_RCAux4.setObjectName(_fromUtf8("progressBar_RCAux4"))
        self.progressBar_RCAux5 = QtGui.QProgressBar(ReceiverCalibrationPanel)
        self.progressBar_RCAux5.setGeometry(QtCore.QRect(140, 456, 231, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.progressBar_RCAux5.setFont(font)
        self.progressBar_RCAux5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressBar_RCAux5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_RCAux5.setMinimum(1000)
        self.progressBar_RCAux5.setMaximum(2000)
        self.progressBar_RCAux5.setProperty("value", 1000)
        self.progressBar_RCAux5.setTextVisible(True)
        self.progressBar_RCAux5.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_RCAux5.setInvertedAppearance(False)
        self.progressBar_RCAux5.setObjectName(_fromUtf8("progressBar_RCAux5"))
        self.progressBar_RCAux7 = QtGui.QProgressBar(ReceiverCalibrationPanel)
        self.progressBar_RCAux7.setGeometry(QtCore.QRect(140, 516, 231, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.progressBar_RCAux7.setFont(font)
        self.progressBar_RCAux7.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressBar_RCAux7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_RCAux7.setMinimum(1000)
        self.progressBar_RCAux7.setMaximum(2000)
        self.progressBar_RCAux7.setProperty("value", 1000)
        self.progressBar_RCAux7.setTextVisible(True)
        self.progressBar_RCAux7.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_RCAux7.setInvertedAppearance(False)
        self.progressBar_RCAux7.setObjectName(_fromUtf8("progressBar_RCAux7"))
        self.progressBar_RCAux6 = QtGui.QProgressBar(ReceiverCalibrationPanel)
        self.progressBar_RCAux6.setGeometry(QtCore.QRect(140, 486, 231, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.progressBar_RCAux6.setFont(font)
        self.progressBar_RCAux6.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressBar_RCAux6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_RCAux6.setMinimum(1000)
        self.progressBar_RCAux6.setMaximum(2000)
        self.progressBar_RCAux6.setProperty("value", 1000)
        self.progressBar_RCAux6.setTextVisible(True)
        self.progressBar_RCAux6.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_RCAux6.setInvertedAppearance(False)
        self.progressBar_RCAux6.setObjectName(_fromUtf8("progressBar_RCAux6"))
        self.label = QtGui.QLabel(ReceiverCalibrationPanel)
        self.label.setGeometry(QtCore.QRect(80, 311, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_aux1 = QtGui.QLabel(ReceiverCalibrationPanel)
        self.label_aux1.setGeometry(QtCore.QRect(80, 341, 46, 13))
        self.label_aux1.setObjectName(_fromUtf8("label_aux1"))
        self.label_aux2 = QtGui.QLabel(ReceiverCalibrationPanel)
        self.label_aux2.setGeometry(QtCore.QRect(80, 370, 46, 13))
        self.label_aux2.setObjectName(_fromUtf8("label_aux2"))
        self.label_aux3 = QtGui.QLabel(ReceiverCalibrationPanel)
        self.label_aux3.setGeometry(QtCore.QRect(80, 400, 46, 13))
        self.label_aux3.setObjectName(_fromUtf8("label_aux3"))
        self.label_aux4 = QtGui.QLabel(ReceiverCalibrationPanel)
        self.label_aux4.setGeometry(QtCore.QRect(80, 430, 46, 13))
        self.label_aux4.setObjectName(_fromUtf8("label_aux4"))
        self.label_aux5 = QtGui.QLabel(ReceiverCalibrationPanel)
        self.label_aux5.setGeometry(QtCore.QRect(80, 460, 46, 13))
        self.label_aux5.setObjectName(_fromUtf8("label_aux5"))
        self.label_aux6 = QtGui.QLabel(ReceiverCalibrationPanel)
        self.label_aux6.setGeometry(QtCore.QRect(80, 490, 46, 13))
        self.label_aux6.setObjectName(_fromUtf8("label_aux6"))
        self.label_aux7 = QtGui.QLabel(ReceiverCalibrationPanel)
        self.label_aux7.setGeometry(QtCore.QRect(80, 520, 46, 13))
        self.label_aux7.setObjectName(_fromUtf8("label_aux7"))

        self.retranslateUi(ReceiverCalibrationPanel)
        QtCore.QMetaObject.connectSlotsByName(ReceiverCalibrationPanel)

    def retranslateUi(self, ReceiverCalibrationPanel):
        ReceiverCalibrationPanel.setWindowTitle(_translate("ReceiverCalibrationPanel", "Form", None))
        self.start.setText(_translate("ReceiverCalibrationPanel", "Start", None))
        self.cancel.setText(_translate("ReceiverCalibrationPanel", "Cancel", None))
        self.next.setText(_translate("ReceiverCalibrationPanel", "Next", None))
        self.progressBar_RCmode.setFormat(_translate("ReceiverCalibrationPanel", "%v", None))
        self.progressBar_RCAux1.setFormat(_translate("ReceiverCalibrationPanel", "%v", None))
        self.progressBar_RCAux2.setFormat(_translate("ReceiverCalibrationPanel", "%v", None))
        self.progressBar_RCAux3.setFormat(_translate("ReceiverCalibrationPanel", "%v", None))
        self.commLog.setHtml(_translate("ReceiverCalibrationPanel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1) Press start to start the RC calibration.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2) Move all channels to the minimum and maximum value.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3) When done press finish to save the calibration.</span></p></body></html>", None))
        self.progressBar_RCAux4.setFormat(_translate("ReceiverCalibrationPanel", "%v", None))
        self.progressBar_RCAux5.setFormat(_translate("ReceiverCalibrationPanel", "%v", None))
        self.progressBar_RCAux7.setFormat(_translate("ReceiverCalibrationPanel", "%v", None))
        self.progressBar_RCAux6.setFormat(_translate("ReceiverCalibrationPanel", "%v", None))
        self.label.setText(_translate("ReceiverCalibrationPanel", "Mode", None))
        self.label_aux1.setText(_translate("ReceiverCalibrationPanel", "Aux1", None))
        self.label_aux2.setText(_translate("ReceiverCalibrationPanel", "Aux2", None))
        self.label_aux3.setText(_translate("ReceiverCalibrationPanel", "Aux3", None))
        self.label_aux4.setText(_translate("ReceiverCalibrationPanel", "Aux4", None))
        self.label_aux5.setText(_translate("ReceiverCalibrationPanel", "Aux5", None))
        self.label_aux6.setText(_translate("ReceiverCalibrationPanel", "Aux6", None))
        self.label_aux7.setText(_translate("ReceiverCalibrationPanel", "Aux7", None))

