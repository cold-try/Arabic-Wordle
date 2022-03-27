function correctionColor(results, limit) {
    var cases = document.getElementsByClassName('case');
    var c = 0;

    for (var i=limit-5; i<limit; i++) {
        if (results[c] == 'y') {
            cases[i].className = 'case true';
            document.querySelector("[data-key='"+cases[i].innerHTML+"']").className = 'letter-target true';
        } 
        else if (results[c] == 'b') {
            cases[i].className = 'case truebut';
            document.querySelector("[data-key='"+cases[i].innerHTML+"']").className = 'letter-target truebut';
        }
        else {
            cases[i].className = 'case empty';
            document.querySelector("[data-key='"+cases[i].innerHTML+"']").className = 'letter-target empty';
        }
        c+=1
    }
}

function finishFrame(secretWord) {
    const modalBackDrop = document.getElementById('modal-backdrop');
    const frame = document.getElementById('finish');
    const secretWordSpan = document.getElementById('mot-cache');
    frame.className = "basic on";
    modalBackDrop.className = "show";
    secretWordSpan.innerHTML = secretWord;
}

function calculScore() {
    const cases = document.getElementsByClassName('case');
    var score = 0;
    for (var i=cases.length-5; i<cases.length; i++) {
        if (cases[i].className == 'case true') {
            score += 2
        } 
        else if (cases[i].className == 'case truebut') {
            score += 1
        }
    }
    return score*10
}

function looseFrame() {
    const modalBackDrop = document.getElementById('modal-backdrop');
    const frame = document.getElementById('loose');
    const scoreSpan = document.getElementById('score');
    frame.className = "basic on";
    modalBackDrop.className = "show";
    scoreSpan.innerHTML = calculScore();
}

function resetFrame() {
    var frame = document.getElementById('box');
    frame.className = "fixed";
}

function notInList() {
    var frame = document.getElementById('box');
    frame.className = "fixed anim";
    setTimeout(resetFrame, 3000);
}

async function ajaxTestLetters(letters, limit) {
    let formData = new FormData();
    formData.append('letters', letters);

    const url = "http://127.0.0.1:8000"; 
    const request = new Request(url, {method: 'POST', body: formData});
    var inList = true;
    var isFinish = false;

    const response = await fetch(request);
    const result = await response.json();
    if (result.isInList) {
        correctionColor(result.score, limit);
        if (result.finish) {
            finishFrame(letters);
            isFinish = true;
        }
    } else {
        notInList();
        inList = false;
    }
    return {inList, isFinish}
}

function completion(letter, word, row) {
    var cases = document.getElementsByClassName('case');
    var limit = 5*row;
    var letters = word;   
    var count = 1;

    for (var i=limit-5; i<limit; i++) {
        if (letter=='←') {
            if (letters.length > 0) {
                letters = letters.substring(0, letters.length-1);
                cases[(limit-letters.length)-1].innerHTML = '';
            }
            break
        } else {
            if (cases[limit-count].innerHTML == '') {
                cases[limit-count].innerHTML = letter;
                letters = letters+letter;
                break
            }
        }
        count += 1;
    }
    return letters
}

const letterTarget = document.getElementsByClassName('letter-target');
const submitButton = document.getElementById('submitLetters');
const openHelpModal = document.getElementById('help-modal')
const closeHelpModal = document.getElementById('out-of-mod');
const modalHelp = document.getElementById('help');
const modalBackDrop = document.getElementById('modal-backdrop');
var unlock = false;
var result = '';
var row = 1;

////////////////////////////////  EVENTS  //////////////////////////////////

openHelpModal.addEventListener("click", event => {
    event.preventDefault();
    modalHelp.className = 'on';
    modalBackDrop.className = 'show';
});

closeHelpModal.addEventListener("click", event => {
    event.preventDefault();
    modalHelp.className = 'off';
    modalBackDrop.className = 'fade';
});

submitButton.addEventListener("click", event => {
    event.preventDefault();
    if (result.length == 5 && unlock) {
        var limit = 5*row;
        unlock = false;
        
        ajaxTestLetters(result, limit)
        .then((data) => {
            if (!data.isFinish) {
                if (data.inList) {
                    row+=1;
                    result='';
                    if (row>6) {
                        looseFrame();
                    }
                }
            } 
        });
    };
});

for (var i = 0; i < letterTarget.length; i++) {
    letterTarget[i].addEventListener('click', event => {
        event.stopPropagation();
        result = completion(event.target.getAttribute("data-key"), result, row);
        unlock = true;
    });
}