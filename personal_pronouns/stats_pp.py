# этот скрипт считает статистику относительно встречаемости личных местоимений для человеческих
# и ИИ текстов

import csv
import numpy as np
from matplotlib import pyplot as plt


with open('AI_Human_PP.csv', 'r', encoding='utf8') as f:
    with open('pp_stats.txt', 'w', encoding='utf8') as f_res:
        reader = csv.DictReader(f, delimiter=',')
        list_ai = []
        list_human = []

        for row in reader:
            if int(row['word_count']) == 0:
                continue
            if row['generated'] == '1.0':
                list_ai.append(int(row['pp_count']))
            else:
                list_human.append(int(row['pp_count']))

        f_res.write(f'Статистика для человеческих текстов:\n'
                    f'Всего текстов: {len(list_human)}\nСреднее: {np.mean(list_human)}\n'
                    f'Медиана: {np.median(list_human)}\nСтандартное отклонение: {np.std(list_human)}\n')

        f_res.write(f'Статистика для ИИ текстов:\n'
                    f'Всего текстов: {len(list_ai)}\nСреднее: {np.mean(list_ai)}\n'
                    f'Медиана: {np.median(list_ai)}\nСтандартное отклонение: {np.std(list_ai)}\n')

        print(max(list_ai))
        print(max(list_human))
        plt.hist(list_human, histtype='step', cumulative=True, bins=len(list_human), )
        plt.hist(list_ai, histtype='step', cumulative=True, bins=len(list_ai))
        plt.show()
