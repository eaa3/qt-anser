# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'systemwidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_systemwidget(object):
    def setupUi(self, systemwidget):
        systemwidget.setObjectName("systemwidget")
        systemwidget.resize(500, 790)
        systemwidget.setMinimumSize(QtCore.QSize(500, 0))
        systemwidget.setMaximumSize(QtCore.QSize(900, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(systemwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.label_14 = QtWidgets.QLabel(systemwidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14, 0, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(systemwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.groupBox = QtWidgets.QGroupBox(systemwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.coil_1 = QtWidgets.QLabel(self.groupBox)
        self.coil_1.setText("")
        self.coil_1.setObjectName("coil_1")
        self.gridLayout.addWidget(self.coil_1, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.coil_3 = QtWidgets.QLabel(self.groupBox)
        self.coil_3.setText("")
        self.coil_3.setObjectName("coil_3")
        self.gridLayout.addWidget(self.coil_3, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.coil_8f = QtWidgets.QLabel(self.groupBox)
        self.coil_8f.setObjectName("coil_8f")
        self.gridLayout.addWidget(self.coil_8f, 2, 8, 1, 1, QtCore.Qt.AlignHCenter)
        self.coil_3f = QtWidgets.QLabel(self.groupBox)
        self.coil_3f.setObjectName("coil_3f")
        self.gridLayout.addWidget(self.coil_3f, 2, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.coil_7f = QtWidgets.QLabel(self.groupBox)
        self.coil_7f.setObjectName("coil_7f")
        self.gridLayout.addWidget(self.coil_7f, 2, 7, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 8, 1, 1, QtCore.Qt.AlignHCenter)
        self.coil_2f = QtWidgets.QLabel(self.groupBox)
        self.coil_2f.setObjectName("coil_2f")
        self.gridLayout.addWidget(self.coil_2f, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.coil_5f = QtWidgets.QLabel(self.groupBox)
        self.coil_5f.setObjectName("coil_5f")
        self.gridLayout.addWidget(self.coil_5f, 2, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.coil_7 = QtWidgets.QLabel(self.groupBox)
        self.coil_7.setText("")
        self.coil_7.setObjectName("coil_7")
        self.gridLayout.addWidget(self.coil_7, 1, 7, 1, 1, QtCore.Qt.AlignHCenter)
        self.coil_5 = QtWidgets.QLabel(self.groupBox)
        self.coil_5.setText("")
        self.coil_5.setObjectName("coil_5")
        self.gridLayout.addWidget(self.coil_5, 1, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.coil_6 = QtWidgets.QLabel(self.groupBox)
        self.coil_6.setText("")
        self.coil_6.setObjectName("coil_6")
        self.gridLayout.addWidget(self.coil_6, 1, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.coil_4f = QtWidgets.QLabel(self.groupBox)
        self.coil_4f.setObjectName("coil_4f")
        self.gridLayout.addWidget(self.coil_4f, 2, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.coil_6f = QtWidgets.QLabel(self.groupBox)
        self.coil_6f.setObjectName("coil_6f")
        self.gridLayout.addWidget(self.coil_6f, 2, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.coil_8 = QtWidgets.QLabel(self.groupBox)
        self.coil_8.setText("")
        self.coil_8.setObjectName("coil_8")
        self.gridLayout.addWidget(self.coil_8, 1, 8, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.coil_4 = QtWidgets.QLabel(self.groupBox)
        self.coil_4.setText("")
        self.coil_4.setObjectName("coil_4")
        self.gridLayout.addWidget(self.coil_4, 1, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.coil_1f = QtWidgets.QLabel(self.groupBox)
        self.coil_1f.setObjectName("coil_1f")
        self.gridLayout.addWidget(self.coil_1f, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.coil_2 = QtWidgets.QLabel(self.groupBox)
        self.coil_2.setText("")
        self.coil_2.setObjectName("coil_2")
        self.gridLayout.addWidget(self.coil_2, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 7, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(systemwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setObjectName("label_28")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.label_30 = QtWidgets.QLabel(self.groupBox_2)
        self.label_30.setObjectName("label_30")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_30)
        self.refresh_rate = QtWidgets.QLabel(self.groupBox_2)
        self.refresh_rate.setObjectName("refresh_rate")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.refresh_rate)
        self.label_32 = QtWidgets.QLabel(self.groupBox_2)
        self.label_32.setObjectName("label_32")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_32)
        self.active_ports = QtWidgets.QLabel(self.groupBox_2)
        self.active_ports.setObjectName("active_ports")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.active_ports)
        self.sampling_frequency = QtWidgets.QLabel(self.groupBox_2)
        self.sampling_frequency.setObjectName("sampling_frequency")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sampling_frequency)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.label_15 = QtWidgets.QLabel(systemwidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15, 0, QtCore.Qt.AlignHCenter)
        self.line_2 = QtWidgets.QFrame(systemwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.groupBox_3 = QtWidgets.QGroupBox(systemwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_34 = QtWidgets.QLabel(self.groupBox_3)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout.addWidget(self.label_34)
        self.label_36 = QtWidgets.QLabel(self.groupBox_3)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout.addWidget(self.label_36)
        self.slider = QtWidgets.QSlider(self.groupBox_3)
        self.slider.setMinimum(1)
        self.slider.setMaximum(4)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.slider.setTickInterval(1)
        self.slider.setObjectName("slider")
        self.horizontalLayout.addWidget(self.slider)
        self.label_35 = QtWidgets.QLabel(self.groupBox_3)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout.addWidget(self.label_35)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_43 = QtWidgets.QLabel(self.groupBox_3)
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.gridLayout_2.addWidget(self.label_43, 0, 0, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.groupBox_3)
        self.label_41.setObjectName("label_41")
        self.gridLayout_2.addWidget(self.label_41, 1, 0, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.groupBox_3)
        self.label_42.setObjectName("label_42")
        self.gridLayout_2.addWidget(self.label_42, 2, 0, 1, 1)
        self.checkbox_1 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkbox_1.setText("")
        self.checkbox_1.setObjectName("checkbox_1")
        self.gridLayout_2.addWidget(self.checkbox_1, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.combo_1 = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_1.sizePolicy().hasHeightForWidth())
        self.combo_1.setSizePolicy(sizePolicy)
        self.combo_1.setObjectName("combo_1")
        self.combo_1.addItem("")
        self.gridLayout_2.addWidget(self.combo_1, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_37 = QtWidgets.QLabel(self.groupBox_3)
        self.label_37.setObjectName("label_37")
        self.gridLayout_2.addWidget(self.label_37, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.combo_2 = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_2.sizePolicy().hasHeightForWidth())
        self.combo_2.setSizePolicy(sizePolicy)
        self.combo_2.setObjectName("combo_2")
        self.gridLayout_2.addWidget(self.combo_2, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.combo_3 = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_3.sizePolicy().hasHeightForWidth())
        self.combo_3.setSizePolicy(sizePolicy)
        self.combo_3.setObjectName("combo_3")
        self.gridLayout_2.addWidget(self.combo_3, 2, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.combo_4 = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_4.sizePolicy().hasHeightForWidth())
        self.combo_4.setSizePolicy(sizePolicy)
        self.combo_4.setObjectName("combo_4")
        self.gridLayout_2.addWidget(self.combo_4, 2, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.checkbox_2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkbox_2.setText("")
        self.checkbox_2.setObjectName("checkbox_2")
        self.gridLayout_2.addWidget(self.checkbox_2, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.checkbox_3 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkbox_3.setText("")
        self.checkbox_3.setObjectName("checkbox_3")
        self.gridLayout_2.addWidget(self.checkbox_3, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.checkbox_4 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkbox_4.setText("")
        self.checkbox_4.setObjectName("checkbox_4")
        self.gridLayout_2.addWidget(self.checkbox_4, 1, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.apply_button = QtWidgets.QPushButton(self.groupBox_3)
        self.apply_button.setFlat(False)
        self.apply_button.setObjectName("apply_button")
        self.verticalLayout_3.addWidget(self.apply_button, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.groupBox_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(systemwidget)
        QtCore.QMetaObject.connectSlotsByName(systemwidget)

    def retranslateUi(self, systemwidget):
        _translate = QtCore.QCoreApplication.translate
        systemwidget.setWindowTitle(_translate("systemwidget", "Form"))
        self.label_14.setText(_translate("systemwidget", "System Status"))
        self.groupBox.setTitle(_translate("systemwidget", "Transmitter Parameters"))
        self.coil_8f.setText(_translate("systemwidget", "0"))
        self.coil_3f.setText(_translate("systemwidget", "0"))
        self.coil_7f.setText(_translate("systemwidget", "0"))
        self.label_19.setText(_translate("systemwidget", "Coils Frequency (kHz):"))
        self.label_9.setText(_translate("systemwidget", "8"))
        self.coil_2f.setText(_translate("systemwidget", "0"))
        self.label_4.setText(_translate("systemwidget", "3"))
        self.coil_5f.setText(_translate("systemwidget", "0"))
        self.label_3.setText(_translate("systemwidget", "2"))
        self.label_2.setText(_translate("systemwidget", "1"))
        self.coil_4f.setText(_translate("systemwidget", "0"))
        self.coil_6f.setText(_translate("systemwidget", "0"))
        self.label.setText(_translate("systemwidget", "Coils:"))
        self.label_7.setText(_translate("systemwidget", "6"))
        self.label_10.setText(_translate("systemwidget", "Coils Active:"))
        self.coil_1f.setText(_translate("systemwidget", "0"))
        self.label_6.setText(_translate("systemwidget", "5"))
        self.label_5.setText(_translate("systemwidget", "4"))
        self.label_8.setText(_translate("systemwidget", "7"))
        self.groupBox_2.setTitle(_translate("systemwidget", "Sensor Parameters"))
        self.label_28.setText(_translate("systemwidget", "Sampling Frequency (kHz):"))
        self.label_30.setText(_translate("systemwidget", "Sample Size:"))
        self.refresh_rate.setText(_translate("systemwidget", "0"))
        self.label_32.setText(_translate("systemwidget", "Active Ports:"))
        self.active_ports.setText(_translate("systemwidget", "0"))
        self.sampling_frequency.setText(_translate("systemwidget", "0"))
        self.label_15.setText(_translate("systemwidget", "Tracking"))
        self.label_34.setText(_translate("systemwidget", "System Speed:"))
        self.label_36.setText(_translate("systemwidget", "Slow:"))
        self.label_35.setText(_translate("systemwidget", "Fast"))
        self.label_41.setText(_translate("systemwidget", "Port:"))
        self.label_42.setText(_translate("systemwidget", "Sensor:"))
        self.combo_1.setItemText(0, _translate("systemwidget", "yrdy"))
        self.label_37.setText(_translate("systemwidget", "1"))
        self.label_11.setText(_translate("systemwidget", "2"))
        self.label_12.setText(_translate("systemwidget", "3"))
        self.label_13.setText(_translate("systemwidget", "4"))
        self.apply_button.setText(_translate("systemwidget", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    systemwidget = QtWidgets.QWidget()
    ui = Ui_systemwidget()
    ui.setupUi(systemwidget)
    systemwidget.show()
    sys.exit(app.exec_())

