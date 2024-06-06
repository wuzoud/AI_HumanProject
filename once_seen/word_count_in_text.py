# подсчитывает количество слов в каждом тексте

import csv
import re

with open('once_seen_counts.csv', 'r', encoding='utf8') as f:
    with open('once_seen_count_with_words.csv', 'w', encoding='utf8', newline='') as f1:

        fieldnames = ['text', 'generated', 'once_seen_count', 'word_count']
        reader = csv.DictReader(f, delimiter=',')
        writer = csv.DictWriter(f1, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            text = row['text']
            word_count = len(re.findall(r'\w+', text))

            writer.writerow({
                'text': text,
                'generated': row['generated'],
                'once_seen_count': row['once_seen_count'],
                'word_count': word_count
            })