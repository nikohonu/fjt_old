# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 254)
        icon = QIcon()
        icon.addFile(u":/icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.push_button_copy = QPushButton(self.centralwidget)
        self.push_button_copy.setObjectName(u"push_button_copy")

        self.gridLayout.addWidget(self.push_button_copy, 11, 0, 1, 2)

        self.combo_box_media_type = QComboBox(self.centralwidget)
        self.combo_box_media_type.setObjectName(u"combo_box_media_type")

        self.gridLayout.addWidget(self.combo_box_media_type, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 12, 0, 1, 2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)

        self.line_edit_additional = QLineEdit(self.centralwidget)
        self.line_edit_additional.setObjectName(u"line_edit_additional")

        self.gridLayout.addWidget(self.line_edit_additional, 6, 1, 1, 1)

        self.label_media_type = QLabel(self.centralwidget)
        self.label_media_type.setObjectName(u"label_media_type")

        self.gridLayout.addWidget(self.label_media_type, 3, 0, 1, 1)

        self.double_spin_box_amount = QDoubleSpinBox(self.centralwidget)
        self.double_spin_box_amount.setObjectName(u"double_spin_box_amount")
        self.double_spin_box_amount.setMinimum(1.000000000000000)
        self.double_spin_box_amount.setMaximum(100000.000000000000000)
        self.double_spin_box_amount.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.double_spin_box_amount, 5, 1, 1, 1)

        self.line_edit_log = QLineEdit(self.centralwidget)
        self.line_edit_log.setObjectName(u"line_edit_log")
        self.line_edit_log.setReadOnly(True)

        self.gridLayout.addWidget(self.line_edit_log, 8, 0, 1, 2)

        self.label_result = QLabel(self.centralwidget)
        self.label_result.setObjectName(u"label_result")

        self.gridLayout.addWidget(self.label_result, 9, 0, 1, 2)

        self.combo_box_name = QComboBox(self.centralwidget)
        self.combo_box_name.setObjectName(u"combo_box_name")
        self.combo_box_name.setEditable(True)

        self.gridLayout.addWidget(self.combo_box_name, 2, 1, 1, 1)

        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")

        self.gridLayout.addWidget(self.label_name, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FJT", None))
        self.push_button_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Additional Info", None))
        self.label_media_type.setText(QCoreApplication.translate("MainWindow", u"Media type", None))
        self.label_result.setText(QCoreApplication.translate("MainWindow", u"1 point per page \u2192 +4 points", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
    # retranslateUi

