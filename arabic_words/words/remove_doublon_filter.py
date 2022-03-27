words = []
counter = 0
with open("arabic_motus/arabic_words/words/last.txt", "r+", encoding='utf-8') as f:
    line = f.readline()
    while line:
        if line not in words:
            words.append(line)
        else:
            counter += 1
        line = f.readline()

print('')
print(f'{counter} DOUBLONS SUPPRIMES !')
print('')

with open('arabic_motus/arabic_words/words/clean.txt', 'w') as f:
    for i in words:
        f.write(i.replace('\n', '') + '\n')