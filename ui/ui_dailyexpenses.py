# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_dailyexpenses.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 529)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.pageAdd = QtWidgets.QWidget()
        self.pageAdd.setObjectName("pageAdd")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pageAdd)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.chbCurrentDate = QtWidgets.QCheckBox(self.pageAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chbCurrentDate.sizePolicy().hasHeightForWidth())
        self.chbCurrentDate.setSizePolicy(sizePolicy)
        self.chbCurrentDate.setObjectName("chbCurrentDate")
        self.gridLayout.addWidget(self.chbCurrentDate, 7, 0, 1, 1)
        self.lblMode = QtWidgets.QLabel(self.pageAdd)
        self.lblMode.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblMode.setObjectName("lblMode")
        self.gridLayout.addWidget(self.lblMode, 3, 0, 1, 1)
        self.cbByWhom = QtWidgets.QComboBox(self.pageAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbByWhom.sizePolicy().hasHeightForWidth())
        self.cbByWhom.setSizePolicy(sizePolicy)
        self.cbByWhom.setEditable(True)
        self.cbByWhom.setObjectName("cbByWhom")
        self.gridLayout.addWidget(self.cbByWhom, 6, 1, 1, 1)
        self.lblWho = QtWidgets.QLabel(self.pageAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblWho.sizePolicy().hasHeightForWidth())
        self.lblWho.setSizePolicy(sizePolicy)
        self.lblWho.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblWho.setObjectName("lblWho")
        self.gridLayout.addWidget(self.lblWho, 6, 0, 1, 1)
        self.cbItem = QtWidgets.QComboBox(self.pageAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbItem.sizePolicy().hasHeightForWidth())
        self.cbItem.setSizePolicy(sizePolicy)
        self.cbItem.setEditable(True)
        self.cbItem.setObjectName("cbItem")
        self.gridLayout.addWidget(self.cbItem, 4, 1, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.pageAdd)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout.addWidget(self.timeEdit, 7, 3, 1, 1)
        self.lblQty = QtWidgets.QLabel(self.pageAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblQty.sizePolicy().hasHeightForWidth())
        self.lblQty.setSizePolicy(sizePolicy)
        self.lblQty.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblQty.setObjectName("lblQty")
        self.gridLayout.addWidget(self.lblQty, 5, 2, 1, 1)
        self.lblWhere = QtWidgets.QLabel(self.pageAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblWhere.sizePolicy().hasHeightForWidth())
        self.lblWhere.setSizePolicy(sizePolicy)
        self.lblWhere.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblWhere.setObjectName("lblWhere")
        self.gridLayout.addWidget(self.lblWhere, 6, 2, 1, 1)
        self.chbCurrentTime = QtWidgets.QCheckBox(self.pageAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chbCurrentTime.sizePolicy().hasHeightForWidth())
        self.chbCurrentTime.setSizePolicy(sizePolicy)
        self.chbCurrentTime.setObjectName("chbCurrentTime")
        self.gridLayout.addWidget(self.chbCurrentTime, 7, 2, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.pageAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2014, 9, 28))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 7, 1, 1, 1)
        self.cbCategory = QtWidgets.QComboBox(self.pageAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbCategory.sizePolicy().hasHeightForWidth())
        self.cbCategory.setSizePolicy(sizePolicy)
        self.cbCategory.setEditable(True)
        self.cbCategory.setObjectName("cbCategory")
        self.gridLayout.addWidget(self.cbCategory, 5, 1, 1, 1)
        self.lbCategory = QtWidgets.QLabel(self.pageAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbCategory.sizePolicy().hasHeightForWidth())
        self.lbCategory.setSizePolicy(sizePolicy)
        self.lbCategory.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbCategory.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbCategory.setObjectName("lbCategory")
        self.gridLayout.addWidget(self.lbCategory, 5, 0, 1, 1)
        self.lblCost = QtWidgets.QLabel(self.pageAdd)
        self.lblCost.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblCost.setObjectName("lblCost")
        self.gridLayout.addWidget(self.lblCost, 4, 2, 1, 1)
        self.lbItem = QtWidgets.QLabel(self.pageAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbItem.sizePolicy().hasHeightForWidth())
        self.lbItem.setSizePolicy(sizePolicy)
        self.lbItem.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbItem.setObjectName("lbItem")
        self.gridLayout.addWidget(self.lbItem, 4, 0, 1, 1)
        self.modeLayout = QtWidgets.QHBoxLayout()
        self.modeLayout.setObjectName("modeLayout")
        self.rbExpense = QtWidgets.QRadioButton(self.pageAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbExpense.sizePolicy().hasHeightForWidth())
        self.rbExpense.setSizePolicy(sizePolicy)
        self.rbExpense.setChecked(True)
        self.rbExpense.setObjectName("rbExpense")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rbExpense)
        self.modeLayout.addWidget(self.rbExpense)
        self.rbIncome = QtWidgets.QRadioButton(self.pageAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbIncome.sizePolicy().hasHeightForWidth())
        self.rbIncome.setSizePolicy(sizePolicy)
        self.rbIncome.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rbIncome.setObjectName("rbIncome")
        self.buttonGroup.addButton(self.rbIncome)
        self.modeLayout.addWidget(self.rbIncome)
        self.gridLayout.addLayout(self.modeLayout, 3, 1, 1, 1)
        self.cbCurrency = QtWidgets.QComboBox(self.pageAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbCurrency.sizePolicy().hasHeightForWidth())
        self.cbCurrency.setSizePolicy(sizePolicy)
        self.cbCurrency.setObjectName("cbCurrency")
        self.gridLayout.addWidget(self.cbCurrency, 4, 4, 1, 1)
        self.cbUnits = QtWidgets.QComboBox(self.pageAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbUnits.sizePolicy().hasHeightForWidth())
        self.cbUnits.setSizePolicy(sizePolicy)
        self.cbUnits.setObjectName("cbUnits")
        self.gridLayout.addWidget(self.cbUnits, 5, 4, 1, 1)
        self.spinboxQty = QtWidgets.QDoubleSpinBox(self.pageAdd)
        self.spinboxQty.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinboxQty.sizePolicy().hasHeightForWidth())
        self.spinboxQty.setSizePolicy(sizePolicy)
        self.spinboxQty.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinboxQty.setMaximum(999999.99)
        self.spinboxQty.setProperty("value", 1.0)
        self.spinboxQty.setObjectName("spinboxQty")
        self.gridLayout.addWidget(self.spinboxQty, 5, 3, 1, 1)
        self.spinboxMoney = QtWidgets.QDoubleSpinBox(self.pageAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinboxMoney.sizePolicy().hasHeightForWidth())
        self.spinboxMoney.setSizePolicy(sizePolicy)
        self.spinboxMoney.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinboxMoney.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinboxMoney.setMaximum(999999999.99)
        self.spinboxMoney.setObjectName("spinboxMoney")
        self.gridLayout.addWidget(self.spinboxMoney, 4, 3, 1, 1)
        self.cbWhere = QtWidgets.QComboBox(self.pageAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbWhere.sizePolicy().hasHeightForWidth())
        self.cbWhere.setSizePolicy(sizePolicy)
        self.cbWhere.setEditable(True)
        self.cbWhere.setObjectName("cbWhere")
        self.gridLayout.addWidget(self.cbWhere, 6, 3, 1, 1)
        self.cbLocation = QtWidgets.QComboBox(self.pageAdd)
        self.cbLocation.setObjectName("cbLocation")
        self.gridLayout.addWidget(self.cbLocation, 6, 4, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.textNote = QtWidgets.QPlainTextEdit(self.pageAdd)
        self.textNote.setObjectName("textNote")
        self.verticalLayout_4.addWidget(self.textNote)
        self.layoutButton = QtWidgets.QHBoxLayout()
        self.layoutButton.setObjectName("layoutButton")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutButton.addItem(spacerItem)
        self.btnAdd = QtWidgets.QPushButton(self.pageAdd)
        self.btnAdd.setObjectName("btnAdd")
        self.layoutButton.addWidget(self.btnAdd)
        self.verticalLayout_4.addLayout(self.layoutButton)
        self.tabWidget.addTab(self.pageAdd, "")
        self.pageTable = QtWidgets.QWidget()
        self.pageTable.setObjectName("pageTable")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pageTable)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableView = BalanceTable(self.pageTable)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_3.addWidget(self.tableView)
        self.tabWidget.addTab(self.pageTable, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 732, 22))
        self.menubar.setObjectName("menubar")
        self.menuDB = QtWidgets.QMenu(self.menubar)
        self.menuDB.setObjectName("menuDB")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReload = QtWidgets.QAction(MainWindow)
        self.actionReload.setObjectName("actionReload")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.menuDB.addAction(self.actionReload)
        self.menuDB.addAction(self.actionClear)
        self.menuDB.addAction(self.actionUndo)
        self.menubar.addAction(self.menuDB.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chbCurrentDate.setText(_translate("MainWindow", "current date"))
        self.lblMode.setText(_translate("MainWindow", "Mode"))
        self.lblWho.setText(_translate("MainWindow", "By whom"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.lblQty.setText(_translate("MainWindow", "qty/amount"))
        self.lblWhere.setText(_translate("MainWindow", "Where"))
        self.chbCurrentTime.setText(_translate("MainWindow", "current time"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.lbCategory.setText(_translate("MainWindow", "Category"))
        self.lblCost.setText(_translate("MainWindow", "Cost"))
        self.lbItem.setText(_translate("MainWindow", "Item"))
        self.rbExpense.setText(_translate("MainWindow", "- (expense)"))
        self.rbIncome.setText(_translate("MainWindow", "+ (income)"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pageAdd), _translate("MainWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pageTable), _translate("MainWindow", "Table"))
        self.menuDB.setTitle(_translate("MainWindow", "DB"))
        self.actionReload.setText(_translate("MainWindow", "Reload"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))

from dailyexpenses.BalanceTable import BalanceTable
