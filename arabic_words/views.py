from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime, timedelta


def words(key):
    with open("arabic_words/words/words.txt", "r+", encoding='utf-8') as f:
        line = f.readline()
        counter=0
        while line:
            counter +=1
            if counter == key:
                break
            line = f.readline()
    return line


def is_in_list(word):
    with open("arabic_words/words/words.txt", "r+", encoding='utf-8') as f:
        line = f.readline()
        the_response = False
        while line:
            if word == line.replace('\n', ''):
                the_response = True
                break
            line = f.readline()
    return the_response


@csrf_exempt
def home(request):
    " CORE "
    today = datetime.today() + timedelta(hours=1)
    currentDate = today.strftime("%m/%d/%y")

    if request.method == 'POST':
        a,b,c = map(int, currentDate.split('/'))
        key = abs(a-c)+b
        solution = list(words(key).replace('\n', ''))
        word_test = request.POST.get('letters')
        score = []
        in_list = is_in_list(word_test)

        if in_list:
            history = {}
            for i in range(0,5):
                history[word_test[i]] = 0

            for i in range(len(solution)):
                if solution[i] == word_test[i]:
                    history[word_test[i]] += 1
                    score.append('y')
                elif word_test[i] in solution:
                    if solution.count(word_test[i]) > history[word_test[i]]:
                        history[word_test[i]] += 1
                        score.append('b')
                    else:
                        score.append('n')
                else:
                    score.append('n')

            if score.count('y') == 5:
                finish = True
            else:
                score.reverse()
                finish = False

            return JsonResponse({'score':score, 'isInList':in_list, 'finish':finish})
        else:
            return JsonResponse({'isInList':in_list})

    else:
        return render(request, 'home.html')