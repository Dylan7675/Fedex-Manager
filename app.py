# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dylanpc/Documents/shiptracker.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow, QMenuBar
from pathlib import Path
from label_format import Formatter
import pandas as pd
import requests
from create_shipment import Configuration, Shipment


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        red = QtGui.QColor(255, 0, 0)
        purple = QtGui.QColor(70, 20, 140)
        self.setObjectName("MainWindow")
        self.resize(820, 410)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(820, 410))
        self.setMinimumSize(QtCore.QSize(820, 410))
        p = self.palette()
        p.setColor(self.backgroundRole(), purple)
        self.setPalette(p)
        self.centralwidget = QtWidgets.QWidget(self)
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
        self.label_table.setColumnCount(11)
        self.label_table.setHorizontalHeaderLabels(("Name", "Address", "Address 2", "City", "State", "Zip", "Phone",
                                                    "Country", "Weight", "Invoice", "Signature"))

        self.label_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
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
        self.print_button = QtWidgets.QPushButton(self.label_tab)
        self.print_button.setGeometry(QtCore.QRect(10, 280, 181, 25))
        self.print_button.setObjectName("print_button")
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
        self.setCentralWidget(self.centralwidget)

        # Menu Bar
        self.menu_bar = self.menuBar()
        self.config_menu = self.menu_bar.addMenu("Config")
        self.new_config_option = QtWidgets.QAction("New Config", self)
        self.new_config_option.setShortcut("Ctrl+N")
        self.new_config_option.triggered.connect(lambda: print("test")) # add new config signal
        self.load_config_option = self.config_menu.addMenu("Load Config")
        self.config_menu.addAction(self.new_config_option)
        self.config_menu.addMenu(self.load_config_option)
        # self.menu_bar.setNativeMenuBar(False)

        self.activated_widget = None

        # Initializing tracking lists
        self.tracking_list = []
        self.tracking_status_list = []

        # Initializing clipboard
        self.clip = QtWidgets.QApplication.clipboard()

        # File Browse Signal Call
        self.browse_button.clicked.connect(self.browse_file_signal)

        # Table Changed Signal Call
        self.label_table.itemChanged.connect(self.edit_label_table_dataset)
        self.label_table.itemEntered.connect(self.active_widget)

        # Export File Signal Call
        self.export_button.clicked.connect(self.active_widget)
        self.export_button.clicked.connect(self.export_label_table)
        self.export_button.blockSignals(True)

        # Print Label Signal Call
        self.print_button.clicked.connect(self.active_widget)
        self.print_button.clicked.connect(self.print_labels)
        self.print_button.blockSignals(True)

        # Export Track Shipments Call
        self.tracking_button.clicked.connect(self.track_shipments_signal)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def browse_file_signal(self):
        """ File Browser Signal Function """

        self.file_path = Path(QtWidgets.QFileDialog.getOpenFileName(self, 'Select files',
                                                            '/', "CSV file (*.csv)")[0])

        if self.file_path.name:

            self.data_import = Formatter(self.file_path)
            try:
                self.log_box.setText("Double Check for Accuracy")
                self.import_df = self.data_import.parse_csv()
                self.update_label_table()
                self.label_table.resizeColumnsToContents()
                self.file_label.setText(self.file_path.name)
                self.export_button.blockSignals(False)
                self.print_button.blockSignals(False)

                if self.data_import.logs:
                    self.log_box.setText("".join(self.data_import.logs))

            except Exception as e:
                self.log_box.setText(f"Incompatible data!\n\nPlease verify the import data.")


    def track_shipments_signal(self):
        print("track signal call")
        #self.tracking_list = self.tracking_input_box.getText().split(",")

        #if self.tracking_list:
            #for index, tracking_number in enumerate(self.tracking_list, 1)
                #self.tracking_status_list.append(Tracker.track(tracking_number))
                #self.update_progressbar(index)

            #update tracking table: Col 0 - Tracking Number ; Col 1 - Tracking Status


    def update_label_table(self):
        """ Updates the label table with data from df """

        self.label_table.blockSignals(True)
        self.df_array = self.import_df.values
        self.label_table.setRowCount(self.import_df.shape[0])
        for row in range(self.import_df.shape[0]):
            for col in range(self.import_df.shape[1]):
                self.label_table.setItem(row, col, QtWidgets.QTableWidgetItem(str(self.df_array[row, col])))
        self.label_table.blockSignals(False)

    def edit_label_table_dataset(self, item):
        """ Listens for table edits and updates df_array dataset """

        self.df_array[item.row(), item.column()] = item.text()
        self.label_table.resizeColumnsToContents()

    def print_labels(self):

        self.print_button.blockSignals(True)
        self.log_box.setText("Printing Labels...")

        recipient_dic = pd.DataFrame(data=self.df_array,
                                 columns=[col for col in
                                 self.import_df.columns]).T.to_dict()

        for key in recipient_dic.keys():
            try:
                recipient = recipient_dic[key]
                shipment = Shipment(recipient)
                shipment.create_shipment()
                shipment.label_2pdf()
                shipment.print_label()
            except Exception as e:
                self.log_box.setText(self.log_box.toPlainText() +
                            f"\n\nUnable to print for {recipient['FullName']}")

    def export_label_table(self):
        """ Reads out edited data from the table and exports to file """

        export_df = pd.DataFrame(data=self.df_array,
                                 columns=[col for col in self.import_df.columns])

        name_path = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File',
                                        "label_export", "CSV file (*.csv)")[0]

        if name_path:
            export_df.to_csv(name_path, index=False)

    def update_progressbar(self, index):
        tracking_percent = (index/len(self.tracking_list))*100
        self.tracking_progressBar.setValue(tracking_percent)
        self.total_label.setText(f"Total Tracked: {index}")

    def keyPressEvent(self, e):
        """ Copy Event """

        if e.modifiers() & QtCore.Qt.ControlModifier:
            if e.key() == QtCore.Qt.Key_C:
                if isinstance(self.activated_widget, QtWidgets.QTableWidget):
                    selected = self.activated_widget.selectedRanges()
                    s = ""
                    for r in range(selected[0].topRow(), selected[0].bottomRow() + 1):
                        for c in range(selected[0].leftColumn(), selected[0].rightColumn() + 1):
                            try:
                                s += str(self.activated_widget.item(r, c).text()) + "\t"
                            except AttributeError:
                                s += "\t"
                        s = s[:-1] + "\n"  # eliminate last '\t'
                    self.clip.setText(s)
        if e.key() == QtCore.Qt.Key_F5:
            self.close()

    def active_widget(self):
        self.activated_widget = self.sender()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Fedex Manager"))
        self.file_label.setText(_translate("MainWindow", "File Name"))
        self.browse_button.setText(_translate("MainWindow", "Browse..."))
        self.label.setText(_translate("MainWindow", "Log Output"))
        self.export_button.setText(_translate("MainWindow", "Export CSV"))
        self.print_button.setText(_translate("MainWindow","Print Labels"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.label_tab), _translate("MainWindow", "Batch Labels"))
        self.tracking_label.setText(_translate("MainWindow", "Tracking Numbers"))
        self.tracking_button.setText(_translate("MainWindow", "Track Shipments"))
        self.total_label.setText(_translate("MainWindow", "Total Tracked: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.track_tab), _translate("MainWindow", "Batch Tracking"))
        self.title_label.setText(_translate("MainWindow", "Fedex Manager"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
