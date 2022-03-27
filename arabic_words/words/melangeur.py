import random

words = []

with open("arabic_motus/arabic_words/words/clean.txt", "r+", encoding='utf-8') as f:
    line = f.readline()
    while line:
        words.append(line)
        line = f.readline()

random.shuffle(words)

with open('arabic_motus/arabic_words/words/words.txt', 'w') as f:
    for i in words:
        f.write(i.replace('\n', '') + '\n')