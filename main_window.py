from PyQt6.QtWidgets import (QWidget,
                             QVBoxLayout, QHBoxLayout,
                             QPushButton, QRadioButton,
                             QGroupBox, QButtonGroup,
                             QLabel
                             )

main_win = QWidget()


main_win.resize(800,600)
main_win.setWindowTitle("Memory Card")


main_v_line = QVBoxLayout()


menu_btn = QPushButton("Меню")
question_text = QLabel("тут буде текст питання")

Radio_box = QGroupBox("Варіанти відповідей")

radio_group = QButtonGroup()

radio_btn_1 = QRadioButton("1")
radio_btn_2 = QRadioButton("2")
radio_btn_3 = QRadioButton("3")
radio_btn_4 = QRadioButton("4")

radio_group.addButton(radio_btn_1)
radio_group.addButton(radio_btn_2)
radio_group.addButton(radio_btn_3)
radio_group.addButton(radio_btn_4)

box_v_line = QVBoxLayout()
box_h_line_1 = QHBoxLayout()
box_h_line_2 = QHBoxLayout()

box_h_line_1.addWidget(radio_btn_1)
box_h_line_1.addWidget(radio_btn_2)
box_h_line_2.addWidget(radio_btn_3)
box_h_line_2.addWidget(radio_btn_4)


box_v_line.addLayout(box_h_line_1)
box_v_line.addLayout(box_h_line_2)

Radio_box.setLayout(box_v_line)

answer_box = QGroupBox()

answer_line = QVBoxLayout()
    
result_text = QLabel("правильно/неправильно")
correct_text = QLabel("тут буде текст правильної відповіді")

answer_line.addWidget(result_text)
answer_line.addWidget(correct_text)

answer_box.setLayout(answer_line)

next_btn = QPushButton("Відповісти")

main_v_line.addWidget(menu_btn)
main_v_line.addWidget(question_text)
main_v_line.addWidget(Radio_box)
main_v_line.addWidget(answer_box)
main_v_line.addWidget(next_btn)


answer_box.hide()

main_win.setLayout(main_v_line)
