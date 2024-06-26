from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint

def show_result():
    xboxground.hide()
    answer_box.show()
    answer.setText('Следующий ворос')

class Question():
    def __init__(self, quasion, rans, wan1, wan2, wan3):
        self.question = quasion
        self.rans = rans
        self.wan1 = wan1
        self.wan2 = wan2
        self.wan3 = wan3


def show_question():
    xboxground.show()
    answer_box.hide()
    
    answer.setText('Ответить')
    butgroup.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    butgroup.setExclusive(True)

'''def start_test():
    if answer.text() == 'Ответить':
        show_result()
    else:
        show_question()'''

def ask(q: Question):
    shuffle(listbut)
    listbut[0].setText(q.rans)
    listbut[1].setText(q.wan1)
    listbut[2].setText(q.wan2)
    listbut[3].setText(q.wan3)

    quasion.setText(q.question)
    truans.setText(q.rans)
    show_question()

def  show_correct(result):
    resulte.setText(result)
    show_result()

def check_answer():
    if listbut[0].isChecked():
        show_correct('Правильно!!!!')
        main_win.score +=1
        print('Стаистика:')
        print('-Всего вопросов:', main_win.total)
        print('-Всего ответов:', main_win.score)
        print('Рейтинг:', main_win.score/main_win.total*100)
    elif listbut[1].isChecked() or listbut[2].isChecked() or listbut[3].isChecked():
        show_correct('Неправильно')
        print('Стаистика:')
        print('-Всего вопросов:', main_win.total)
        print('-Всего ответов:', main_win.score)
        print('Рейтинг:', main_win.score/main_win.total*100)

def next_question():

    main_win.total += 1
    n = randint(0, len(quas)-1)
    qquas = quas[n]
    ask(qquas)
    
def click_okey():
    if answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()



# СОЗДАЕ=ЁМ ОКНО ПРИЛОЖЕНИ
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Викторина')
main_win.move(900, 70)
main_win.resize(400, 200)
#пНЕЛЬ ВОПРОСА
quasion = QLabel('Какой из этих стран не существует?')

main_win.total = 1
main_win.score = 0

button1 = QRadioButton('СССР')
button2 = QRadioButton('США')
button3 = QRadioButton('Бразилия')
button4 = QRadioButton('Ватикан')

listbut = [button1, button2, button3, button4]

butgroup = QButtonGroup()
butgroup.addButton(button1)
butgroup.addButton(button2)
butgroup.addButton(button3)
butgroup.addButton(button4)

answer = QPushButton('Ответить')


xboxground = QGroupBox('Подумай внимательно:')
#linii
boxline_h = QHBoxLayout()
boxlinev1 = QVBoxLayout()
boxlinev2 = QVBoxLayout()




boxlinev1.addWidget(button1)
boxlinev1.addWidget(button2)

boxlinev2.addWidget(button3)
boxlinev2.addWidget(button4)

boxline_h.addLayout(boxlinev1)
boxline_h.addLayout(boxlinev2)

xboxground.setLayout(boxline_h)





#ХЕШТЕГ

answer_box = QGroupBox('Резултат тетса')
resulte = QLabel('Правильно/неправильно')
truans = QLabel('Молодец!')

ans_lay_v = QVBoxLayout()
ans_lay_v.addWidget(resulte, alignment=(Qt.AlignLeft | Qt.AlignTop))
ans_lay_v.addWidget(truans, alignment=Qt.AlignCenter, stretch = 2)
answer_box.setLayout(ans_lay_v)


#хЕЩТЕ РАЗМЕЩАЕМ КРЕПИМ
main_line_v = QVBoxLayout()



Mainline_h1 = QHBoxLayout()
Mainline_h1.addStretch(0)
Mainline_h1.addWidget(quasion, alignment=Qt.AlignLeft)
Mainline_h1.addStretch(0)

Mainline_h2 = QHBoxLayout()
Mainline_h2.addStretch(0)
Mainline_h2.addWidget(xboxground)
Mainline_h2.addWidget(answer_box)
answer_box.hide()
Mainline_h2.addStretch(0)

Mainline_h3 = QHBoxLayout()
Mainline_h3.addStretch(0)
Mainline_h3.addWidget(answer, alignment=Qt.AlignLeft)
Mainline_h3.addStretch(0)

#main_line_v.addWidget(answer, alignment=Qt.AlignCenter, stretch = 0)

#щещтег размещяем на вертикаль!!

main_line_v = QVBoxLayout()



main_line_v.addLayout(Mainline_h1)
main_line_v.addStretch(0)
main_line_v.addLayout(Mainline_h2)
main_line_v.addStretch(0)
main_line_v.addLayout(Mainline_h3)


main_win.setLayout(main_line_v)



quas = []

quas.append(Question('Какой из этих стран в наше время не существует?', 'СССР', 'США', 'Бразилия', 'Ватикан'))
quas.append(Question('Какого цвета нет на флаге Росии?', 'Жёлтый', 'Красный', 'Синий', 'Белый'))
quas.append(Question('Какой из этих знаков является вопросительным?', '?', '/', '.', ','))





answer.clicked.connect(click_okey)


main_win.show()
app.exec_()