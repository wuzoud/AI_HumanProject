import spacy
import os


nlp = spacy.load("en_core_web_sm")

pp_table = ['I','me', 'you', 'he', 'she', 'it', 'him', 'her', 'we', 'us', 'they', 'them']

pp = []

text = "I love her eyes."
sentences = text.split('.')

for sent in sentences:
    doc = nlp(sent+'.')
    save_tokens = []
    keep = True
    for token in doc:
        print(f"{token.text} ({token.dep_})")
    print('---------------------------------------------')
    # print('-------------------------')
    # for token in doc:
    #     if token.dep_ == 'nsubj':
    #         keep = False
    #         continue
    #     # print(f"{token.text}({token.dep_})")
    #     if token.dep_ == 'advcl' or token.dep_ == 'acl':
    #         save_tokens.append(token.text)
    #         # for i in token.children:
    #         #     if i.dep_ == 'nsubj':
    #         #         keep = False
    #         continue
    #     if token.dep_ == 'punct':
    #         if keep:
    #             clauses.extend(save_tokens)
    #         keep = True
    #         save_tokens = []

for i in pp:
    print(i)
    index = text.index(i)
    text = text[:index] + text[index:index + len(i)].upper() + text[index + len(i):]
