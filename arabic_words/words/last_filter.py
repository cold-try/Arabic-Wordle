alphabet = 'ابتثجحخدذرزسشصضطظعغفقكلمنهويءىئؤةإأ'
ephemere = ''
intermed_list = []
final_list = []

with open("arabic_motus/arabic_words/words/ff3.txt", "r+", encoding='utf-8') as f:
        line = f.readline()
        while line:
            for i in line:
                if i in alphabet:
                    ephemere += i
            intermed_list.append(ephemere)
            ephemere = ''
            line = f.readline()

for i in intermed_list:
    if len(i) > 1:
        if (i[0] + i[1] == 'ال'):
            final_list.append(i[2:])
        else:
            final_list.append(i)

with open('arabic_motus/arabic_words/words/last2.txt', 'w') as f:
    for i in final_list:
        if len(i) == 5:
            f.write(i.replace('\n', '') + '\n')