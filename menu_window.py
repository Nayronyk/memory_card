from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                              QVBoxLayout, QHBoxLayout)


menu_win = QWidget()
menu_main_v_line = QVBoxLayout()

menu_h_line_1 = QHBoxLayout()
menu_h_line_2 = QHBoxLayout()
menu_h_line_3 = QHBoxLayout()
menu_h_line_4 = QHBoxLayout()
menu_h_line_5 = QHBoxLayout()
menu_h_line_6 = QHBoxLayout()

menu_question_lb = QLabel("Введіть запитання")
menu_question_edit = QLineEdit()
menu_h_line_1.addWidget(menu_question_lb)
menu_h_line_1.addWidget(menu_question_edit)
menu_main_v_line.addLayout(menu_h_line_1)

menu_answer_lb = QLabel("Введіть вірну відповідь")
menu_answer_edit = QLineEdit()
menu_h_line_2.addWidget(menu_answer_lb)
menu_h_line_2.addWidget(menu_answer_edit)
menu_main_v_line.addLayout(menu_h_line_2)

menu_wrong_answer_1_lb = QLabel("Введіть першу хибну відповідь")
menu_wrong_answer_1_edit = QLineEdit()
menu_h_line_3.addWidget(menu_wrong_answer_1_lb)
menu_h_line_3.addWidget(menu_wrong_answer_1_edit)
menu_main_v_line.addLayout(menu_h_line_3)

menu_wrong_answer_2_lb = QLabel("Введіть другу хибну відповідь")
menu_wrong_answer_2_edit = QLineEdit()
menu_h_line_4.addWidget(menu_wrong_answer_2_lb)
menu_h_line_4.addWidget(menu_wrong_answer_2_edit)
menu_main_v_line.addLayout(menu_h_line_4)

menu_wrong_answer_3_lb = QLabel("Введіть третю хибну відповідь")
menu_wrong_answer_3_edit = QLineEdit()
menu_h_line_5.addWidget(menu_wrong_answer_3_lb)
menu_h_line_5.addWidget(menu_wrong_answer_3_edit)
menu_main_v_line.addLayout(menu_h_line_5)

menu_add_question_btn = QPushButton("Додати")
menu_clear_btn = QPushButton("Очистити")
menu_h_line_6.addWidget(menu_add_question_btn)
menu_h_line_6.addWidget(menu_clear_btn)
menu_main_v_line.addLayout(menu_h_line_6)




menu_back_btn = QPushButton("Назад")

menu_main_v_line.addWidget(menu_back_btn)
menu_win.setLayout(menu_main_v_line)
#THE END