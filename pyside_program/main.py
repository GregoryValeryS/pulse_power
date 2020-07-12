import sys
from PyQt5 import QtWidgets
from ui import Ui_Pulse


def bp_rasshet():
    """Функция считывающает данные, производит рассчёт, выводит результат"""
    # удаляем пробелы, запятые меняем на точки
    value_vattmeter = ui.line_vattmeter.text().replace(' ', '').replace(',', '.')
    # value_vattmeter состоит из цифр
    # или  если в поле одна точка не в начале и не в конце и если остальные символы - цифры
    if value_vattmeter.isdigit() or (value_vattmeter.count('.') == 1 and value_vattmeter.replace('.', '').isdigit()):
        ui.txt_status.append('Расчёт импульсной мощности с диапазоном, '
                              'учитывающим погрешность измерений, произведён успешно.\n')
        value_vattmeter = float(value_vattmeter)
        ui.line_vattmeter.setText(str(value_vattmeter))
        if ui.combo_mode.currentIndex() == 0:  # КП-3
            signal_duration_floor = 1
            signal_duration_ceil = 1
            pulse_repetition_rate = 1000
            performance_ratio_Ke_floor = 0.96
            performance_ratio_Ke_ceil = 1.06
            attenuation_Dp_ampl = 0
            attenuation_Dp_power = 22
            station = 'КП-3'
        else:  # КП-2
            station = 'КП-2'  # к КП-2 подходит только этот переход
            performance_ratio_Ke_floor = 0.93
            performance_ratio_Ke_ceil = 1.05
            attenuation_Dp_ampl = 22.7
            attenuation_Dp_power = 0.5
            if ui.combo_mode.currentIndex() == 1:  # КП-2: 7.5, 10, 15, 60
                signal_duration_floor = 0.1
                signal_duration_ceil = 0.15
                pulse_repetition_rate = 1500
            else:
                signal_duration_floor = 0.5
                if ui.combo_mode.currentIndex() == 4:  # КП-2: 240, 400 обзор сектор
                    signal_duration_ceil = 0.81
                    pulse_repetition_rate = 375
                else:
                    signal_duration_ceil = 0.73
                    if ui.combo_mode.currentIndex() == 2:  # КП-2: 120
                        pulse_repetition_rate = 375
                    else:  # ui.combo_mode.currentIndex() == 3   # КП-2: 240, 400 обзор круг
                        pulse_repetition_rate = 400

        ui.LCD_signal_duration_floor.display(signal_duration_floor)
        ui.LCD_signal_duration_ceil.display(signal_duration_ceil)
        ui.LCD_repetition_rate.display(pulse_repetition_rate)
        ui.LCD_ke_floor.display(performance_ratio_Ke_floor)
        ui.LCD_ke_ceil.display(performance_ratio_Ke_ceil)

        if ui.combo_element.currentIndex() == 0:  # КП-3:   Fн = 8.24 - 12.05 ГГц 5.433.022
            coaxial_transition_utilization_rate_a = 0.03
            converter_reflectance_module = 0.23
            element = 'КП-3'
        elif ui.combo_element.currentIndex() == 1:  # КП-3:        Fн = 4 - 10 ГГц      5.433.021
            coaxial_transition_utilization_rate_a = 0.01
            converter_reflectance_module = 0.167
            element = 'КП-3'
        else:  # ui.combo_element.currentIndex() == 2        # КП-2: Fн = 12.05 - 17.44 ГГц 5.433.023
            coaxial_transition_utilization_rate_a = 0.02
            converter_reflectance_module = 0.286
            element = 'КП-2'

        if element != station:
            value_vattmeter = 0
            ui.txt_status.append('ВНИМАНИЕ! Выбранный вами элемент перехода не подходит'
                                  ' под частотный диапазон режима работы станции.\n')

        ui.LCD_a.display(coaxial_transition_utilization_rate_a)
        ui.LCD_Gpr.display(converter_reflectance_module)
        # удаляем пробелы, запятые меняем на точки
        input_atten_power = ui.line_atten_power.text().replace(' ', '').replace(',', '.')

        if input_atten_power:
            if input_atten_power.isdigit() or (
                    input_atten_power.count('.') == 1 and input_atten_power.replace('.', '').isdigit()):
                # input_atten_ampl состоит из цифр или  если в поле одна точка не в начале и не в конце, a остальные символы - цифры:
                attenuation_Dp_power = float(input_atten_power)
                ui.line_atten_power.setText(str(attenuation_Dp_power))
            else:
                value_vattmeter = 0
                ui.txt_status.append('Ошибка формата данных в "5. Ослабление по мощности".\n')
        input_atten_ampl = ui.line_atten_ampl.text().replace(' ', '').replace(',', '.')
        # удаляем пробелы, запятые меняем на точки

        if input_atten_ampl:
            if input_atten_ampl.isdigit() or (
                    input_atten_ampl.count('.') == 1 and input_atten_ampl.replace('.', '').isdigit()):
                # input_atten_ampl состоит из цифр или
                # если в поле одна точка не в начале и не в конце, a остальные символы - цифры:
                attenuation_Dp_ampl = float(input_atten_ampl)
                ui.line_atten_ampl.setText(str(attenuation_Dp_ampl))
            else:
                value_vattmeter = 0
                ui.txt_status.append('Ошибка формата данных в "4. Ослабление по амплитуде".\n')

        attenuation_ampl = 10 ** (attenuation_Dp_ampl / 20)
        attenuation_power = 10 ** (attenuation_Dp_power / 20)
        attenuation_tract = attenuation_power * attenuation_ampl

        ui.LCD_atten_ampl.display(attenuation_ampl)
        ui.LCD_atten_power.display(attenuation_power)
        ui.LCD_atten_tract.display(attenuation_tract)

        pulse_power_ceil = (value_vattmeter * attenuation_tract) / (
                signal_duration_floor * 10 ** (-6) * pulse_repetition_rate * (
                performance_ratio_Ke_floor - 4 * coaxial_transition_utilization_rate_a ** 2) * (
                        1 - converter_reflectance_module ** 2))
        pulse_power_floor = (value_vattmeter * attenuation_tract) / (
                signal_duration_ceil * 10 ** (-6) * pulse_repetition_rate * (
                performance_ratio_Ke_ceil - 4 * coaxial_transition_utilization_rate_a ** 2) * (
                        1 - converter_reflectance_module ** 2))
        pulse_power_mean = (pulse_power_ceil + pulse_power_floor) / 2
        pulse_power_range = (pulse_power_ceil - pulse_power_floor) / 2
        ui.pulse_power.display(pulse_power_mean / 1000)
        ui.range_pulse_power.display(pulse_power_range / 1000)

        if pulse_power_mean > 500000:
            ui.txt_status.append('Расчёт импульсной мощности произведён, но полученное значение '
                                  'характеристки значительно выше указанных в ТТХ станций.\n\n'
                                  'Проверьте правильность заполнения 3, 4, 5 окон, '
                                  'обратите внимание на единицы измерения величин.\n')
    else:
        ui.txt_status.append('Ошибка формата данных в "3. Показания ваттметра".\n')


def bp_manual():
    """Вывод инструкции эксплуатации программы"""
    ui.txt_status.append('Большая часть параметров определяется автоматически.\n\n'
                          'В пункте "1" выберете станцию и режим работы.\n'
                          'В пункте "2" выберете элемент перехода из комплекта ваттметра.\n'
                          'В пункте "3" внесите показания ваттметра в кВт.\n\n'
                          'Пункты "4" и "5" заполянются автоматически для тракта, собранного БРЭК в/ч 45097, '
                          'но Вы можете указать значения на основе собранного вами тракта, '
                          'обратите внимание на различие ослабления по амплитуде и по мощности.\n\n')


def bp_clear():
    """Очистка всех заполняемых полей"""
    ui.txt_status.append('Очистка полей выполнена\n')
    ui.line_vattmeter.clear()
    ui.line_atten_ampl.clear()
    ui.line_atten_power.clear()
    ui.LCD_atten_ampl.display(0)
    ui.LCD_atten_power.display(0)
    ui.LCD_atten_tract.display(0)
    ui.pulse_power.display(0)
    ui.range_pulse_power.display(0)


def main():
    global ui
    """Функция инициализации приложения"""
    # Create application - инициализация приложения
    app = QtWidgets.QApplication(sys.argv)
    # Create form and init UI - инициализация формы
    Pulse = QtWidgets.QWidget()
    ui = Ui_Pulse()
    ui.setupUi(Pulse)
    Pulse.show()

    ui.button_Clear.clicked.connect(bp_clear)  # очистка при нажатии кнопка Clear
    ui.button_Calculation.clicked.connect(bp_rasshet)  # присоединим к нажатию кнопки Rasschet функцию bp_rasshet
    # сейчас мне стыдно за такие названия кнопок, типа Rasschet, но переписывать не буду
    ui.button_Manual.clicked.connect(bp_manual)  # присоединим к нажатию кнопки Методичка функцию bp_clear

    ui.txt_status.append('Программа "Pulse Power" иницирована и готова к использованию\n'
                         'Версия - Beta 0.2\n'
                         'Связь с автором - Г.Скворцов GregoryValeryS@gmail.com\n'
                         'GNU General Public License v3.0\n')

    sys.exit(app.exec_())  # Run main loop

if __name__ == '__main__':
    main()
