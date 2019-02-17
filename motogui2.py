from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, Qt
import os
import random
import moto_facts
import prioritizer
import re
from itertools import zip_longest
from userSelectgui import Ui_SelectUser

class Ui_MainWindow(QtWidgets.QMainWindow):
    lockDown = QtCore.pyqtSignal()
    undoLockDown = QtCore.pyqtSignal()
    exitLogger = QtCore.pyqtSignal()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 797)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mainProgramTitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.mainProgramTitle.setFont(font)
        self.mainProgramTitle.setObjectName("mainProgramTitle")
        self.gridLayout_2.addWidget(self.mainProgramTitle, 0, 1, 1, 1)
        self.verticalMainButtonLayout = QtWidgets.QVBoxLayout()
        self.verticalMainButtonLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalMainButtonLayout.setContentsMargins(3, 11, 10, 12)
        self.verticalMainButtonLayout.setSpacing(0)
        self.verticalMainButtonLayout.setObjectName("verticalMainButtonLayout")
        self.logMaintenanceButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.logMaintenanceButton.setIconSize(QtCore.QSize(20, 20))
        self.logMaintenanceButton.setAutoDefault(False)
        self.logMaintenanceButton.setDefault(True)
        self.logMaintenanceButton.setProperty("pageNumber", 1)
        self.logMaintenanceButton.setObjectName("logMaintenanceButton")
        self.verticalMainButtonLayout.addWidget(self.logMaintenanceButton)
        self.buildIssueListButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.buildIssueListButton.setProperty("pageNumber", 6)
        self.buildIssueListButton.setObjectName("buildIssueListButton")
        self.verticalMainButtonLayout.addWidget(self.buildIssueListButton)
        self.viewGarageButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.viewGarageButton.setProperty("pageNumber", 2)
        self.viewGarageButton.setObjectName("viewGarageButton")
        self.verticalMainButtonLayout.addWidget(self.viewGarageButton)
        self.troubleShootButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.troubleShootButton.setProperty("pageNumber", 3)
        self.troubleShootButton.setObjectName("checkScheduledRepairsButton")
        self.verticalMainButtonLayout.addWidget(self.troubleShootButton)
        self.rideLogButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.rideLogButton.setProperty("pageNumber", 4)
        self.rideLogButton.setObjectName("diagnoseASymptomButton")
        self.verticalMainButtonLayout.addWidget(self.rideLogButton)
        self.prioritizeActionsButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.prioritizeActionsButton.setCheckable(False)
        self.prioritizeActionsButton.setProperty("pageNumber", 5)
        self.prioritizeActionsButton.setObjectName("prioritizeActionsButton")
        self.verticalMainButtonLayout.addWidget(self.prioritizeActionsButton)
        self.gridLayout_2.addLayout(self.verticalMainButtonLayout, 0, 0, 2, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setLineWidth(1)
        self.stackedWidget.setObjectName("stackedWidget")
        self.IssueBuildingPage = QtWidgets.QWidget()
        self.IssueBuildingPage.setObjectName("IssueBuildingPage")
        self.layoutWidget = QtWidgets.QWidget(self.IssueBuildingPage)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 551, 501))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.issueListLable = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.issueListLable.setFont(font)
        self.issueListLable.setObjectName("issueListLable")
        self.gridLayout.addWidget(self.issueListLable, 3, 0, 1, 1)
        self.listOfIssues = QtWidgets.QListWidget(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listOfIssues.setFont(font)
        self.listOfIssues.setDragEnabled(True)
        self.listOfIssues.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listOfIssues.setDefaultDropAction(QtCore.Qt.ActionMask)
        self.listOfIssues.setAlternatingRowColors(True)
        self.listOfIssues.setUniformItemSizes(False)
        self.listOfIssues.setWordWrap(True)
        self.listOfIssues.setObjectName("listOfIssues")
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.gridLayout.addWidget(self.listOfIssues, 4, 0, 1, 2)
        self.issueDescripText = QtWidgets.QLineEdit(self.layoutWidget)
        self.issueDescripText.setInputMask("")
        self.issueDescripText.setText("")
        self.issueDescripText.setClearButtonEnabled(False)
        self.issueDescripText.setObjectName("issueDescripText")
        self.gridLayout.addWidget(self.issueDescripText, 1, 0, 1, 2)
        self.issueDescripLable = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.issueDescripLable.setFont(font)
        self.issueDescripLable.setObjectName("issueDescripLable")
        self.gridLayout.addWidget(self.issueDescripLable, 0, 0, 1, 1)
        self.logIssueButton = QtWidgets.QPushButton(self.layoutWidget)
        self.logIssueButton.setObjectName("logIssueButton")
        self.gridLayout.addWidget(self.logIssueButton, 5, 1, 1, 1)
        self.deleteIssueButton = QtWidgets.QPushButton(self.layoutWidget)
        self.deleteIssueButton.setCheckable(False)
        self.deleteIssueButton.setObjectName("deleteIssueButton")
        self.gridLayout.addWidget(self.deleteIssueButton, 5, 0, 1, 1)
        self.NextRepairDate = QtWidgets.QDateEdit(self.layoutWidget)
        self.NextRepairDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 2, 1), QtCore.QTime(0, 0, 0)))
        self.NextRepairDate.setMaximumDate(QtCore.QDate(7999, 12, 30))
        self.NextRepairDate.setCalendarPopup(True)
        self.NextRepairDate.setObjectName("NextRepairDate")
        self.gridLayout.addWidget(self.NextRepairDate, 3, 1, 1, 1)
        self.stackedWidget.addWidget(self.IssueBuildingPage)
        self.workLoggingPage = QtWidgets.QWidget()
        self.workLoggingPage.setObjectName("workLoggingPage")
        self.gridLayoutWidget = QtWidgets.QWidget(self.workLoggingPage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 551, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.logWorkLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.logWorkLabel.setFont(font)
        self.logWorkLabel.setObjectName("logWorkLabel")
        self.gridLayout_3.addWidget(self.logWorkLabel, 0, 0, 1, 1)
        self.deleteWorkButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.deleteWorkButton.setCheckable(False)
        self.deleteWorkButton.setObjectName("deleteWorkButton")
        self.gridLayout_3.addWidget(self.deleteWorkButton, 3, 0, 1, 1)
        self.logWorkButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.logWorkButton.setObjectName("logWorkButton")
        self.gridLayout_3.addWidget(self.logWorkButton, 3, 1, 1, 1)
        self.listOfLoggedWork = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listOfLoggedWork.setAlternatingRowColors(False)
        self.listOfLoggedWork.setWordWrap(True)
        self.listOfLoggedWork.setAlternatingRowColors(True)
        self.listOfLoggedWork.setObjectName("listOfLoggedWork")
        self.gridLayout_3.addWidget(self.listOfLoggedWork, 2, 0, 1, 2)
        self.maintenanceDescriptLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.maintenanceDescriptLineEdit.setText("")
        self.maintenanceDescriptLineEdit.setObjectName("maintenanceDescriptLineEdit")
        self.gridLayout_3.addWidget(self.maintenanceDescriptLineEdit, 1, 0, 1, 2)
        self.stackedWidget.addWidget(self.workLoggingPage)
        self.garagePage = QtWidgets.QWidget()
        self.garagePage.setObjectName("garagePage")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.garagePage)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 551, 501))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.yourGarageLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.yourGarageLabel.setFont(font)
        self.yourGarageLabel.setObjectName("yourGarageLabel")
        self.gridLayout_5.addWidget(self.yourGarageLabel, 0, 0, 1, 1)
        self.listOfBikes = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.listOfBikes.setWordWrap(True)
        self.listOfBikes.setAlternatingRowColors(True)
        self.listOfBikes.setObjectName("listOfBikes")
        self.gridLayout_5.addWidget(self.listOfBikes, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_5.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.removeBikeButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.removeBikeButton.setObjectName("removeBikeButton")
        self.gridLayout_5.addWidget(self.removeBikeButton, 3, 0, 1, 1)
        self.stackedWidget.addWidget(self.garagePage)
        self.scheduleRepairsPage = QtWidgets.QWidget()
        self.scheduleRepairsPage.setObjectName("scheduleRepairsPage")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.scheduleRepairsPage)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 551, 501))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.nextRepairDateLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nextRepairDateLabel.setFont(font)
        self.nextRepairDateLabel.setObjectName("nextRepairDateLabel")
        self.gridLayout_6.addWidget(self.nextRepairDateLabel, 0, 0, 1, 1)
        self.suggestedDatesTable = QtWidgets.QTableWidget(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.suggestedDatesTable.setFont(font)
        self.suggestedDatesTable.setAutoFillBackground(False)
        self.suggestedDatesTable.setWordWrap(True)
        self.suggestedDatesTable.setColumnCount(2)
        self.suggestedDatesTable.setObjectName("suggestedDatesTable")
        self.suggestedDatesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.suggestedDatesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.suggestedDatesTable.setHorizontalHeaderItem(1, item)
        self.suggestedDatesTable.horizontalHeader().setVisible(False)
        self.suggestedDatesTable.horizontalHeader().setCascadingSectionResizes(False)
        self.suggestedDatesTable.horizontalHeader().setDefaultSectionSize(190)
        self.gridLayout_6.addWidget(self.suggestedDatesTable, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.scheduleRepairsPage)
        self.symptomDiagoserPage = QtWidgets.QWidget()
        self.symptomDiagoserPage.setObjectName("symptomDiagoserPage")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.symptomDiagoserPage)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 551, 461))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.diagnoseLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.diagnoseLabel.setFont(font)
        self.diagnoseLabel.setObjectName("diagnoseLabel")
        self.gridLayout_7.addWidget(self.diagnoseLabel, 0, 0, 1, 1)
        self.listOfSymptoms = QtWidgets.QListWidget(self.gridLayoutWidget_4)
        self.listOfSymptoms.setMovement(QtWidgets.QListView.Static)
        self.listOfSymptoms.setResizeMode(QtWidgets.QListView.Fixed)
        self.listOfSymptoms.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listOfSymptoms.setSelectionRectVisible(False)
        self.listOfSymptoms.setObjectName("listOfSymptoms")
        item = QtWidgets.QListWidgetItem()
        self.listOfSymptoms.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfSymptoms.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfSymptoms.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfSymptoms.addItem(item)
        self.gridLayout_7.addWidget(self.listOfSymptoms, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget_4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_7.addWidget(self.line, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.symptomDiagoserPage)
        self.prioritizerPage = QtWidgets.QWidget()
        self.prioritizerPage.setObjectName("prioritizerPage")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.prioritizerPage)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 551, 501))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.listOfPrioritizedIssues = QtWidgets.QListWidget(self.gridLayoutWidget_5)
        self.listOfPrioritizedIssues.setWordWrap(True)
        self.listOfPrioritizedIssues.setAlternatingRowColors(True)
        self.listOfPrioritizedIssues.setObjectName("listOfPrioritizedIssues")
        self.gridLayout_9.addWidget(self.listOfPrioritizedIssues, 1, 0, 1, 1)
        self.prioritizeLabel = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.prioritizeLabel.setFont(font)
        self.prioritizeLabel.setObjectName("prioritizeLabel")
        self.gridLayout_9.addWidget(self.prioritizeLabel, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.prioritizerPage)
        self.beforeEveryRidePage = QtWidgets.QWidget()
        self.beforeEveryRidePage.setProperty("pageNumber", 7)
        self.beforeEveryRidePage.setObjectName("beforeEveryRidePage")
        self.preRideCheckList = QtWidgets.QTextEdit(self.beforeEveryRidePage)
        self.preRideCheckList.setGeometry(QtCore.QRect(10, 50, 551, 551))
        self.preRideCheckList.setFrameShadow(QtWidgets.QFrame.Plain)
        self.preRideCheckList.setReadOnly(True)
        self.preRideCheckList.setObjectName("preRideCheckList")
        self.beforeRideLabel = QtWidgets.QLabel(self.beforeEveryRidePage)
        self.beforeRideLabel.setGeometry(QtCore.QRect(150, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.beforeRideLabel.setFont(font)
        self.beforeRideLabel.setObjectName("beforeRideLabel")
        self.stackedWidget.addWidget(self.beforeEveryRidePage)
        self.lastLoggedPage = QtWidgets.QWidget()
        self.lastLoggedPage.setObjectName("lastLoggedPage")
        self.lastLogLabel = QtWidgets.QLabel(self.lastLoggedPage)
        self.lastLogLabel.setGeometry(QtCore.QRect(10, 10, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lastLogLabel.setFont(font)
        self.lastLogLabel.setObjectName("lastLogLabel")
        self.listOfLastLoggedDates = QtWidgets.QListWidget(self.lastLoggedPage)
        self.listOfLastLoggedDates.setGeometry(QtCore.QRect(0, 110, 551, 391))
        self.listOfLastLoggedDates.setWordWrap(True)
        self.listOfLastLoggedDates.setAlternatingRowColors(True)
        self.listOfLastLoggedDates.setObjectName("listOfLastLoggedDates")
        self.lookUpLabel = QtWidgets.QLabel(self.lastLoggedPage)
        self.lookUpLabel.setGeometry(QtCore.QRect(40, 70, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(7.5)
        font.setBold(True)
        font.setWeight(75)
        self.lookUpLabel.setFont(font)
        self.lookUpLabel.setObjectName("lookUpLabel")
        self.lookUpDescription = QtWidgets.QLineEdit(self.lastLoggedPage)
        self.lookUpDescription.setGeometry(QtCore.QRect(180, 70, 371, 25))
        self.lookUpDescription.setObjectName("lookUpDescription")
        self.stackedWidget.addWidget(self.lastLoggedPage)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.treeWidget = QtWidgets.QTreeWidget(self.page)
        self.treeWidget.setGeometry(QtCore.QRect(10, 20, 581, 471))  #531 originally
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)  # CARBURETOR ISSUES
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)  # CLUTCH ISSUES
        item_1 = QtWidgets.QTreeWidgetItem(item_0)  # Clutch Slipping
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)  # Clutch Dragging
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)  # Excessive Clutch Noise
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)  # TRANSMISSION ISSUES
        item_1 = QtWidgets.QTreeWidgetItem(item_0)  # "Check Clutch for issues first"
        item_1 = QtWidgets.QTreeWidgetItem(item_0)  # Main Transmission problems
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)  # EMERGENCE ISSUES
        item_1 = QtWidgets.QTreeWidgetItem(item_0)  # "Engine Won't Start" 2nd level
        item_2 = QtWidgets.QTreeWidgetItem(item_1)  # engine has spark
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)  # engine does not have spark
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)


        self.diagnoseLabel_2 = QtWidgets.QLabel(self.page)
        self.diagnoseLabel_2.setGeometry(QtCore.QRect(0, 0, 549, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.diagnoseLabel_2.setFont(font)
        self.diagnoseLabel_2.setObjectName("diagnoseLabel_2")
        self.stackedWidget.addWidget(self.page)
        self.rideLogPage = QtWidgets.QWidget()
        self.rideLogPage.setObjectName("rideLogPage")
        self.layoutWidget_2 = QtWidgets.QWidget(self.rideLogPage)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 0, 551, 501))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setVerticalSpacing(12)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.logLable = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.logLable.setFont(font)
        self.logLable.setObjectName("logLable")
        self.gridLayout_4.addWidget(self.logLable, 3, 0, 1, 1)
        self.listOfLoggedRides = QtWidgets.QListWidget(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listOfLoggedRides.setFont(font)
        self.listOfLoggedRides.setAccessibleDescription("")
        self.listOfLoggedRides.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listOfLoggedRides.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.listOfLoggedRides.setProperty("showDropIndicator", False)
        self.listOfLoggedRides.setDragEnabled(False)
        self.listOfLoggedRides.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listOfLoggedRides.setDefaultDropAction(QtCore.Qt.ActionMask)
        self.listOfLoggedRides.setAlternatingRowColors(True)
        self.listOfLoggedRides.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listOfLoggedRides.setProperty("isWrapping", False)
        self.listOfLoggedRides.setUniformItemSizes(False)
        self.listOfLoggedRides.setWordWrap(True)
        self.listOfLoggedRides.setObjectName("listOfLoggedRides")
        self.gridLayout_4.addWidget(self.listOfLoggedRides, 4, 0, 1, 2)
        self.descripOfRide = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.descripOfRide.setFont(font)
        self.descripOfRide.setInputMask("")
        self.descripOfRide.setText("")
        self.descripOfRide.setClearButtonEnabled(False)
        self.descripOfRide.setObjectName("descripOfRide")
        self.gridLayout_4.addWidget(self.descripOfRide, 1, 0, 1, 2)
        self.rideLogLable = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rideLogLable.setFont(font)
        self.rideLogLable.setObjectName("rideLogLable")
        self.gridLayout_4.addWidget(self.rideLogLable, 0, 0, 1, 1)
        self.logrideButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.logrideButton.setObjectName("logrideButton")
        self.gridLayout_4.addWidget(self.logrideButton, 5, 1, 1, 1)
        self.deleteLogItemButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.deleteLogItemButton.setCheckable(False)
        self.deleteLogItemButton.setObjectName("deleteLogItemButton")
        self.gridLayout_4.addWidget(self.deleteLogItemButton, 5, 0, 1, 1)
        self.stackedWidget.addWidget(self.rideLogPage)
        self.gridLayout_2.addWidget(self.stackedWidget, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuManage = QtWidgets.QMenu(self.menubar)
        self.menuManage.setObjectName("menuManage")
        self.menuTheme = QtWidgets.QMenu(self.menubar)
        self.menuTheme.setObjectName("menuTheme")
        self.menuChoose_Theme = QtWidgets.QMenu(self.menuTheme)
        self.menuChoose_Theme.setObjectName("menuChoose_Theme")
        self.menuTips = QtWidgets.QMenu(self.menubar)
        self.menuTips.setObjectName("menuTips")
        self.menuHelpful_Reminders = QtWidgets.QMenu(self.menuTips)
        self.menuHelpful_Reminders.setObjectName("menuHelpful_Reminders")
        self.menuMaintenance_Schedule = QtWidgets.QMenu(self.menuTips)
        self.menuMaintenance_Schedule.setObjectName("menuMaintenance_Schedule")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSwitch_User = QtWidgets.QAction(MainWindow)
        self.actionSwitch_User.setObjectName("actionSwitch_User")
        self.actionIssue_List = QtWidgets.QAction(MainWindow)
        self.actionIssue_List.setObjectName("actionIssue_List")
        self.actionLog_Maintenance = QtWidgets.QAction(MainWindow)
        self.actionLog_Maintenance.setObjectName("actionLog_Maintenance")
        self.actionView_Garage = QtWidgets.QAction(MainWindow)
        self.actionView_Garage.setObjectName("actionView_Garage")
        self.actionBefore_Every_Ride_Checks = QtWidgets.QAction(MainWindow)
        self.actionBefore_Every_Ride_Checks.setProperty("pageNumber", 7)
        self.actionBefore_Every_Ride_Checks.setObjectName("actionBefore_Every_Ride_Checks")
        self.actionSymptom_Diagnoser = QtWidgets.QAction(MainWindow)
        self.actionSymptom_Diagnoser.setObjectName("actionSymptom_Diagnoser")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionLast_Logged = QtWidgets.QAction(MainWindow)
        self.actionLast_Logged.setProperty("pageNumber", 8)
        self.actionLast_Logged.setObjectName("actionLast_Logged")
        self.actionUpcoming = QtWidgets.QAction(MainWindow)
        self.actionUpcoming.setObjectName("actionUpcoming")
        self.actionPast_Due = QtWidgets.QAction(MainWindow)
        self.actionPast_Due.setObjectName("actionPast_Due")
        self.actionKawasaki = QtWidgets.QAction(MainWindow)
        self.actionKawasaki.setObjectName("actionKawasaki")
        self.actionHonda = QtWidgets.QAction(MainWindow)
        self.actionHonda.setObjectName("actionHonda")
        self.actionYamaha = QtWidgets.QAction(MainWindow)
        self.actionYamaha.setObjectName("actionYamaha")
        self.actionHarley_Davidson = QtWidgets.QAction(MainWindow)
        self.actionHarley_Davidson.setObjectName("actionHarley_Davidson")
        self.actionLog_Ride = QtWidgets.QAction(MainWindow)
        self.actionLog_Ride.setObjectName("actionLog_Ride")
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSwitch_User)
        self.menuFile.addAction(self.actionExit)
        self.menuManage.addAction(self.actionIssue_List)
        self.menuManage.addAction(self.actionLog_Maintenance)
        self.menuManage.addAction(self.actionView_Garage)
        self.menuManage.addAction(self.actionLast_Logged)
        self.menuManage.addAction(self.actionLog_Ride)
        self.menuChoose_Theme.addAction(self.actionKawasaki)
        self.menuChoose_Theme.addAction(self.actionHonda)
        self.menuChoose_Theme.addAction(self.actionYamaha)
        self.menuChoose_Theme.addAction(self.actionHarley_Davidson)
        self.menuTheme.addAction(self.menuChoose_Theme.menuAction())
        self.menuHelpful_Reminders.addAction(self.actionBefore_Every_Ride_Checks)
        self.menuMaintenance_Schedule.addAction(self.actionUpcoming)
        self.menuMaintenance_Schedule.addAction(self.actionPast_Due)
        self.menuTips.addAction(self.menuHelpful_Reminders.menuAction())
        self.menuTips.addAction(self.actionSymptom_Diagnoser)
        self.menuTips.addAction(self.menuMaintenance_Schedule.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuManage.menuAction())
        self.menubar.addAction(self.menuTheme.menuAction())
        self.menubar.addAction(self.menuTips.menuAction())

        self.retranslateUi(MainWindow)

        # Begin Logic and Connections !!!
        MainWindow.setWindowTitle("Moto-Maintenance Logger")

        self.userSwitchView()
        MainWindow.setEnabled(False)
        # connect signals to appropriate slots
        self.undoLockDown.connect(lambda: self.unlock(MainWindow))
        self.lockDown.connect(lambda: self.lock(MainWindow))
        self.exitLogger.connect(lambda: self.closeAll(MainWindow))

        self.actionSwitch_User.triggered.connect(self.switchUserAfter)
        self.actionSymptom_Diagnoser.triggered.connect(self.switchEight)

        # QAction connections
        self.actionLast_Logged.triggered.connect(self.switchSeven)
        self.actionBefore_Every_Ride_Checks.triggered.connect(self.switchSix)
        self.actionExit.triggered.connect(self.close)

        # show random moto fact
        info = QtWidgets.QMessageBox
        info.about(self.centralwidget,  "Random Motorcycle Fact!", random.choice(moto_facts.random_fact))

        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # stacked widget index changing
        self.buildIssueListButton.clicked.connect(self.switchZero)
        self.logMaintenanceButton.clicked.connect(self.switchOne)
        self.viewGarageButton.clicked.connect(self.switchTwo)
        self.prioritizeActionsButton.clicked.connect(self.switchFive)
        self.troubleShootButton.clicked.connect(self.switchEight)
        self.rideLogButton.clicked.connect(self.switchNine)

        # "last logged look up" connections
        self.lookUpDescription.textEdited.connect(self.lookUpLog)
        self.actionLast_Logged.triggered.connect(self.switchSeven)
        os.chdir('..')  # level up necessary

        # ride log list connections
        self.descripOfRide.returnPressed.connect(self.logRide)
        self.logrideButton.clicked.connect(self.logRide)
        self.deleteLogItemButton.clicked.connect(self.removeRide)
        self.actionLog_Ride.triggered.connect(self.switchNine)

        # my garage list connections
        self.lineEdit.returnPressed.connect(self.addBike)  # holds on to bike name typed
        self.removeBikeButton.clicked.connect(self.removeBike)  # button to delete a bike
        self.actionView_Garage.triggered.connect(self.switchTwo)

        # work log list connections
        self.maintenanceDescriptLineEdit.returnPressed.connect(self.logWorkToFile)
        self.logWorkButton.clicked.connect(self.logWorkToFile)
        self.deleteWorkButton.clicked.connect(self.removeFromLog)
        self.actionLog_Maintenance.triggered.connect(self.switchOne)

        # user built issue list connections
        self.issueDescripText.returnPressed.connect(self.submit)
        self.logIssueButton.clicked.connect(self.logIssue)
        self.deleteIssueButton.clicked.connect(self.removeIssue)
        self.actionIssue_List.triggered.connect(self.switchZero)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def unlock(self, mainWin):
        mainWin.setEnabled(True)

    def lock(self, mainWin):
        mainWin.setEnabled(False)

    def closeAll(self, mainWin):
        mainWin.close()

    def endMyLife(self):
        self.exitLogger.emit()

    def switchUserAfter(self):
        os.chdir('..')
        os.chdir('..')
        self.clearCurrentData()
        self.lockDown.emit()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SelectUser()
        self.ui.setup_Ui(self.window)
        self.ui.userCreateButton.clicked.connect(lambda: self.initInfo(self.window))
        self.ui.userSelectButtonBox.accepted.connect(lambda: self.initInfo(self.window))
        self.ui.userSelectButtonBox.rejected.connect(self.endMyLife)
        self.ui.userSelectButtonBox.rejected.connect(lambda: self.closeAll(self.window))
        os.chdir('..')
        self.window.show()

    def userSwitchView(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SelectUser()
        self.ui.setup_Ui(self.window)
        self.ui.userCreateButton.clicked.connect(lambda: self.initInfo(self.window))
        self.ui.userSelectButtonBox.accepted.connect(lambda: self.initInfo(self.window))
        self.ui.userSelectButtonBox.rejected.connect(self.endMyLife)
        self.ui.userSelectButtonBox.rejected.connect(lambda: self.closeAll(self.window))

        self.window.show()
        return self.window

    def clearCurrentData(self):
        self.listOfLoggedWork.clear()
        self.listOfIssues.clear()
        self.listOfBikes.clear()
        self.listOfLastLoggedDates.clear()
        self.listOfLoggedRides.clear()

    # for initializing a users lists of info from files
    def initInfo(self, mainwin):
        mainwin.close()
        self.undoLockDown.emit()
        self.clearCurrentData()
        self.stackedWidget.setCurrentIndex(1)

        # begin my-garage feature
        with open('my-garage.txt') as f:
            for line in f:
                stripped = line.rstrip()
                item = QtWidgets.QListWidgetItem(stripped, self.listOfBikes)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.listOfBikes.addItem(item)

        # end my-garage feature

        # begin work performed logging
        with open('work-log.txt') as f:
            for line in f:
                stripped = line.rstrip()
                self.listOfLoggedWork.addItem(stripped)
        # end work performed logging

        # begin user built issue list
        with open('issue-list.txt') as f:
            for line in f:
                stripped = line.rstrip()
                item = QtWidgets.QListWidgetItem(stripped, self.listOfIssues)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.listOfIssues.addItem(item)

        # begin ride log list
        with open('ride-log.txt') as f:
            for line in f:
                stripped = line.rstrip()
                self.listOfLoggedRides.addItem(stripped)
        # end ride log list

    def submit(self):
        file = open('issue-list.txt', 'a')
        file.write(self.issueDescripText.text() + '\r')
        issue = self.issueDescripText.text()
        item = QtWidgets.QListWidgetItem(issue, self.listOfIssues)
        item.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.issueDescripText.clear()
        file.close()

    # for logging an item already on the list
    def logIssue(self):
        file = open('work-log.txt', 'a')
        issueFile = open('issue-list.txt', 'w')
        date = QDate.currentDate()
        for index in range(self.listOfIssues.count()):
            if self.listOfIssues.item(index).checkState() != Qt.Checked:
                issueFile.write(self.listOfIssues.item(index).text() + '\r')
            else:
                file.write(self.listOfIssues.item(index).text() + ' - ' + date.toString(Qt.ISODate) + '\r')

        file.close()
        issueFile.close()
        self.listOfIssues.clear()

        with open('issue-list.txt') as f:
            for line in f:
                stripped = line.rstrip()
                item = QtWidgets.QListWidgetItem(stripped, self.listOfIssues)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.listOfIssues.addItem(item)

    def removeIssue(self):
        file = open('issue-list.txt', 'w')
        for index in range(self.listOfIssues.count()):
            if self.listOfIssues.item(index).checkState() != Qt.Checked:
                file.write(self.listOfIssues.item(index).text() + '\r')
        file.close()
        self.listOfIssues.clear()

        with open('issue-list.txt') as f:
            for line in f:
                stripped = line.rstrip()
                item = QtWidgets.QListWidgetItem(stripped, self.listOfIssues)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.listOfIssues.addItem(item)

    # FOR WORK PERFORMED LOGGING
    def logWorkToFile(self):
        file = open('work-log.txt', 'a')
        date = QDate.currentDate()
        if self.maintenanceDescriptLineEdit.text() != "":  # make sure we don't log an empty description
            file.write(self.maintenanceDescriptLineEdit.text() + ' - ' + date.toString(Qt.ISODate) + '\r')
            file.close()
            self.listOfLoggedWork.addItem(self.maintenanceDescriptLineEdit.text() + ' - ' + date.toString(Qt.ISODate))
            self.maintenanceDescriptLineEdit.clear()

        # FOR WORK PERFORMED LOGGING

    def removeFromLog(self):
        if self.listOfLoggedWork.currentItem():
            file = open('work-log.txt', 'r')
            lines = file.readlines()
            file.close()
            updatedLog = []
            file = open('work-log.txt', 'w')

            for line in lines:
                if self.listOfLoggedWork.currentItem().text() not in line:
                    updatedLog.append(line.rstrip())
                    file.write(line)
            file.close()
            self.listOfLoggedWork.clear()
            self.listOfLoggedWork.addItems(updatedLog)


    # my-garage feature
    def addBike(self):
        if self.lineEdit.text() != "":
            file = open('my-garage.txt', 'a')  # do I have a reason to put today's the date in issue file?
            file.write(self.lineEdit.text() + '\r')  # ' - ' + QDate.currentDate().toString(Qt.ISODate) + '\r')
            self.listOfBikes.addItem(self.lineEdit.text())
            self.lineEdit.clear()
            file.close()

    # my garage feature
    def removeBike(self):
        if self.listOfBikes.currentItem():
            file = open('my-garage.txt', 'r')
            lines = file.readlines()
            file.close()
            updatedLog = []
            file = open('my-garage.txt', 'w')
            for line in lines:
                if self.listOfBikes.currentItem().text() not in line:  # not in line:
                    updatedLog.append(line.rstrip())
                    file.write(line)
            file.close()
            self.listOfBikes.clear()
            self.listOfBikes.addItems(updatedLog)

    # ride log feature
    def logRide(self):
        if self.descripOfRide.text() != "":
            file = open('ride-log.txt', 'a')
            date = QDate.currentDate()
            file.write(self.descripOfRide.text() + ' - ' + date.toString(Qt.ISODate) + '\r')
            file.close()
            self.listOfLoggedRides.addItem(self.descripOfRide.text() + ' - ' + date.toString(Qt.ISODate))
            self.descripOfRide.clear()

    # ride log feature
    def removeRide(self):
        if self.listOfLoggedRides.currentItem():  # make sure that we have selected an item to delete
            file = open('ride-log.txt', 'r')
            lines = file.readlines()
            file.close()
            updatedLog = []
            file = open('ride-log.txt', 'w')
            for line in lines:
                if self.listOfLoggedRides.currentItem().text() not in line:
                    updatedLog.append(line.rstrip())
                    file.write(line)
            file.close()
            self.listOfLoggedRides.clear()
            self.listOfLoggedRides.addItems(updatedLog)

    # last logged feature
    def lookUpLog(self):
        self.listOfLastLoggedDates.clear()
        if self.lookUpDescription.text() != "":
            typed = self.lookUpDescription.text()
        else:
            typed = ' '  # initialize the list regardless
        pat = '.*' + re.escape(typed) + '.*'  # searching for this
        pattern = re.compile(pat, re.IGNORECASE)
        results = []
        str = ''

        with open('work-log.txt') as f:
            for line in f:
                result = pattern.search(line)
                if result:
                    results.append(line.rstrip())  # put matched lines into array

        for line in results:
            str += line + '-'   # build a string out of the results for the grouper function

        list_of_expected_dates = re.split('-|\\n', str)
        Q_Dates = []
        now = QDate.currentDate()  # today's date
        args = [iter(list_of_expected_dates)] * 4
        list = zip_longest(fillvalue=None, *args)

        descrip = []
        # group the function up and create QDate objects out of our text dates, put them in list Q_Dates
        for description, year, month, day in list:
            if day is None:
                break
            a_date = QDate(int(year), int(month), int(day))
            Q_Dates.append(a_date)  # get date as QDate object
            descrip.append(description)  # get description with it

        descripWithDates = []
        for then, line in zip(Q_Dates, descrip):
            descripWithDates.append(line + 'performed ' + now.daysTo(then).__abs__().__str__() + ' days ago')
        self.listOfLastLoggedDates.addItems(descripWithDates)

    def switchZero(self):
        self.listOfIssues.clear()
        with open('issue-list.txt') as f:
            for line in f:
                stripped = line.rstrip()
                item = QtWidgets.QListWidgetItem(stripped, self.listOfIssues)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.listOfIssues.addItem(item)
        self.stackedWidget.setCurrentIndex(0)

    def switchOne(self):
        self.listOfLoggedWork.clear()
        with open('work-log.txt') as f:
            for line in f:
                stripped = line.rstrip()
                self.listOfLoggedWork.addItem(stripped)
        self.stackedWidget.setCurrentIndex(1)

    def switchTwo(self):
        self.listOfBikes.clear()
        with open('my-garage.txt') as f:
            for line in f:
                stripped = line.rstrip()
                self.listOfBikes.addItem(stripped)
        self.stackedWidget.setCurrentIndex(2)

    def switchFive(self):
        self.stackedWidget.setCurrentIndex(5)
        file = open('issue-list.txt', 'r')
        lines = file.readlines()
        file.close()
        issues = []
        for line in lines:
            issues.append(line.rstrip())

        orderedList = prioritizer.prioritize(issues)
        self.listOfPrioritizedIssues.clear()
        list1 = [i[0] for i in orderedList]  #
        highToLow = list1.__reversed__()
        self.listOfPrioritizedIssues.addItems(highToLow)

    # Before Every Ride Checks
    def switchSix(self):
        self.stackedWidget.setCurrentIndex(6)

    # Look up last logged
    def switchSeven(self):
        self.lookUpLog()
        self.stackedWidget.setCurrentIndex(7)

    def switchEight(self):
        self.stackedWidget.setCurrentIndex(8)

    def switchNine(self):
        self.listOfLoggedRides.clear()

        with open('ride-log.txt') as f:
            for line in f:
                stripped = line.rstrip()
                self.listOfLoggedRides.addItem(stripped)
        self.stackedWidget.setCurrentIndex(9)

    # End Logic !!!

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainProgramTitle.setText(_translate("MainWindow", "MOTO-MAINTENANCE LOGGER"))
        self.logMaintenanceButton.setText(_translate("MainWindow", "Log Maintenance"))
        self.logMaintenanceButton.setDescription(_translate("MainWindow", "keep track of your work"))
        self.buildIssueListButton.setText(_translate("MainWindow", "Build Issue List"))
        self.buildIssueListButton.setDescription(_translate("MainWindow", "put together a list of work that needs to be done"))
        self.viewGarageButton.setText(_translate("MainWindow", "View Garage"))
        self.viewGarageButton.setDescription(_translate("MainWindow", "view all of your machines and choose which one to work on"))
        self.troubleShootButton.setText(_translate("MainWindow", "Troubleshoot Issues"))
        self.troubleShootButton.setDescription(_translate("MainWindow", "use simple drop down selection to figure out what\'s going wrong"))
        self.rideLogButton.setText(_translate("MainWindow", "Log a Ride"))
        self.rideLogButton.setDescription(_translate("MainWindow", "take note of your recent rides so you don't forget"))
        self.prioritizeActionsButton.setText(_translate("MainWindow", "Generate Course of Action"))
        self.prioritizeActionsButton.setDescription(_translate("MainWindow", "find out what you should do first and what can wait"))
        self.issueListLable.setText(_translate("MainWindow", "Issue List"))
        self.listOfIssues.setToolTip(_translate("MainWindow", "<html><head/><body><p>Check off issues that you want to log as performed or that you want to remove from your list.</p></body></html>"))
        self.listOfIssues.setSortingEnabled(False)
        __sortingEnabled = self.listOfIssues.isSortingEnabled()
        self.listOfIssues.setSortingEnabled(False)
        self.listOfIssues.setSortingEnabled(__sortingEnabled)
        self.issueDescripText.setToolTip(_translate("MainWindow", "<html><head/><body><p>Provide a short description of the issues that needs addressing.</p></body></html>"))
        self.issueDescripText.setPlaceholderText(_translate("MainWindow", "enter a short description of the issue"))
        self.issueDescripLable.setText(_translate("MainWindow", "Issue Description"))
        self.logIssueButton.setText(_translate("MainWindow", "Log Issue"))  # ISSUE LIST BUTTON
        self.deleteIssueButton.setText(_translate("MainWindow", "Delete Issue"))
        self.NextRepairDate.setToolTip(_translate("MainWindow", "Schedule date of the next repair"))
        self.NextRepairDate.setDisplayFormat(_translate("MainWindow", "yy/M/d"))
        self.logWorkLabel.setText(_translate("MainWindow", "Log work performed"))
        self.deleteWorkButton.setText(_translate("MainWindow", "Delete Issue"))
        self.logWorkButton.setText(_translate("MainWindow", "Log Work"))  # WORK LOGGING BUTTON
        self.maintenanceDescriptLineEdit.setPlaceholderText(_translate("MainWindow", "enter a description of the maintenance you performed"))
        self.yourGarageLabel.setText(_translate("MainWindow", "Your Garage"))
        self.listOfBikes.setToolTip(_translate("MainWindow", "<html><head/><body><p>Double click on the bike whose data you would like to mount!</p></body></html>"))
        __sortingEnabled = self.listOfBikes.isSortingEnabled()
        self.listOfBikes.setSortingEnabled(False)
        self.listOfBikes.setSortingEnabled(__sortingEnabled)
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Hit enter after you\'re finished typing to add a motorcycle to the list.</p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "enter a motorcycle to add to your garage"))
        self.removeBikeButton.setText(_translate("MainWindow", "Delete Bike"))
        self.nextRepairDateLabel.setText(_translate("MainWindow", "Suggested Scheduled Repairs"))
        item = self.suggestedDatesTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Work Description"))
        item = self.suggestedDatesTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Suggested Next Date"))
        self.diagnoseLabel.setText(_translate("MainWindow", "Troubleshoot Symptoms to Diagnose Issues"))
        __sortingEnabled = self.listOfSymptoms.isSortingEnabled()
        self.listOfSymptoms.setSortingEnabled(False)
        item = self.listOfSymptoms.item(0)
        item.setText(_translate("MainWindow", "Engine Issues"))
        item = self.listOfSymptoms.item(1)
        item.setText(_translate("MainWindow", "Carbureator Issues"))
        item = self.listOfSymptoms.item(2)
        item.setText(_translate("MainWindow", "Exhaust Issues"))
        self.listOfSymptoms.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listOfPrioritizedIssues.isSortingEnabled()
        self.listOfPrioritizedIssues.setSortingEnabled(False)
        self.listOfPrioritizedIssues.setSortingEnabled(__sortingEnabled)
        self.prioritizeLabel.setText(_translate("MainWindow", "Suggested Course of Action Based on Calculated Priority Levels"))
        self.preRideCheckList.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Below is a list of things to do before setting out on a ride.</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Walk around the motorcycle and look for any thing that seems out of place, such as leaking fluids.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Look to see how much fuel is in your tank, if it is not equipped with a fuel guage.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Check your engine oil level.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Visually inspect your drivetrain for any obvious defects.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Check your throttle and clutch cabel play for appropriate tension.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Test your breaks to make sure they are responsive. </li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Check to make sure your tires are inflated to specification.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Make sure that all of your lights are working.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Don\'t forget to wear your helmet and have it properly secured on your head!</li></ul></body></html>"))
        self.beforeRideLabel.setText(_translate("MainWindow", "\"Before Every Ride\" Check List"))
        self.lastLogLabel.setText(_translate("MainWindow", "Last Logged Reference/Lookup"))
        self.lookUpLabel.setText(_translate("MainWindow", "Look Up Repair"))
        self.lookUpDescription.setPlaceholderText(_translate("MainWindow", "enter the name of previous work completed"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "ISSUE TROUBLE SHOOTER"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Carbuerator Issues"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Bad Idling"))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("MainWindow", "a) check any vaccume lines for leaking air"))
        self.treeWidget.topLevelItem(0).child(0).child(1).setText(0, _translate("MainWindow", "b) Check air/fuel mixture"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Bad Fuel Economy"))
        self.treeWidget.topLevelItem(0).child(1).child(0).setText(0, _translate("MainWindow", "a) check air/fuel mixture"))
        self.treeWidget.topLevelItem(0).child(1).child(1).setText(0, _translate("MainWindow", "b) check sparkplug conditions"))
        self.treeWidget.topLevelItem(0).child(1).child(2).setText(0, _translate("MainWindow", "c) check fuel system for blockage"))

        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Clutch Issues"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "Clutch Slipping"))
        self.treeWidget.topLevelItem(1).child(0).child(0).setText(0, _translate("MainWindow", "a) Incorrect clutch adjustment"))
        self.treeWidget.topLevelItem(1).child(0).child(1).setText(0, _translate("MainWindow", "b) Weak clutch springs"))
        self.treeWidget.topLevelItem(1).child(0).child(2).setText(0, _translate("MainWindow", "c) Worn clutch plates"))
        self.treeWidget.topLevelItem(1).child(0).child(3).setText(0, _translate("MainWindow", "d) Damaged pressure plates"))
        self.treeWidget.topLevelItem(1).child(0).child(4).setText(0, _translate("MainWindow", "e) Clutch release mechanism damage"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "Clutch dragging"))
        self.treeWidget.topLevelItem(1).child(1).child(0).setText(0, _translate("MainWindow", "a) Incorrect clutch adjustment"))
        self.treeWidget.topLevelItem(1).child(1).child(1).setText(0, _translate("MainWindow", "b) Clutch spring tension uneven"))
        self.treeWidget.topLevelItem(1).child(1).child(2).setText(0, _translate("MainWindow", "c) Warped clutch plates"))
        self.treeWidget.topLevelItem(1).child(1).child(3).setText(0, _translate("MainWindow", "d) Excessive clutch level play"))
        self.treeWidget.topLevelItem(1).child(1).child(4).setText(0, _translate("MainWindow", "e) Clutch housing damage"))
        self.treeWidget.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "Excessive Clutch Noise"))
        self.treeWidget.topLevelItem(1).child(2).child(0).setText(0, _translate("MainWindow", "a) Damaged clutch gear teeth"))
        self.treeWidget.topLevelItem(1).child(2).child(1).setText(0, _translate("MainWindow", "b) Worn or warped clutch plates"))


        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "Transmission Issues"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "Check clutch for issues first"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "Main Problems"))
        self.treeWidget.topLevelItem(2).child(1).child(0).setText(0, _translate("MainWindow", "a) Excessive gear noise"))
        self.treeWidget.topLevelItem(2).child(1).child(1).setText(0, _translate("MainWindow", "b) Diffcult shifting"))
        self.treeWidget.topLevelItem(2).child(1).child(2).setText(0, _translate("MainWindow", "c) Gears pop out of mesh"))
        self.treeWidget.topLevelItem(2).child(1).child(3).setText(0, _translate("MainWindow", "D) Incorrect shift level operation"))


        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "Emergency Issues"))
        self.treeWidget.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "Engine Won't Start"))
        self.treeWidget.topLevelItem(3).child(0).child(0).setText(0, _translate("MainWindow", "If engine has spark"))
        self.treeWidget.topLevelItem(3).child(0).child(0).child(0).setText(0, _translate("MainWindow", "a) Obstructed fuel line or fuel filter"))
        self.treeWidget.topLevelItem(3).child(0).child(0).child(1).setText(0, _translate("MainWindow", "b) Leaking head gasket"))
        self.treeWidget.topLevelItem(3).child(0).child(0).child(2).setText(0, _translate("MainWindow", "c) Low Compression"))
        self.treeWidget.topLevelItem(3).child(0).child(1).setText(0, _translate("MainWindow", "If engine does not have spark"))
        self.treeWidget.topLevelItem(3).child(0).child(1).child(0).setText(0, _translate("MainWindow", "a) Loose electrical connections"))
        self.treeWidget.topLevelItem(3).child(0).child(1).child(1).setText(0, _translate("MainWindow", "b) Dirty electrical connections"))
        self.treeWidget.topLevelItem(3).child(0).child(1).child(2).setText(0, _translate("MainWindow", "c) Loose or broken ignition coil ground wire"))
        self.treeWidget.topLevelItem(3).child(0).child(1).child(3).setText(0, _translate("MainWindow", "d) Broken or shorted high tension lead to the park plug"))
        self.treeWidget.topLevelItem(3).child(0).child(1).child(4).setText(0, _translate("MainWindow", "e) Discharged batery"))
        self.treeWidget.topLevelItem(3).child(0).child(1).child(5).setText(0, _translate("MainWindow", "f) Disconnected or damaged battery connection"))
        self.treeWidget.topLevelItem(3).child(0).child(1).child(6).setText(0, _translate("MainWindow", "g) Breaker points oxidized"))

        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.diagnoseLabel_2.setText(_translate("MainWindow", "Troubleshoot Symptoms to Diagnose Issues"))
        self.logLable.setText(_translate("MainWindow", "Log"))
        self.listOfLoggedRides.setToolTip(_translate("MainWindow", "<html><head/><body><p>Check out your past rides here.</p></body></html>"))
        self.listOfLoggedRides.setSortingEnabled(False)
        __sortingEnabled = self.listOfLoggedRides.isSortingEnabled()
        self.listOfLoggedRides.setSortingEnabled(False)
        self.listOfLoggedRides.setSortingEnabled(__sortingEnabled)
        self.descripOfRide.setToolTip(_translate("MainWindow", "Provide a short summary of your most recent ride!"))
        self.descripOfRide.setPlaceholderText(_translate("MainWindow", "enter a short description of your ride"))
        self.rideLogLable.setText(_translate("MainWindow", "Ride Log"))
        self.logrideButton.setText(_translate("MainWindow", "Log Ride"))
        self.deleteLogItemButton.setText(_translate("MainWindow", "Delete Logged Ride"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuManage.setTitle(_translate("MainWindow", "Manage"))
        self.menuTheme.setTitle(_translate("MainWindow", "Settings"))
        self.menuChoose_Theme.setTitle(_translate("MainWindow", "Choose Theme"))
        self.menuTips.setTitle(_translate("MainWindow", "Tips"))
        self.menuHelpful_Reminders.setTitle(_translate("MainWindow", "Helpful Reminders"))
        self.menuMaintenance_Schedule.setTitle(_translate("MainWindow", "Maintenance Schedule"))
        self.actionSwitch_User.setText(_translate("MainWindow", "Switch User"))
        self.actionIssue_List.setText(_translate("MainWindow", "Issue List"))
        self.actionLog_Maintenance.setText(_translate("MainWindow", "Log Maintenance"))
        self.actionView_Garage.setText(_translate("MainWindow", "View Garage"))
        self.actionBefore_Every_Ride_Checks.setText(_translate("MainWindow", "Before Every Ride Checks"))
        self.actionSymptom_Diagnoser.setText(_translate("MainWindow", "Symptom Diagnoser"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionLast_Logged.setText(_translate("MainWindow", "Last Logged"))
        self.actionUpcoming.setText(_translate("MainWindow", "Upcoming"))
        self.actionPast_Due.setText(_translate("MainWindow", "Past Due"))
        self.actionKawasaki.setText(_translate("MainWindow", "Kawasaki"))
        self.actionHonda.setText(_translate("MainWindow", "Honda"))
        self.actionYamaha.setText(_translate("MainWindow", "Yamaha"))
        self.actionHarley_Davidson.setText(_translate("MainWindow", "Harley-Davidson"))
        self.actionLog_Ride.setText(_translate("MainWindow", "Log Ride"))
