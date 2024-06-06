import csv
import collections

cnt = collections.Counter()

with open("once_seen_indices.csv", "r", encoding='utf8') as f_index:
    reader = csv.DictReader(f_index, delimiter=',')
    for row in reader:
        cnt[row['count']] += 1      # счетчик  формата "номер текста - количество одиноких слов" (переформатируем
        # файл once_seen_indices.csv, там данные в виде "слово - номер текста"

with open('once_seen_counts.csv', 'w', encoding='utf8', newline='') as f_output:
    with open('AI_Human_cut.csv', 'r', encoding='utf8') as f_data:
        reader_data = csv.DictReader(f_data, delimiter=',')
        writer = csv.DictWriter(f_output, fieldnames=['text', 'generated', 'once_seen_count'])
        counter = 0
        writer.writeheader()
        for row in reader_data:     # записываем данные в формате "текст, сгенерированность, количество одиноких слов"
            a = str(counter)
            if a in cnt.keys():
                writer.writerow({'text': row['text'],
                                 'generated': row['generated'],
                                 'once_seen_count': cnt[a]})
            else:
                writer.writerow({'text': row['text'],
                                 'generated': row['generated'],
                                 'once_seen_count': 0})
            counter += 1
