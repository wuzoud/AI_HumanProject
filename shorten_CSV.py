# этот скрипт равномерное обрезает исходный датасет до объема в 120 000 строк

import csv

with open('AI_Human.csv', 'r', encoding='utf8') as f_input:     # исходный файл
    with open('AI_Human_cut.csv', 'w', encoding='utf8', newline='') as f_output:        # обрезанный файл
        reader = csv.reader(f_input, delimiter=',')
        writer = csv.writer(f_output, delimiter=',')
        step = -1
        for row in reader:
            if (step % 4 == 0) or step == -1:   # записываем файлы из исходного с шагом 5
                writer.writerow(row)
            if step >= 480000 - 1:
                print(row)
                break
            step += 1
