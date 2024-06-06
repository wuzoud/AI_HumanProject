# этот скрипт подсчитывает примерное количество причастных оборотов в каждом тексте и записывает
# в новый файл вместе с текстом и его категорией (generated/non-generated)

import csv
import spacy
import os.path as osp


nlp = spacy.load("en_core_web_sm")      # пайплайн для токенизации текстов
dir_path = osp.dirname(osp.dirname(__file__))

with open(dir_path+'/AI_Human_cut.csv', 'r', encoding='utf8') as f:
    with open('AI_Human_Counted.csv', 'w', encoding='utf8', newline='') as f1:

        fieldnames = ['text', 'generated', 'clause_count']
        reader = csv.DictReader(f, delimiter=',')
        writer = csv.DictWriter(f1, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            text = row['text']
            clauses = 0     # счетчик причастных оборотов на текст (обнуляется в начале каждой итерации)
            sentences = text.split('.')     # разбивает текст на предложения

            for sent in sentences:
                doc = nlp(sent + '.')
                # save_tokens = []
                clause_count = 0        # счетчик причастных оборотов на каждое предложение
                keep = True     # если True, то добавляем найденный причастный оборот в счетчик
                # print('-------------------------')
                for token in doc:
                    # print(f"{token.text}({token.dep_})")
                    if token.dep_ in {'nsubj', 'csubj', 'nsubjpass', 'csubjpass'}:
                        keep = False        # если видим подлежащее, то пропускаем отделенную знаками препинания часть
                        continue            # т.к. в таком случае это не причастный оборот
                    if token.dep_ == 'advcl' or token.dep_ == 'acl':        # проверка на причастие
                        # save_tokens.append(token.text)
                        clause_count += 1
                        # for i in token.children:
                        #     if i.dep_ == 'nsubj':
                        #         keep = False
                        continue
                    if token.dep_ == 'punct':       # если видим знак препинания, то подсчитываем накопившееся
                        if keep:
                            clauses += clause_count
                        keep = True
                        clause_count = 0

            writer.writerow({
                'text': text,
                'generated': row['generated'],
                'clause_count': clauses
            })

