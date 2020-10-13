# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/windowIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setStyleSheet("background-color:rgb(255, 85, 0);\n"
"min-height:40;\n"
"max-height:40;")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setContentsMargins(-1, 6, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Logo = QtWidgets.QLabel(self.horizontalFrame)
        self.Logo.setStyleSheet("min-width:30px;\n"
"max-width:30px;\n"
"min-height:30px;\n"
"max-height:30px;")
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap(":/icons/icons/logo.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.horizontalLayout.addWidget(self.Logo, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.CodeGeneratorPushButton = QtWidgets.QPushButton(self.horizontalFrame)
        self.CodeGeneratorPushButton.setMinimumSize(QtCore.QSize(27, 27))
        self.CodeGeneratorPushButton.setMaximumSize(QtCore.QSize(27, 27))
        self.CodeGeneratorPushButton.setStyleSheet("QPushButton#CodeGeneratorPushButton {\n"
"    min-width: 25px;\n"
"    max-width: 25px;\n"
"    min-height: 25px;\n"
"    max-height: 25px;\n"
"    background-color: rgba(255, 255, 255, 0%);\n"
"    \n"
"    border:1px;\n"
"    border-color: rgb(255, 85, 0);\n"
"    border-style: solid;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius:5px;\n"
"}\n"
"\n"
"QPushButton#CodeGeneratorPushButton:hover {\n"
"    background:  rgb(255, 119, 51);\n"
"}\n"
"\n"
"QPushButton#CodeGeneratorPushButton:pressed {\n"
"    background: rgba(255, 255, 255, 0%);\n"
"}")
        self.CodeGeneratorPushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/code.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CodeGeneratorPushButton.setIcon(icon1)
        self.CodeGeneratorPushButton.setIconSize(QtCore.QSize(25, 25))
        self.CodeGeneratorPushButton.setObjectName("CodeGeneratorPushButton")
        self.horizontalLayout.addWidget(self.CodeGeneratorPushButton)
        self.RegexSheetPushButton = QtWidgets.QPushButton(self.horizontalFrame)
        self.RegexSheetPushButton.setMinimumSize(QtCore.QSize(27, 27))
        self.RegexSheetPushButton.setMaximumSize(QtCore.QSize(27, 27))
        self.RegexSheetPushButton.setStyleSheet("QPushButton#RegexSheetPushButton {\n"
"    min-width: 25px;\n"
"    max-width: 25px;\n"
"    min-height: 25px;\n"
"    max-height: 25px;\n"
"    background-color: rgba(255, 255, 255, 0%);\n"
"    \n"
"    border:1px;\n"
"    border-color: rgb(255, 85, 0);\n"
"    border-style: solid;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius:5px;\n"
"}\n"
"\n"
"QPushButton#RegexSheetPushButton:hover {\n"
"    background:  rgb(255, 119, 51);\n"
"}\n"
"\n"
"QPushButton#RegexSheetPushButton:pressed {\n"
"    background: rgba(255, 255, 255, 0%);\n"
"}")
        self.RegexSheetPushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/sheet.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RegexSheetPushButton.setIcon(icon2)
        self.RegexSheetPushButton.setIconSize(QtCore.QSize(25, 25))
        self.RegexSheetPushButton.setObjectName("RegexSheetPushButton")
        self.horizontalLayout.addWidget(self.RegexSheetPushButton)
        self.AboutPushButton = QtWidgets.QPushButton(self.horizontalFrame)
        self.AboutPushButton.setMinimumSize(QtCore.QSize(27, 27))
        self.AboutPushButton.setMaximumSize(QtCore.QSize(27, 27))
        self.AboutPushButton.setStyleSheet("QPushButton#AboutPushButton {\n"
"    min-width: 25px;\n"
"    max-width: 25px;\n"
"    min-height: 25px;\n"
"    max-height: 25px;\n"
"    background-color: rgba(255, 255, 255, 0%);\n"
"    \n"
"    border:1px;\n"
"    border-color: rgb(255, 85, 0);\n"
"    border-style: solid;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius:5px;\n"
"}\n"
"\n"
"QPushButton#AboutPushButton:hover {\n"
"    background:  rgb(255, 119, 51);\n"
"}\n"
"\n"
"QPushButton#AboutPushButton:pressed {\n"
"    background: rgba(255, 255, 255, 0%);\n"
"}")
        self.AboutPushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AboutPushButton.setIcon(icon3)
        self.AboutPushButton.setIconSize(QtCore.QSize(25, 25))
        self.AboutPushButton.setObjectName("AboutPushButton")
        self.horizontalLayout.addWidget(self.AboutPushButton)
        self.verticalLayout.addWidget(self.horizontalFrame, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(15, 15, 15, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("min-height:15;\n"
"max-height:15;\n"
"background-color: rgba(0, 0, 0, 0%);")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.NoMatchesLabel = QtWidgets.QLabel(self.centralwidget)
        self.NoMatchesLabel.setStyleSheet("    background-color: rgb(153, 153, 153);\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    min-width:150px;\n"
"    max-width:150px;\n"
"    min-height:20;\n"
"    max-height:20;")
        self.NoMatchesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.NoMatchesLabel.setObjectName("NoMatchesLabel")
        self.horizontalLayout_4.addWidget(self.NoMatchesLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.RegexTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.RegexTextEdit.setFont(font)
        self.RegexTextEdit.setStyleSheet("QPlainTextEdit {\n"
"    min-width:360px;\n"
"    min-height:30;\n"
"    max-height:30;\n"
"    margin-bottom:5px;\n"
"    \n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(255,255,255,100%);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPlainTextEdit::focus    {\n"
"    border-bottom-color:rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPlainTextEdit::disabled    {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15);\n"
"}")
        self.RegexTextEdit.setObjectName("RegexTextEdit")
        self.horizontalLayout_3.addWidget(self.RegexTextEdit)
        self.ProcessPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ProcessPushButton.setStyleSheet("QPushButton#ProcessPushButton {\n"
"    min-width:60px;\n"
"    max-width:60px;\n"
"    min-height:35;\n"
"    max-height:35;\n"
"    margin-bottom:5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(255,255,255,100%);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPushButton#ProcessPushButton:hover {\n"
"    background:  rgba(255,255,255,50%);\n"
"    border-bottom-color:rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton#ProcessPushButton:pressed {\n"
"    background:  rgba(255,255,255,100%);\n"
"    border-bottom-color:rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton#ProcessPushButton:disabled {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15); \n"
"}")
        self.ProcessPushButton.setObjectName("ProcessPushButton")
        self.horizontalLayout_3.addWidget(self.ProcessPushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("min-height:15;\n"
"max-height:15;\n"
"background-color: rgba(0, 0, 0, 0%);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.TestStringTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.TestStringTextEdit.setFont(font)
        self.TestStringTextEdit.setStyleSheet("QPlainTextEdit {\n"
"    min-width:360px;\n"
"    min-height:30;\n"
"    \n"
"    padding-left: 5px;\n"
"    padding-top: 10px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(255,255,255,100%);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPlainTextEdit::focus    {\n"
"    border-bottom-color:rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPlainTextEdit::disabled    {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15);\n"
"}")
        self.TestStringTextEdit.setObjectName("TestStringTextEdit")
        self.verticalLayout_4.addWidget(self.TestStringTextEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setStyleSheet("background-color: rgb(238, 238, 238);\n"
"min-width: 300;\n"
"max-width: 500;")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.verticalFrame)
        self.widget.setStyleSheet("background-color:rgb(249, 249, 249)")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("min-height:15;\n"
"max-height:15;\n"
"background-color: rgba(0, 0, 0, 0%);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.RresultScrollArea = QtWidgets.QScrollArea(self.widget)
        self.RresultScrollArea.setStyleSheet("border:No;")
        self.RresultScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RresultScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RresultScrollArea.setWidgetResizable(True)
        self.RresultScrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.RresultScrollArea.setObjectName("RresultScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 300, 449))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.RresultScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.RresultScrollArea)
        self.verticalLayout_2.addWidget(self.widget)
        self.horizontalLayout_2.addWidget(self.verticalFrame)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1081, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.SheetDockWidget = QtWidgets.QDockWidget(MainWindow)
        self.SheetDockWidget.setMinimumSize(QtCore.QSize(312, 91))
        self.SheetDockWidget.setMaximumSize(QtCore.QSize(312, 524287))
        self.SheetDockWidget.setStyleSheet("")
        self.SheetDockWidget.setObjectName("SheetDockWidget")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents_4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.dockWidgetContents_4)
        self.scrollArea_2.setStyleSheet("border:No;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 296, 1465))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_126 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_126.setFont(font)
        self.label_126.setStyleSheet("min-height:15;\n"
"max-height:15;\n"
"background-color: rgba(0, 0, 0, 0%);")
        self.label_126.setObjectName("label_126")
        self.verticalLayout_17.addWidget(self.label_126)
        self.line_12 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_12.setStyleSheet("background-color:rgb(255, 85, 0);\n"
"border:No;\n"
"height:1px")
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout_17.addWidget(self.line_12)
        self.verticalLayout_16.addLayout(self.verticalLayout_17)
        self.horizontalLayout_62 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")
        self.label_127 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_127.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_127.setObjectName("label_127")
        self.horizontalLayout_62.addWidget(self.label_127)
        self.label_128 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_128.setObjectName("label_128")
        self.horizontalLayout_62.addWidget(self.label_128)
        self.verticalLayout_16.addLayout(self.horizontalLayout_62)
        self.horizontalLayout_63 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        self.label_129 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_129.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_129.setObjectName("label_129")
        self.horizontalLayout_63.addWidget(self.label_129)
        self.label_130 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_130.setObjectName("label_130")
        self.horizontalLayout_63.addWidget(self.label_130)
        self.verticalLayout_16.addLayout(self.horizontalLayout_63)
        self.horizontalLayout_64 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")
        self.label_131 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_131.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_131.setObjectName("label_131")
        self.horizontalLayout_64.addWidget(self.label_131)
        self.label_132 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_132.setObjectName("label_132")
        self.horizontalLayout_64.addWidget(self.label_132)
        self.verticalLayout_16.addLayout(self.horizontalLayout_64)
        self.horizontalLayout_65 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        self.label_133 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_133.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_133.setObjectName("label_133")
        self.horizontalLayout_65.addWidget(self.label_133)
        self.label_134 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_134.setObjectName("label_134")
        self.horizontalLayout_65.addWidget(self.label_134)
        self.verticalLayout_16.addLayout(self.horizontalLayout_65)
        self.horizontalLayout_66 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_66.setObjectName("horizontalLayout_66")
        self.label_135 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_135.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_135.setObjectName("label_135")
        self.horizontalLayout_66.addWidget(self.label_135)
        self.label_136 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_136.setObjectName("label_136")
        self.horizontalLayout_66.addWidget(self.label_136)
        self.verticalLayout_16.addLayout(self.horizontalLayout_66)
        self.horizontalLayout_67 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_67.setObjectName("horizontalLayout_67")
        self.label_137 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_137.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_137.setObjectName("label_137")
        self.horizontalLayout_67.addWidget(self.label_137)
        self.label_138 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_138.setObjectName("label_138")
        self.horizontalLayout_67.addWidget(self.label_138)
        self.verticalLayout_16.addLayout(self.horizontalLayout_67)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_139 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_139.setFont(font)
        self.label_139.setStyleSheet("min-height:15;\n"
"max-height:15;\n"
"background-color: rgba(0, 0, 0, 0%);")
        self.label_139.setObjectName("label_139")
        self.verticalLayout_18.addWidget(self.label_139)
        self.line_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_13.setStyleSheet("background-color:rgb(255, 85, 0);\n"
"border:No;\n"
"height:1px")
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.verticalLayout_18.addWidget(self.line_13)
        self.verticalLayout_16.addLayout(self.verticalLayout_18)
        self.horizontalLayout_68 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_68.setObjectName("horizontalLayout_68")
        self.label_140 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_140.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_140.setObjectName("label_140")
        self.horizontalLayout_68.addWidget(self.label_140)
        self.label_141 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_141.setObjectName("label_141")
        self.horizontalLayout_68.addWidget(self.label_141)
        self.verticalLayout_16.addLayout(self.horizontalLayout_68)
        self.horizontalLayout_69 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_69.setObjectName("horizontalLayout_69")
        self.label_142 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_142.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_142.setObjectName("label_142")
        self.horizontalLayout_69.addWidget(self.label_142)
        self.label_143 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_143.setObjectName("label_143")
        self.horizontalLayout_69.addWidget(self.label_143)
        self.verticalLayout_16.addLayout(self.horizontalLayout_69)
        self.horizontalLayout_70 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_70.setObjectName("horizontalLayout_70")
        self.label_144 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_144.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_144.setObjectName("label_144")
        self.horizontalLayout_70.addWidget(self.label_144)
        self.label_145 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_145.setObjectName("label_145")
        self.horizontalLayout_70.addWidget(self.label_145)
        self.verticalLayout_16.addLayout(self.horizontalLayout_70)
        self.horizontalLayout_71 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_71.setObjectName("horizontalLayout_71")
        self.label_146 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_146.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_146.setObjectName("label_146")
        self.horizontalLayout_71.addWidget(self.label_146)
        self.label_147 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_147.setObjectName("label_147")
        self.horizontalLayout_71.addWidget(self.label_147)
        self.verticalLayout_16.addLayout(self.horizontalLayout_71)
        self.horizontalLayout_72 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_72.setObjectName("horizontalLayout_72")
        self.label_148 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_148.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_148.setObjectName("label_148")
        self.horizontalLayout_72.addWidget(self.label_148)
        self.label_149 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_149.setObjectName("label_149")
        self.horizontalLayout_72.addWidget(self.label_149)
        self.verticalLayout_16.addLayout(self.horizontalLayout_72)
        self.horizontalLayout_73 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_73.setObjectName("horizontalLayout_73")
        self.label_150 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_150.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_150.setObjectName("label_150")
        self.horizontalLayout_73.addWidget(self.label_150)
        self.label_151 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_151.setObjectName("label_151")
        self.horizontalLayout_73.addWidget(self.label_151)
        self.verticalLayout_16.addLayout(self.horizontalLayout_73)
        self.horizontalLayout_74 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_74.setObjectName("horizontalLayout_74")
        self.label_152 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_152.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_152.setObjectName("label_152")
        self.horizontalLayout_74.addWidget(self.label_152)
        self.label_153 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_153.setObjectName("label_153")
        self.horizontalLayout_74.addWidget(self.label_153)
        self.verticalLayout_16.addLayout(self.horizontalLayout_74)
        self.horizontalLayout_75 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_75.setObjectName("horizontalLayout_75")
        self.label_154 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_154.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_154.setObjectName("label_154")
        self.horizontalLayout_75.addWidget(self.label_154)
        self.label_155 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_155.setObjectName("label_155")
        self.horizontalLayout_75.addWidget(self.label_155)
        self.verticalLayout_16.addLayout(self.horizontalLayout_75)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_156 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_156.setFont(font)
        self.label_156.setStyleSheet("min-height:15;\n"
"max-height:15;\n"
"background-color: rgba(0, 0, 0, 0%);")
        self.label_156.setObjectName("label_156")
        self.verticalLayout_19.addWidget(self.label_156)
        self.line_14 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_14.setStyleSheet("background-color:rgb(255, 85, 0);\n"
"border:No;\n"
"height:1px")
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.verticalLayout_19.addWidget(self.line_14)
        self.verticalLayout_16.addLayout(self.verticalLayout_19)
        self.horizontalLayout_76 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_76.setObjectName("horizontalLayout_76")
        self.label_157 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_157.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_157.setObjectName("label_157")
        self.horizontalLayout_76.addWidget(self.label_157)
        self.label_158 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_158.setObjectName("label_158")
        self.horizontalLayout_76.addWidget(self.label_158)
        self.verticalLayout_16.addLayout(self.horizontalLayout_76)
        self.horizontalLayout_77 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_77.setObjectName("horizontalLayout_77")
        self.label_159 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_159.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_159.setObjectName("label_159")
        self.horizontalLayout_77.addWidget(self.label_159)
        self.label_160 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_160.setObjectName("label_160")
        self.horizontalLayout_77.addWidget(self.label_160)
        self.verticalLayout_16.addLayout(self.horizontalLayout_77)
        self.horizontalLayout_78 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_78.setObjectName("horizontalLayout_78")
        self.label_161 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_161.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_161.setObjectName("label_161")
        self.horizontalLayout_78.addWidget(self.label_161)
        self.label_162 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_162.setObjectName("label_162")
        self.horizontalLayout_78.addWidget(self.label_162)
        self.verticalLayout_16.addLayout(self.horizontalLayout_78)
        self.horizontalLayout_79 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_79.setObjectName("horizontalLayout_79")
        self.label_163 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_163.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_163.setObjectName("label_163")
        self.horizontalLayout_79.addWidget(self.label_163)
        self.label_164 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_164.setObjectName("label_164")
        self.horizontalLayout_79.addWidget(self.label_164)
        self.verticalLayout_16.addLayout(self.horizontalLayout_79)
        self.horizontalLayout_80 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_80.setObjectName("horizontalLayout_80")
        self.label_165 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_165.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_165.setObjectName("label_165")
        self.horizontalLayout_80.addWidget(self.label_165)
        self.label_166 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_166.setObjectName("label_166")
        self.horizontalLayout_80.addWidget(self.label_166)
        self.verticalLayout_16.addLayout(self.horizontalLayout_80)
        self.horizontalLayout_81 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_81.setObjectName("horizontalLayout_81")
        self.label_167 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_167.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_167.setObjectName("label_167")
        self.horizontalLayout_81.addWidget(self.label_167)
        self.label_168 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_168.setObjectName("label_168")
        self.horizontalLayout_81.addWidget(self.label_168)
        self.verticalLayout_16.addLayout(self.horizontalLayout_81)
        self.horizontalLayout_82 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_82.setObjectName("horizontalLayout_82")
        self.label_169 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_169.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_169.setObjectName("label_169")
        self.horizontalLayout_82.addWidget(self.label_169)
        self.label_170 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_170.setObjectName("label_170")
        self.horizontalLayout_82.addWidget(self.label_170)
        self.verticalLayout_16.addLayout(self.horizontalLayout_82)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_171 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_171.setFont(font)
        self.label_171.setStyleSheet("min-height:15;\n"
"max-height:15;\n"
"background-color: rgba(0, 0, 0, 0%);")
        self.label_171.setObjectName("label_171")
        self.verticalLayout_20.addWidget(self.label_171)
        self.line_15 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_15.setStyleSheet("background-color:rgb(255, 85, 0);\n"
"border:No;\n"
"height:1px")
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.verticalLayout_20.addWidget(self.line_15)
        self.verticalLayout_16.addLayout(self.verticalLayout_20)
        self.horizontalLayout_83 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_83.setObjectName("horizontalLayout_83")
        self.label_172 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_172.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_172.setObjectName("label_172")
        self.horizontalLayout_83.addWidget(self.label_172)
        self.label_173 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_173.setObjectName("label_173")
        self.horizontalLayout_83.addWidget(self.label_173)
        self.verticalLayout_16.addLayout(self.horizontalLayout_83)
        self.horizontalLayout_84 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_84.setObjectName("horizontalLayout_84")
        self.label_174 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_174.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_174.setObjectName("label_174")
        self.horizontalLayout_84.addWidget(self.label_174)
        self.label_175 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_175.setObjectName("label_175")
        self.horizontalLayout_84.addWidget(self.label_175)
        self.verticalLayout_16.addLayout(self.horizontalLayout_84)
        self.horizontalLayout_85 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_85.setObjectName("horizontalLayout_85")
        self.label_176 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_176.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_176.setObjectName("label_176")
        self.horizontalLayout_85.addWidget(self.label_176)
        self.label_177 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_177.setObjectName("label_177")
        self.horizontalLayout_85.addWidget(self.label_177)
        self.verticalLayout_16.addLayout(self.horizontalLayout_85)
        self.horizontalLayout_86 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_86.setObjectName("horizontalLayout_86")
        self.label_178 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_178.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_178.setObjectName("label_178")
        self.horizontalLayout_86.addWidget(self.label_178)
        self.label_179 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_179.setObjectName("label_179")
        self.horizontalLayout_86.addWidget(self.label_179)
        self.verticalLayout_16.addLayout(self.horizontalLayout_86)
        self.horizontalLayout_87 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_87.setObjectName("horizontalLayout_87")
        self.label_180 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_180.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_180.setObjectName("label_180")
        self.horizontalLayout_87.addWidget(self.label_180)
        self.label_181 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_181.setObjectName("label_181")
        self.horizontalLayout_87.addWidget(self.label_181)
        self.verticalLayout_16.addLayout(self.horizontalLayout_87)
        self.horizontalLayout_88 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_88.setObjectName("horizontalLayout_88")
        self.label_182 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_182.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_182.setObjectName("label_182")
        self.horizontalLayout_88.addWidget(self.label_182)
        self.label_183 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_183.setObjectName("label_183")
        self.horizontalLayout_88.addWidget(self.label_183)
        self.verticalLayout_16.addLayout(self.horizontalLayout_88)
        self.horizontalLayout_89 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_89.setObjectName("horizontalLayout_89")
        self.label_184 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_184.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_184.setObjectName("label_184")
        self.horizontalLayout_89.addWidget(self.label_184)
        self.label_185 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_185.setObjectName("label_185")
        self.horizontalLayout_89.addWidget(self.label_185)
        self.verticalLayout_16.addLayout(self.horizontalLayout_89)
        self.horizontalLayout_90 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_90.setObjectName("horizontalLayout_90")
        self.label_186 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_186.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_186.setObjectName("label_186")
        self.horizontalLayout_90.addWidget(self.label_186)
        self.label_187 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_187.setObjectName("label_187")
        self.horizontalLayout_90.addWidget(self.label_187)
        self.verticalLayout_16.addLayout(self.horizontalLayout_90)
        self.horizontalLayout_91 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_91.setObjectName("horizontalLayout_91")
        self.label_188 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_188.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_188.setObjectName("label_188")
        self.horizontalLayout_91.addWidget(self.label_188)
        self.label_189 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_189.setObjectName("label_189")
        self.horizontalLayout_91.addWidget(self.label_189)
        self.verticalLayout_16.addLayout(self.horizontalLayout_91)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_190 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_190.setFont(font)
        self.label_190.setStyleSheet("min-height:15;\n"
"max-height:15;\n"
"background-color: rgba(0, 0, 0, 0%);")
        self.label_190.setObjectName("label_190")
        self.verticalLayout_21.addWidget(self.label_190)
        self.line_16 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_16.setStyleSheet("background-color:rgb(255, 85, 0);\n"
"border:No;\n"
"height:1px")
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.verticalLayout_21.addWidget(self.line_16)
        self.verticalLayout_16.addLayout(self.verticalLayout_21)
        self.horizontalLayout_92 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_92.setObjectName("horizontalLayout_92")
        self.label_191 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_191.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_191.setObjectName("label_191")
        self.horizontalLayout_92.addWidget(self.label_191)
        self.label_192 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_192.setObjectName("label_192")
        self.horizontalLayout_92.addWidget(self.label_192)
        self.verticalLayout_16.addLayout(self.horizontalLayout_92)
        self.horizontalLayout_93 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_93.setObjectName("horizontalLayout_93")
        self.label_193 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_193.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_193.setObjectName("label_193")
        self.horizontalLayout_93.addWidget(self.label_193)
        self.label_194 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_194.setObjectName("label_194")
        self.horizontalLayout_93.addWidget(self.label_194)
        self.verticalLayout_16.addLayout(self.horizontalLayout_93)
        self.horizontalLayout_94 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_94.setObjectName("horizontalLayout_94")
        self.label_195 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_195.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_195.setObjectName("label_195")
        self.horizontalLayout_94.addWidget(self.label_195)
        self.label_196 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_196.setObjectName("label_196")
        self.horizontalLayout_94.addWidget(self.label_196)
        self.verticalLayout_16.addLayout(self.horizontalLayout_94)
        self.horizontalLayout_95 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_95.setObjectName("horizontalLayout_95")
        self.label_197 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_197.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_197.setObjectName("label_197")
        self.horizontalLayout_95.addWidget(self.label_197)
        self.label_198 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_198.setObjectName("label_198")
        self.horizontalLayout_95.addWidget(self.label_198)
        self.verticalLayout_16.addLayout(self.horizontalLayout_95)
        self.horizontalLayout_96 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_96.setObjectName("horizontalLayout_96")
        self.label_199 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_199.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_199.setObjectName("label_199")
        self.horizontalLayout_96.addWidget(self.label_199)
        self.label_200 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_200.setObjectName("label_200")
        self.horizontalLayout_96.addWidget(self.label_200)
        self.verticalLayout_16.addLayout(self.horizontalLayout_96)
        self.horizontalLayout_97 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_97.setObjectName("horizontalLayout_97")
        self.label_201 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_201.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_201.setObjectName("label_201")
        self.horizontalLayout_97.addWidget(self.label_201)
        self.label_202 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_202.setObjectName("label_202")
        self.horizontalLayout_97.addWidget(self.label_202)
        self.verticalLayout_16.addLayout(self.horizontalLayout_97)
        self.horizontalLayout_98 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_98.setObjectName("horizontalLayout_98")
        self.label_203 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_203.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_203.setObjectName("label_203")
        self.horizontalLayout_98.addWidget(self.label_203)
        self.label_204 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_204.setObjectName("label_204")
        self.horizontalLayout_98.addWidget(self.label_204)
        self.verticalLayout_16.addLayout(self.horizontalLayout_98)
        self.horizontalLayout_99 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_99.setObjectName("horizontalLayout_99")
        self.label_205 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_205.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_205.setObjectName("label_205")
        self.horizontalLayout_99.addWidget(self.label_205)
        self.label_206 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_206.setObjectName("label_206")
        self.horizontalLayout_99.addWidget(self.label_206)
        self.verticalLayout_16.addLayout(self.horizontalLayout_99)
        self.horizontalLayout_100 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_100.setObjectName("horizontalLayout_100")
        self.label_207 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_207.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_207.setObjectName("label_207")
        self.horizontalLayout_100.addWidget(self.label_207)
        self.label_208 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_208.setObjectName("label_208")
        self.horizontalLayout_100.addWidget(self.label_208)
        self.verticalLayout_16.addLayout(self.horizontalLayout_100)
        self.horizontalLayout_101 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_101.setObjectName("horizontalLayout_101")
        self.label_209 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_209.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_209.setObjectName("label_209")
        self.horizontalLayout_101.addWidget(self.label_209)
        self.label_210 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_210.setObjectName("label_210")
        self.horizontalLayout_101.addWidget(self.label_210)
        self.verticalLayout_16.addLayout(self.horizontalLayout_101)
        self.horizontalLayout_102 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_102.setObjectName("horizontalLayout_102")
        self.label_211 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_211.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_211.setObjectName("label_211")
        self.horizontalLayout_102.addWidget(self.label_211)
        self.label_212 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_212.setObjectName("label_212")
        self.horizontalLayout_102.addWidget(self.label_212)
        self.verticalLayout_16.addLayout(self.horizontalLayout_102)
        self.horizontalLayout_103 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_103.setObjectName("horizontalLayout_103")
        self.label_213 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_213.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_213.setObjectName("label_213")
        self.horizontalLayout_103.addWidget(self.label_213)
        self.label_214 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_214.setObjectName("label_214")
        self.horizontalLayout_103.addWidget(self.label_214)
        self.verticalLayout_16.addLayout(self.horizontalLayout_103)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_215 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_215.setFont(font)
        self.label_215.setStyleSheet("min-height:15;\n"
"max-height:15;\n"
"background-color: rgba(0, 0, 0, 0%);")
        self.label_215.setObjectName("label_215")
        self.verticalLayout_22.addWidget(self.label_215)
        self.line_17 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_17.setStyleSheet("background-color:rgb(255, 85, 0);\n"
"border:No;\n"
"height:1px")
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.verticalLayout_22.addWidget(self.line_17)
        self.verticalLayout_16.addLayout(self.verticalLayout_22)
        self.horizontalLayout_104 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_104.setObjectName("horizontalLayout_104")
        self.label_216 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_216.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_216.setObjectName("label_216")
        self.horizontalLayout_104.addWidget(self.label_216)
        self.label_217 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_217.setObjectName("label_217")
        self.horizontalLayout_104.addWidget(self.label_217)
        self.verticalLayout_16.addLayout(self.horizontalLayout_104)
        self.horizontalLayout_105 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_105.setObjectName("horizontalLayout_105")
        self.label_218 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_218.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_218.setObjectName("label_218")
        self.horizontalLayout_105.addWidget(self.label_218)
        self.label_219 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_219.setObjectName("label_219")
        self.horizontalLayout_105.addWidget(self.label_219)
        self.verticalLayout_16.addLayout(self.horizontalLayout_105)
        self.horizontalLayout_106 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_106.setObjectName("horizontalLayout_106")
        self.label_220 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_220.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_220.setObjectName("label_220")
        self.horizontalLayout_106.addWidget(self.label_220)
        self.label_221 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_221.setObjectName("label_221")
        self.horizontalLayout_106.addWidget(self.label_221)
        self.verticalLayout_16.addLayout(self.horizontalLayout_106)
        self.horizontalLayout_107 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_107.setObjectName("horizontalLayout_107")
        self.label_222 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_222.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_222.setObjectName("label_222")
        self.horizontalLayout_107.addWidget(self.label_222)
        self.label_223 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_223.setObjectName("label_223")
        self.horizontalLayout_107.addWidget(self.label_223)
        self.verticalLayout_16.addLayout(self.horizontalLayout_107)
        self.horizontalLayout_108 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_108.setObjectName("horizontalLayout_108")
        self.label_224 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_224.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_224.setObjectName("label_224")
        self.horizontalLayout_108.addWidget(self.label_224)
        self.label_225 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_225.setObjectName("label_225")
        self.horizontalLayout_108.addWidget(self.label_225)
        self.verticalLayout_16.addLayout(self.horizontalLayout_108)
        self.horizontalLayout_109 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_109.setObjectName("horizontalLayout_109")
        self.label_226 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_226.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_226.setObjectName("label_226")
        self.horizontalLayout_109.addWidget(self.label_226)
        self.label_227 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_227.setObjectName("label_227")
        self.horizontalLayout_109.addWidget(self.label_227)
        self.verticalLayout_16.addLayout(self.horizontalLayout_109)
        self.horizontalLayout_110 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_110.setObjectName("horizontalLayout_110")
        self.label_228 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_228.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_228.setObjectName("label_228")
        self.horizontalLayout_110.addWidget(self.label_228)
        self.label_229 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_229.setObjectName("label_229")
        self.horizontalLayout_110.addWidget(self.label_229)
        self.verticalLayout_16.addLayout(self.horizontalLayout_110)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_230 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_230.setFont(font)
        self.label_230.setStyleSheet("min-height:15;\n"
"max-height:15;\n"
"background-color: rgba(0, 0, 0, 0%);")
        self.label_230.setObjectName("label_230")
        self.verticalLayout_23.addWidget(self.label_230)
        self.line_18 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_18.setStyleSheet("background-color:rgb(255, 85, 0);\n"
"border:No;\n"
"height:1px")
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.verticalLayout_23.addWidget(self.line_18)
        self.verticalLayout_16.addLayout(self.verticalLayout_23)
        self.horizontalLayout_111 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_111.setObjectName("horizontalLayout_111")
        self.label_231 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_231.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_231.setObjectName("label_231")
        self.horizontalLayout_111.addWidget(self.label_231)
        self.label_232 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_232.setObjectName("label_232")
        self.horizontalLayout_111.addWidget(self.label_232)
        self.verticalLayout_16.addLayout(self.horizontalLayout_111)
        self.horizontalLayout_112 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_112.setObjectName("horizontalLayout_112")
        self.label_233 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_233.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_233.setObjectName("label_233")
        self.horizontalLayout_112.addWidget(self.label_233)
        self.label_234 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_234.setObjectName("label_234")
        self.horizontalLayout_112.addWidget(self.label_234)
        self.verticalLayout_16.addLayout(self.horizontalLayout_112)
        self.horizontalLayout_113 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_113.setObjectName("horizontalLayout_113")
        self.label_235 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_235.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_235.setObjectName("label_235")
        self.horizontalLayout_113.addWidget(self.label_235)
        self.label_236 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_236.setObjectName("label_236")
        self.horizontalLayout_113.addWidget(self.label_236)
        self.verticalLayout_16.addLayout(self.horizontalLayout_113)
        self.horizontalLayout_114 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_114.setObjectName("horizontalLayout_114")
        self.label_237 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_237.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_237.setObjectName("label_237")
        self.horizontalLayout_114.addWidget(self.label_237)
        self.label_238 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_238.setObjectName("label_238")
        self.horizontalLayout_114.addWidget(self.label_238)
        self.verticalLayout_16.addLayout(self.horizontalLayout_114)
        self.horizontalLayout_115 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_115.setObjectName("horizontalLayout_115")
        self.label_239 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_239.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_239.setObjectName("label_239")
        self.horizontalLayout_115.addWidget(self.label_239)
        self.label_240 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_240.setObjectName("label_240")
        self.horizontalLayout_115.addWidget(self.label_240)
        self.verticalLayout_16.addLayout(self.horizontalLayout_115)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_241 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_241.setFont(font)
        self.label_241.setStyleSheet("min-height:15;\n"
"max-height:15;\n"
"background-color: rgba(0, 0, 0, 0%);")
        self.label_241.setObjectName("label_241")
        self.verticalLayout_24.addWidget(self.label_241)
        self.line_19 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_19.setStyleSheet("background-color:rgb(255, 85, 0);\n"
"border:No;\n"
"height:1px")
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.verticalLayout_24.addWidget(self.line_19)
        self.verticalLayout_16.addLayout(self.verticalLayout_24)
        self.horizontalLayout_116 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_116.setObjectName("horizontalLayout_116")
        self.label_242 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_242.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_242.setObjectName("label_242")
        self.horizontalLayout_116.addWidget(self.label_242)
        self.label_243 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_243.setObjectName("label_243")
        self.horizontalLayout_116.addWidget(self.label_243)
        self.verticalLayout_16.addLayout(self.horizontalLayout_116)
        self.horizontalLayout_117 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_117.setObjectName("horizontalLayout_117")
        self.label_244 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_244.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_244.setObjectName("label_244")
        self.horizontalLayout_117.addWidget(self.label_244)
        self.label_245 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_245.setObjectName("label_245")
        self.horizontalLayout_117.addWidget(self.label_245)
        self.verticalLayout_16.addLayout(self.horizontalLayout_117)
        self.horizontalLayout_118 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_118.setObjectName("horizontalLayout_118")
        self.label_246 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_246.setStyleSheet("min-width:100px;\n"
"max-width:100px;")
        self.label_246.setObjectName("label_246")
        self.horizontalLayout_118.addWidget(self.label_246)
        self.label_247 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_247.setObjectName("label_247")
        self.horizontalLayout_118.addWidget(self.label_247)
        self.verticalLayout_16.addLayout(self.horizontalLayout_118)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.SheetDockWidget.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.SheetDockWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyRex"))
        self.label.setText(_translate("MainWindow", "REGULAR EXPRESSION"))
        self.NoMatchesLabel.setText(_translate("MainWindow", " 0 matches or wrong syntax"))
        self.RegexTextEdit.setPlaceholderText(_translate("MainWindow", "insert your pattern"))
        self.ProcessPushButton.setText(_translate("MainWindow", "Process"))
        self.ProcessPushButton.setShortcut(_translate("MainWindow", "Return"))
        self.label_2.setText(_translate("MainWindow", "TEST STRING"))
        self.TestStringTextEdit.setPlaceholderText(_translate("MainWindow", "insert your test string here"))
        self.label_3.setText(_translate("MainWindow", "MATCH INFORMATION"))
        self.SheetDockWidget.setWindowTitle(_translate("MainWindow", "Regex Sheet"))
        self.label_126.setText(_translate("MainWindow", "Regular Expression Basics"))
        self.label_127.setText(_translate("MainWindow", "."))
        self.label_128.setText(_translate("MainWindow", "Any character except newline"))
        self.label_129.setText(_translate("MainWindow", "a"))
        self.label_130.setText(_translate("MainWindow", "The character a"))
        self.label_131.setText(_translate("MainWindow", "ab"))
        self.label_132.setText(_translate("MainWindow", "The string ab"))
        self.label_133.setText(_translate("MainWindow", "a|b"))
        self.label_134.setText(_translate("MainWindow", "a or b"))
        self.label_135.setText(_translate("MainWindow", "a*"))
        self.label_136.setText(_translate("MainWindow", "0 or more a\'s"))
        self.label_137.setText(_translate("MainWindow", "\\"))
        self.label_138.setText(_translate("MainWindow", "Escapes a special character"))
        self.label_139.setText(_translate("MainWindow", "Regular Expression Quantifiers"))
        self.label_140.setText(_translate("MainWindow", "*"))
        self.label_141.setText(_translate("MainWindow", "0 or more"))
        self.label_142.setText(_translate("MainWindow", "+"))
        self.label_143.setText(_translate("MainWindow", "1 or more"))
        self.label_144.setText(_translate("MainWindow", "?"))
        self.label_145.setText(_translate("MainWindow", "0 or 1"))
        self.label_146.setText(_translate("MainWindow", "{2}"))
        self.label_147.setText(_translate("MainWindow", "Exactly 2"))
        self.label_148.setText(_translate("MainWindow", "{2, 5}"))
        self.label_149.setText(_translate("MainWindow", "Between 2 and 5"))
        self.label_150.setText(_translate("MainWindow", "{2,}"))
        self.label_151.setText(_translate("MainWindow", "2 or more"))
        self.label_152.setText(_translate("MainWindow", "{,5}"))
        self.label_153.setText(_translate("MainWindow", "Up to 5"))
        self.label_154.setText(_translate("MainWindow", "ab"))
        self.label_155.setText(_translate("MainWindow", "The string ab"))
        self.label_156.setText(_translate("MainWindow", "Regular Expression Groups"))
        self.label_157.setText(_translate("MainWindow", "(...)"))
        self.label_158.setText(_translate("MainWindow", "Capturing group"))
        self.label_159.setText(_translate("MainWindow", "(?P<Y>...)"))
        self.label_160.setText(_translate("MainWindow", "Capturing group named Y"))
        self.label_161.setText(_translate("MainWindow", "(?:...)"))
        self.label_162.setText(_translate("MainWindow", "Non-capturing group"))
        self.label_163.setText(_translate("MainWindow", "\\Y"))
        self.label_164.setText(_translate("MainWindow", "Match the Y\'th captured group"))
        self.label_165.setText(_translate("MainWindow", "(?P=Y)"))
        self.label_166.setText(_translate("MainWindow", "Match the named group Y"))
        self.label_167.setText(_translate("MainWindow", "(?#...)"))
        self.label_168.setText(_translate("MainWindow", "Comment"))
        self.label_169.setText(_translate("MainWindow", "{2}"))
        self.label_170.setText(_translate("MainWindow", "Exactly 2"))
        self.label_171.setText(_translate("MainWindow", "Regular Expression Character Classes"))
        self.label_172.setText(_translate("MainWindow", "[ab-d]"))
        self.label_173.setText(_translate("MainWindow", "One character of: a, b, c, d"))
        self.label_174.setText(_translate("MainWindow", "[^ab-d]"))
        self.label_175.setText(_translate("MainWindow", "One character except: a, b, c, d"))
        self.label_176.setText(_translate("MainWindow", "[b]"))
        self.label_177.setText(_translate("MainWindow", "Backspace character"))
        self.label_178.setText(_translate("MainWindow", "\\d"))
        self.label_179.setText(_translate("MainWindow", "One digit"))
        self.label_180.setText(_translate("MainWindow", "\\D"))
        self.label_181.setText(_translate("MainWindow", "One non-digit"))
        self.label_182.setText(_translate("MainWindow", "\\s"))
        self.label_183.setText(_translate("MainWindow", "One whitespace"))
        self.label_184.setText(_translate("MainWindow", "\\S"))
        self.label_185.setText(_translate("MainWindow", "One non-whitespace"))
        self.label_186.setText(_translate("MainWindow", "\\w"))
        self.label_187.setText(_translate("MainWindow", "One word character"))
        self.label_188.setText(_translate("MainWindow", "\\W"))
        self.label_189.setText(_translate("MainWindow", "One non-word character"))
        self.label_190.setText(_translate("MainWindow", "Regular Expression Assertions"))
        self.label_191.setText(_translate("MainWindow", "^"))
        self.label_192.setText(_translate("MainWindow", "Start of string"))
        self.label_193.setText(_translate("MainWindow", "\\A"))
        self.label_194.setText(_translate("MainWindow", "Start of string, ignores m flag"))
        self.label_195.setText(_translate("MainWindow", "$"))
        self.label_196.setText(_translate("MainWindow", "End of string"))
        self.label_197.setText(_translate("MainWindow", "\\Z"))
        self.label_198.setText(_translate("MainWindow", "End of string, ignores m flag"))
        self.label_199.setText(_translate("MainWindow", "\\b"))
        self.label_200.setText(_translate("MainWindow", "Word boundary"))
        self.label_201.setText(_translate("MainWindow", "\\B"))
        self.label_202.setText(_translate("MainWindow", "Non-word boundary"))
        self.label_203.setText(_translate("MainWindow", "(?=...)"))
        self.label_204.setText(_translate("MainWindow", "Positive lookahead"))
        self.label_205.setText(_translate("MainWindow", "(?!...)"))
        self.label_206.setText(_translate("MainWindow", "Negative lookahead"))
        self.label_207.setText(_translate("MainWindow", "(?<=...)"))
        self.label_208.setText(_translate("MainWindow", "Positive lookbehind"))
        self.label_209.setText(_translate("MainWindow", "(?<!...)"))
        self.label_210.setText(_translate("MainWindow", "Negative lookbehind"))
        self.label_211.setText(_translate("MainWindow", "(?()|)"))
        self.label_212.setText(_translate("MainWindow", "Conditional"))
        self.label_213.setText(_translate("MainWindow", "\\Z"))
        self.label_214.setText(_translate("MainWindow", "End of string, ignores m flag"))
        self.label_215.setText(_translate("MainWindow", "Regular Expression Flags"))
        self.label_216.setText(_translate("MainWindow", "i"))
        self.label_217.setText(_translate("MainWindow", "Ignore case"))
        self.label_218.setText(_translate("MainWindow", "m"))
        self.label_219.setText(_translate("MainWindow", "^ and $ match start and end of line"))
        self.label_220.setText(_translate("MainWindow", "s"))
        self.label_221.setText(_translate("MainWindow", "Matches newline as well"))
        self.label_222.setText(_translate("MainWindow", "x"))
        self.label_223.setText(_translate("MainWindow", "Allow spaces and comments"))
        self.label_224.setText(_translate("MainWindow", "L"))
        self.label_225.setText(_translate("MainWindow", "Locale character classes"))
        self.label_226.setText(_translate("MainWindow", "u"))
        self.label_227.setText(_translate("MainWindow", "Unicode character classes"))
        self.label_228.setText(_translate("MainWindow", "(?iLmsux)"))
        self.label_229.setText(_translate("MainWindow", "Set flags within regex"))
        self.label_230.setText(_translate("MainWindow", "Regular Expression Flags"))
        self.label_231.setText(_translate("MainWindow", "\\n"))
        self.label_232.setText(_translate("MainWindow", "Newline"))
        self.label_233.setText(_translate("MainWindow", "\\r"))
        self.label_234.setText(_translate("MainWindow", "Carriage return"))
        self.label_235.setText(_translate("MainWindow", "\\t"))
        self.label_236.setText(_translate("MainWindow", "Tab"))
        self.label_237.setText(_translate("MainWindow", "\\YYY"))
        self.label_238.setText(_translate("MainWindow", "Octal character YYY"))
        self.label_239.setText(_translate("MainWindow", "\\xYY"))
        self.label_240.setText(_translate("MainWindow", "Hexadecimal character YY"))
        self.label_241.setText(_translate("MainWindow", "Regular Expression Replacement"))
        self.label_242.setText(_translate("MainWindow", "\\g<0>"))
        self.label_243.setText(_translate("MainWindow", "Insert entire match"))
        self.label_244.setText(_translate("MainWindow", "\\g<Y>"))
        self.label_245.setText(_translate("MainWindow", "Insert match Y (name or number)"))
        self.label_246.setText(_translate("MainWindow", "\\Y"))
        self.label_247.setText(_translate("MainWindow", "Insert group numbered Y"))
import src_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())