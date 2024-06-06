# этот скрипт ищет все "одинокие" слова, а затем записывает их в csv-файл вместе с индексом текста,
# в котором это слово встречается

import csv
import spacy


nlp = spacy.load("en_core_web_sm")      # пайплайн для токенизации текстов

cnt = {}    # счетчик-словарь, в котором ключи будут слова, а в значения - индекс текста, если слово "одинокое"
# и "_", если  слово встречается больше одного раза

fieldnames = ['word', 'count']

with open('AI_Human_cut.csv', 'r', encoding='utf8') as f_data:
    with open('once_seen_indices.csv', 'w', encoding='utf8', newline='') as f_output:

        reader = csv.DictReader(f_data, delimiter=',')
        writer = csv.writer(f_output)

        row_num = 0     # счетчик, номер строки, на которой мы находимся, т.е. индекс текста

        for row in reader:

            text = row['text']
            doc = nlp(text)
            for token in doc:
                if token.text in cnt.keys():
                    cnt[token.text] = '_'
                else:
                    cnt[token.text] = row_num

            row_num += 1

        writer.writerow(fieldnames)
        for key, value in cnt.items():
            if value != '_':
                writer.writerow([key] + [value])


