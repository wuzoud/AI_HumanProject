# подсчитывает количество слов в каждом тексте

import csv
import re

with open('AI_Human_cut.csv', 'r', encoding='utf8') as f:
    with open('AI_Human_Wordcount.csv', 'w', encoding='utf8', newline='') as f1:

        fieldnames = ['text', 'generated', 'word_count']
        reader = csv.DictReader(f, delimiter=',')
        writer = csv.DictWriter(f1, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            text = row['text']
            word_count = len(re.findall(r'\w+', text))

            writer.writerow({
                'text': text,
                'generated': row['generated'],
                'word_count': word_count
            })