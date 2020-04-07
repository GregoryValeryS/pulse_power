# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\GitHub\pulse_power\pyside_program\pulse_power.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_main(object):
    def setupUi(self, Dialog_main):
        Dialog_main.setObjectName("Dialog_main")
        Dialog_main.resize(541, 510)
        self.GroupBox_signal = QtWidgets.QGroupBox(Dialog_main)
        self.GroupBox_signal.setGeometry(QtCore.QRect(10, 10, 241, 171))
        self.GroupBox_signal.setFlat(False)
        self.GroupBox_signal.setCheckable(False)
        self.GroupBox_signal.setObjectName("GroupBox_signal")
        self.label_signal_duration = QtWidgets.QLabel(self.GroupBox_signal)
        self.label_signal_duration.setGeometry(QtCore.QRect(10, 70, 161, 20))
        self.label_signal_duration.setObjectName("label_signal_duration")
        self.label_repetition_rate = QtWidgets.QLabel(self.GroupBox_signal)
        self.label_repetition_rate.setGeometry(QtCore.QRect(10, 120, 211, 20))
        self.label_repetition_rate.setTextFormat(QtCore.Qt.AutoText)
        self.label_repetition_rate.setObjectName("label_repetition_rate")
        self.label_mode = QtWidgets.QLabel(self.GroupBox_signal)
        self.label_mode.setGeometry(QtCore.QRect(10, 20, 181, 16))
        self.label_mode.setObjectName("label_mode")
        self.combo_mode = QtWidgets.QComboBox(self.GroupBox_signal)
        self.combo_mode.setGeometry(QtCore.QRect(10, 40, 191, 22))
        self.combo_mode.setObjectName("combo_mode")
        self.LCD_signal_duration_floor = QtWidgets.QLCDNumber(self.GroupBox_signal)
        self.LCD_signal_duration_floor.setGeometry(QtCore.QRect(10, 90, 51, 21))
        self.LCD_signal_duration_floor.setMidLineWidth(0)
        self.LCD_signal_duration_floor.setSmallDecimalPoint(False)
        self.LCD_signal_duration_floor.setObjectName("LCD_signal_duration_floor")
        self.LCD_repetition_rate = QtWidgets.QLCDNumber(self.GroupBox_signal)
        self.LCD_repetition_rate.setGeometry(QtCore.QRect(10, 140, 51, 21))
        self.LCD_repetition_rate.setMidLineWidth(0)
        self.LCD_repetition_rate.setSmallDecimalPoint(False)
        self.LCD_repetition_rate.setObjectName("LCD_repetition_rate")
        self.LCD_signal_duration_ceil = QtWidgets.QLCDNumber(self.GroupBox_signal)
        self.LCD_signal_duration_ceil.setGeometry(QtCore.QRect(90, 90, 51, 21))
        self.LCD_signal_duration_ceil.setMidLineWidth(0)
        self.LCD_signal_duration_ceil.setSmallDecimalPoint(False)
        self.LCD_signal_duration_ceil.setObjectName("LCD_signal_duration_ceil")
        self.label_dash = QtWidgets.QLabel(self.GroupBox_signal)
        self.label_dash.setGeometry(QtCore.QRect(70, 90, 16, 16))
        self.label_dash.setObjectName("label_dash")
        self.GroupBox_vattmeter = QtWidgets.QGroupBox(Dialog_main)
        self.GroupBox_vattmeter.setGeometry(QtCore.QRect(270, 240, 171, 61))
        self.GroupBox_vattmeter.setObjectName("GroupBox_vattmeter")
        self.line_vattmeter = QtWidgets.QLineEdit(self.GroupBox_vattmeter)
        self.line_vattmeter.setGeometry(QtCore.QRect(20, 20, 141, 21))
        self.line_vattmeter.setObjectName("line_vattmeter")
        self.GroupBox_tract = QtWidgets.QGroupBox(Dialog_main)
        self.GroupBox_tract.setGeometry(QtCore.QRect(10, 190, 241, 181))
        self.GroupBox_tract.setObjectName("GroupBox_tract")
        self.line_Dp = QtWidgets.QLineEdit(self.GroupBox_tract)
        self.line_Dp.setGeometry(QtCore.QRect(10, 120, 221, 20))
        self.line_Dp.setObjectName("line_Dp")
        self.label_k_attenuation = QtWidgets.QLabel(self.GroupBox_tract)
        self.label_k_attenuation.setGeometry(QtCore.QRect(10, 150, 191, 20))
        self.label_k_attenuation.setObjectName("label_k_attenuation")
        self.LCD_kosl = QtWidgets.QLCDNumber(self.GroupBox_tract)
        self.LCD_kosl.setGeometry(QtCore.QRect(180, 150, 51, 21))
        self.LCD_kosl.setMidLineWidth(0)
        self.LCD_kosl.setSmallDecimalPoint(False)
        self.LCD_kosl.setObjectName("LCD_kosl")
        self.label_Dp_KP_2 = QtWidgets.QLabel(self.GroupBox_tract)
        self.label_Dp_KP_2.setGeometry(QtCore.QRect(10, 20, 221, 20))
        self.label_Dp_KP_2.setObjectName("label_Dp_KP_2")
        self.label_Dp_KP_3 = QtWidgets.QLabel(self.GroupBox_tract)
        self.label_Dp_KP_3.setGeometry(QtCore.QRect(10, 40, 211, 20))
        self.label_Dp_KP_3.setObjectName("label_Dp_KP_3")
        self.label_Dp_1 = QtWidgets.QLabel(self.GroupBox_tract)
        self.label_Dp_1.setGeometry(QtCore.QRect(10, 80, 211, 20))
        self.label_Dp_1.setObjectName("label_Dp_1")
        self.label_Dp = QtWidgets.QLabel(self.GroupBox_tract)
        self.label_Dp.setGeometry(QtCore.QRect(10, 100, 211, 20))
        self.label_Dp.setObjectName("label_Dp")
        self.label_Dp_2 = QtWidgets.QLabel(self.GroupBox_tract)
        self.label_Dp_2.setGeometry(QtCore.QRect(10, 60, 211, 20))
        self.label_Dp_2.setObjectName("label_Dp_2")
        self.GroupBox_result = QtWidgets.QGroupBox(Dialog_main)
        self.GroupBox_result.setGeometry(QtCore.QRect(20, 380, 221, 111))
        self.GroupBox_result.setObjectName("GroupBox_result")
        self.pulse_power = QtWidgets.QLCDNumber(self.GroupBox_result)
        self.pulse_power.setGeometry(QtCore.QRect(10, 20, 71, 41))
        self.pulse_power.setMidLineWidth(0)
        self.pulse_power.setSmallDecimalPoint(False)
        self.pulse_power.setObjectName("pulse_power")
        self.label_pl_min = QtWidgets.QLabel(self.GroupBox_result)
        self.label_pl_min.setGeometry(QtCore.QRect(90, 40, 16, 16))
        self.label_pl_min.setObjectName("label_pl_min")
        self.range_pulse_power = QtWidgets.QLCDNumber(self.GroupBox_result)
        self.range_pulse_power.setGeometry(QtCore.QRect(110, 30, 61, 31))
        self.range_pulse_power.setMidLineWidth(0)
        self.range_pulse_power.setSmallDecimalPoint(False)
        self.range_pulse_power.setObjectName("range_pulse_power")
        self.button_Сalculation = QtWidgets.QPushButton(self.GroupBox_result)
        self.button_Сalculation.setGeometry(QtCore.QRect(10, 70, 51, 31))
        self.button_Сalculation.setObjectName("button_Сalculation")
        self.button_Clear = QtWidgets.QPushButton(self.GroupBox_result)
        self.button_Clear.setGeometry(QtCore.QRect(70, 70, 61, 31))
        self.button_Clear.setObjectName("button_Clear")
        self.button_Manual = QtWidgets.QPushButton(self.GroupBox_result)
        self.button_Manual.setGeometry(QtCore.QRect(140, 70, 71, 31))
        self.button_Manual.setObjectName("button_Manual")
        self.GroupBox_status = QtWidgets.QGroupBox(Dialog_main)
        self.GroupBox_status.setGeometry(QtCore.QRect(270, 310, 261, 181))
        self.GroupBox_status.setObjectName("GroupBox_status")
        self.txt_status = QtWidgets.QTextBrowser(self.GroupBox_status)
        self.txt_status.setGeometry(QtCore.QRect(10, 20, 241, 151))
        self.txt_status.setObjectName("txt_status")
        self.GroupBox_element = QtWidgets.QGroupBox(Dialog_main)
        self.GroupBox_element.setGeometry(QtCore.QRect(270, 10, 261, 221))
        self.GroupBox_element.setObjectName("GroupBox_element")
        self.label_element = QtWidgets.QLabel(self.GroupBox_element)
        self.label_element.setGeometry(QtCore.QRect(10, 20, 161, 16))
        self.label_element.setObjectName("label_element")
        self.combo_element = QtWidgets.QComboBox(self.GroupBox_element)
        self.combo_element.setGeometry(QtCore.QRect(10, 40, 171, 22))
        self.combo_element.setObjectName("combo_element")
        self.label_ke = QtWidgets.QLabel(self.GroupBox_element)
        self.label_ke.setGeometry(QtCore.QRect(10, 70, 181, 20))
        self.label_ke.setObjectName("label_ke")
        self.LCD_ke = QtWidgets.QLCDNumber(self.GroupBox_element)
        self.LCD_ke.setGeometry(QtCore.QRect(10, 90, 51, 21))
        self.LCD_ke.setMidLineWidth(0)
        self.LCD_ke.setSmallDecimalPoint(False)
        self.LCD_ke.setObjectName("LCD_ke")
        self.label_Gpr = QtWidgets.QLabel(self.GroupBox_element)
        self.label_Gpr.setGeometry(QtCore.QRect(10, 120, 221, 20))
        self.label_Gpr.setTextFormat(QtCore.Qt.AutoText)
        self.label_Gpr.setObjectName("label_Gpr")
        self.LCD_Gpr = QtWidgets.QLCDNumber(self.GroupBox_element)
        self.LCD_Gpr.setGeometry(QtCore.QRect(10, 140, 51, 21))
        self.LCD_Gpr.setMidLineWidth(0)
        self.LCD_Gpr.setSmallDecimalPoint(False)
        self.LCD_Gpr.setObjectName("LCD_Gpr")
        self.label_a = QtWidgets.QLabel(self.GroupBox_element)
        self.label_a.setGeometry(QtCore.QRect(10, 170, 251, 20))
        self.label_a.setTextFormat(QtCore.Qt.AutoText)
        self.label_a.setObjectName("label_a")
        self.LCD_a = QtWidgets.QLCDNumber(self.GroupBox_element)
        self.LCD_a.setGeometry(QtCore.QRect(10, 190, 51, 21))
        self.LCD_a.setMidLineWidth(0)
        self.LCD_a.setSmallDecimalPoint(False)
        self.LCD_a.setObjectName("LCD_a")

        self.retranslateUi(Dialog_main)
        QtCore.QMetaObject.connectSlotsByName(Dialog_main)

    def retranslateUi(self, Dialog_main):
        _translate = QtCore.QCoreApplication.translate
        Dialog_main.setWindowTitle(_translate("Dialog_main", "Dialog"))
        self.GroupBox_signal.setTitle(_translate("Dialog_main", "1. Сигнал на выходе станции"))
        self.label_signal_duration.setText(_translate("Dialog_main", "Длительность сигнала - t, мкс"))
        self.label_repetition_rate.setText(_translate("Dialog_main", "Частота повторения импульсов - Fи, Гц"))
        self.label_mode.setText(_translate("Dialog_main", "Выберете режим работы станции:"))
        self.label_dash.setText(_translate("Dialog_main", "—"))
        self.GroupBox_vattmeter.setTitle(_translate("Dialog_main", "4. Показания ваттметра Px, Вт"))
        self.GroupBox_tract.setTitle(_translate("Dialog_main", "3. Тракт"))
        self.label_k_attenuation.setText(_translate("Dialog_main", "Коэфф. осл. тракта - kосл, раз"))
        self.label_Dp_KP_2.setText(_translate("Dialog_main", "КП-2: 22.7 фланец \'контроль\' + 0.5 = 23.2;"))
        self.label_Dp_KP_3.setText(_translate("Dialog_main", "КП-3: 22. Значение ослабления тракта"))
        self.label_Dp_1.setText(_translate("Dialog_main", "у вас может отличаться, считате сами."))
        self.label_Dp.setText(_translate("Dialog_main", "Суммарное ослабление тракта - Dp, Дб"))
        self.label_Dp_2.setText(_translate("Dialog_main", "равное сумма ослабл. элементов тракта"))
        self.GroupBox_result.setTitle(_translate("Dialog_main", "Импульсная мощность Pимп, кВт"))
        self.label_pl_min.setText(_translate("Dialog_main", "±"))
        self.button_Сalculation.setText(_translate("Dialog_main", "Расчёт"))
        self.button_Clear.setText(_translate("Dialog_main", "Очистить"))
        self.button_Manual.setText(_translate("Dialog_main", "Методичка"))
        self.GroupBox_status.setTitle(_translate("Dialog_main", "Окно диалога"))
        self.GroupBox_element.setTitle(_translate("Dialog_main", "2. Элемент перехода"))
        self.label_element.setText(_translate("Dialog_main", "Выберете элемент перехода:"))
        self.label_ke.setText(_translate("Dialog_main", "Коэффециент эффективности - Кэ"))
        self.label_Gpr.setText(_translate("Dialog_main", "Модуль коэффециента отражения - |Гпр|"))
        self.label_a.setText(_translate("Dialog_main", "Коэффециент исп. коасксиального перехода - а"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) # Create application
    Dialog_main = QtWidgets.QDialog() # Create form and init UI
    ui = Ui_Dialog_main()
    ui.setupUi(Dialog_main)
    Dialog_main.show()
    sys.exit(app.exec_()) # Run main loop

# Hook logic
def select_mode():
    pass

def select_element():
    pass

def bp_rasshet():
    value_vattmeter = float(ui.vattmeter.text())
    value_tract = float(ui.vattmeter.text())
    attenuation_coefficient = 158.49        # тут должна быть формула перевода децбел в разы
    signal_duration_ceil = 1                    # должна быть определена в choice_resim()
    signal_duration_floor = 1                   # должна быть определена в choice_resim()
    pulse_repetition_rate = 1000                # должна быть определена в choice_resim()
    performance_ratio_Ke_ceil = 1.06                # должна быть определена в select_element()
    performance_ratio_Ke_floor = 0.96               # должна быть определена в select_element()
    coaxial_transition_utilization_rate_a = 0.03    # должна быть определена в select_element()
    converter_reflectance_module = 0.23
    pulse_power_ceil = (value_vattmeter * attenuation_coefficient) / (signal_duration_floor * 10**(-6) * pulse_repetition_rate * (performance_ratio_Ke_floor - 4*coaxial_transition_utilization_rate_a**2) * (1 - converter_reflectance_module**2))
    pulse_power_floor = (value_vattmeter * attenuation_coefficient) / (signal_duration_ceil * 10**(-6) * pulse_repetition_rate * (performance_ratio_Ke_ceil - 4*coaxial_transition_utilization_rate_a**2) * (1 - converter_reflectance_module**2))
    pulse_power_mean = (pulse_power_ceil + pulse_power_floor)/2
    pulse_power_range = (pulse_power_ceil - pulse_power_floor)/2

    ui.pulse_power.display(pulse_power_mean/1000)
    ui.range_pulse_power.display(pulse_power_range/1000)

def bp_metodichka():
    ui.dialog.setText( 'методическое пособие не загружено, потому что разработчика Коныч выгонял из ГРР БРЭК' )

def bp_clear():
    ui.vattmeter.clear()
    ui.dialog.clear()

ui.Rasschet.clicked.connect( bp_rasshet )       # присоединим к нажатию кнопки Rasschet функцию bp_rasshet
ui.Metodichka.clicked.connect( bp_metodichka )  # присоединим к нажатию кнопки Metodichka функцию bp_metodichka
ui.Clear.clicked.connect( bp_clear )            # очистка при нажатии кнопка Clear