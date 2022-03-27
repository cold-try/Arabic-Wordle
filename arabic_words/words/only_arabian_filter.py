alphabet = 'ابتثجحخدذرزسشصضطظعغفقكلمنهويءىئؤةإأ'
intermed_list = []
arabian_list = []

with open("arabic_motus/arabic_words/words/ff.txt", "r+", encoding='utf-8') as f:
        line = f.readline()
        while line:
            x = line.split(' ')
            for i in x:
                bef_app = i.split('\t')
                for xx in bef_app:
                    intermed_list.append(xx)
            line = f.readline()

# only arabian filter
for i in intermed_list:
    for x in i:
        if x in alphabet and i not in arabian_list:
            arabian_list.append(i)
