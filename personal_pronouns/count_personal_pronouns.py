# подсчитывает количество личных местоимений в каждом тексте

import csv
import spacy
import os.path as osp


nlp = spacy.load("en_core_web_sm")      # пайплайн для токенизации текстов
dir_path = osp.dirname(osp.dirname(__file__))
pp_table = ['i', 'me', 'you', 'he', 'she', 'it', 'him', 'her', 'we', 'us', 'they', 'them', ]
pp = []


with open(dir_path+'/AI_Human_Wordcount.csv', 'r', encoding='utf8') as f:
    with open('AI_Human_PP.csv', 'w', encoding='utf8', newline='') as f1:

        fieldnames = ['text', 'generated', 'word_count', 'pp_count']
        reader = csv.DictReader(f, delimiter=',')
        writer = csv.DictWriter(f1, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            text = row['text']
            pronouns = 0     # счетчик личных местоимений на текст (обнуляется в начале каждой итерации)
            sentences = text.split('.')

            for sent in sentences:
                doc = nlp(sent + '.')
                save_tokens = []
                for token in doc:
                    if token.text.lower() in pp_table:
                        if (token.dep_ != 'poss') and (token.text != 'US'):
                            pronouns += 1

            writer.writerow({
                'text': text,
                'generated': row['generated'],
                'word_count': row['word_count'],
                'pp_count': pronouns
            })

