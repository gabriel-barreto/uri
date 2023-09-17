const INITIAL_LETTER_CODE = 65;

function getLetterValue(letter) {
    const letterCode = letter.charCodeAt(0);
    return letterCode - INITIAL_LETTER_CODE;
}

function calculate({ index, phrase }) {
    return phrase
            .split('')
            .reduce((acc, letter, letterIndex) => {
                const letterValue = getLetterValue(letter)
                const value = letterValue + letterIndex + index
                return acc + value
            }, 0)
}

function main(lines) {
    let total = 0;
    let phraseIndex = 0;
    lines
        .slice(1)
        .forEach((item, index) => {
            if (isNaN(item)) {
                const phraseValue = calculate({
                    phrase: item,
                    index: phraseIndex
                })
                total += phraseValue
                phraseIndex += 1;
            }
            else if (index !== 0) {
                console.log(total)
                phraseIndex = 0;
                total = 0;
            }
        })
        console.log(total)
}

const lines = [
    '1',
    '2',
    'CBA',
    'DDD',
    '1',
    'Z',
    '6',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    '6',
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    '1',
    'ZZZZZZZZZZ'
]

main(lines)

