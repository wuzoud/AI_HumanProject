# этот скрипт считает, сколько раз встретилось каждое слово во всех текстах вместе и записывает
# результат в файл word_count.csv

import collections
import csv
import spacy


nlp = spacy.load("en_core_web_sm")      # пайплайн для токенизации текстов

cnt = collections.Counter()     # счетчик слов

fieldnames = ['word', 'count']

with open('AI_Human_cut.csv', 'r', encoding='utf8') as f:

    rows_cnt = 0     # счетчик всех обработанных текстов на случай, если программу придется преждевременно прервать
    reader = csv.DictReader(f, delimiter=',')

    try:
        for row in reader:
            text = row['text']
            doc = nlp(text)
            for token in doc:
                cnt[token.text.lower()] += 1
            rows_cnt += 1

    except KeyboardInterrupt:       # событие преждевременной остановки программы
        with open('word_count.csv', 'w', encoding='utf8', newline='') as f1:    # запись в файл
            writer = csv.writer(f1)
            writer.writerow(fieldnames)
            for key, value in cnt.items():
                writer.writerow([key] + [value])
            print(rows_cnt)

    with open('word_count.csv', 'w', encoding='utf8', newline='') as f1:   # запись в файл по завершении подсчетов
        writer = csv.writer(f1)
        writer.writerow(fieldnames)
        for key, value in cnt.items():
            writer.writerow([key] + [value])
