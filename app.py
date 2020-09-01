# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dylanpc/Documents/shiptracker.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        red = QtGui.QColor(255, 0, 0)
        purple = QtGui.QColor(70, 20, 140)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 410)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(820, 410))
        MainWindow.setMinimumSize(QtCore.QSize(820, 410))
        p = MainWindow.palette()
        p.setColor(MainWindow.backgroundRole(), purple)
        MainWindow.setPalette(p)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 811, 351))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setStyleSheet("background-color: white;")
        self.label_tab = QtWidgets.QWidget()
        self.label_tab.setObjectName("label_tab")
        self.label_table = QtWidgets.QTableWidget(self.label_tab)
        self.label_table.setGeometry(QtCore.QRect(200, 0, 585, 351))
        self.label_table.setObjectName("label_table")
        self.label_table.setColumnCount(10)
        self.label_table.setHorizontalHeaderLabels(("Name", "Address", "Address 2", "City", "State", "Zip", "Country",
                                                    "Invoice", "Weight", "Signature"))
        label_header = self.label_table.horizontalHeader()
        for i in range(10, 1):
            label_header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        self.label_table.setRowCount(0)
        self.file_label = QtWidgets.QLabel(self.label_tab)
        self.file_label.setGeometry(QtCore.QRect(10, 0, 181, 31))
        self.file_label.setAlignment(QtCore.Qt.AlignCenter)
        self.file_label.setObjectName("file_label")
        self.browse_button = QtWidgets.QPushButton(self.label_tab)
        self.browse_button.setGeometry(QtCore.QRect(8, 30, 181, 25))
        self.browse_button.setObjectName("browse_button")
        self.log_box = QtWidgets.QTextBrowser(self.label_tab)
        self.log_box.setGeometry(QtCore.QRect(10, 100, 181, 171))
        self.log_box.setObjectName("log_box")
        self.log_box.setTextColor(red)
        self.log_box.setText("< Execution Logs >")
        self.label = QtWidgets.QLabel(self.label_tab)
        self.label.setGeometry(QtCore.QRect(6, 80, 181, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.export_button = QtWidgets.QPushButton(self.label_tab)
        self.export_button.setGeometry(QtCore.QRect(10, 310, 181, 25))
        self.export_button.setObjectName("export_button")
        self.tabWidget.addTab(self.label_tab, "")
        self.track_tab = QtWidgets.QWidget()
        self.track_tab.setObjectName("track_tab")
        self.tracking_table = QtWidgets.QTableWidget(self.track_tab)
        self.tracking_table.setGeometry(QtCore.QRect(200, 0, 585, 351))
        self.tracking_table.setObjectName("tracking_table")
        self.tracking_table.setColumnCount(2)
        self.tracking_table.setRowCount(0)
        self.tracking_table.setHorizontalHeaderLabels(("Tracking Number", "Tracking Status"))
        tracking_header = self.tracking_table.horizontalHeader()
        tracking_header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        tracking_header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tracking_input_box = QtWidgets.QTextEdit(self.track_tab)
        self.tracking_input_box.setGeometry(QtCore.QRect(10, 20, 181, 191))
        self.tracking_input_box.setObjectName("tracking_input_box")
        self.tracking_label = QtWidgets.QLabel(self.track_tab)
        self.tracking_label.setGeometry(QtCore.QRect(10, 0, 181, 20))
        self.tracking_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tracking_label.setObjectName("tracking_label")
        self.tracking_button = QtWidgets.QPushButton(self.track_tab)
        self.tracking_button.setGeometry(QtCore.QRect(10, 230, 181, 25))
        self.tracking_button.setObjectName("tracking_button")
        self.tracking_progressBar = QtWidgets.QProgressBar(self.track_tab)
        self.tracking_progressBar.setGeometry(QtCore.QRect(10, 270, 181, 23))
        self.tracking_progressBar.setProperty("value", 0)
        self.tracking_progressBar.setObjectName("tracking_progressBar")
        self.total_label = QtWidgets.QLabel(self.track_tab)
        self.total_label.setGeometry(QtCore.QRect(10, 310, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.total_label.setFont(font)
        self.total_label.setObjectName("total_label")
        self.tabWidget.addTab(self.track_tab, "")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(180, 0, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.title_label.setStyleSheet("color: white;")
        MainWindow.setCentralWidget(self.centralwidget)

        # File Browse Signal Call
        self.browse_button.clicked.connect(self.browse_file_signal)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # File Browser Signal Function
    def browse_file_signal(self):

        print("File browse button pressed")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fedex Manager"))
        self.file_label.setText(_translate("MainWindow", "File Name"))
        self.browse_button.setText(_translate("MainWindow", "Browse..."))
        self.label.setText(_translate("MainWindow", "Log Output"))
        self.export_button.setText(_translate("MainWindow", "Export"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.label_tab), _translate("MainWindow", "Batch Labels"))
        self.tracking_label.setText(_translate("MainWindow", "Tracking Numbers"))
        self.tracking_button.setText(_translate("MainWindow", "Track Shipments"))
        self.total_label.setText(_translate("MainWindow", "Total Tracked: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.track_tab), _translate("MainWindow", "Batch Tracking"))
        self.title_label.setText(_translate("MainWindow", "Fedex Manager"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    App = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(App)
    App.show()
    sys.exit(app.exec_())