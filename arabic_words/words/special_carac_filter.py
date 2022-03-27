alphabet = 'ابتثجحخدذرزسشصضطظعغفقكلمنهويءىئؤةإأ'
intermed_list = []
second_list = []
third_list = []
third_list2 = []
fourth_list = []

with open("arabic_motus/arabic_words/words/ff2.txt", "r+", encoding='utf-8') as f:
        line = f.readline()
        while line:
            x = line.split(' ')
            for i in x:
                intermed_list.append(i)
            line = f.readline()

for i in intermed_list:
    x = i.split('/')
    for i in x:
        second_list.append(i)

for i in second_list:
    x = i.split('،')

    for i in x:
        third_list.append(i)

for i in third_list:
    x = i.split('-')

    for i in x:
        third_list2.append(i)


for i in third_list2:
    for e in i:
        if e in alphabet and i not in fourth_list:
            fourth_list.append(i)


with open('arabic_motus/arabic_words/words/ff3.txt', 'w') as f:
    for i in fourth_list:
        f.write(i.replace('\n', '') + '\n')