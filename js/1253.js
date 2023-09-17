const INIT_ALPHA_CHAR_CODE = 65
const FINAL_ALPHA_CHAR_CODE = 91

function decryptLetter({ letter, times }) {
  const encryptedCharCode = letter.charCodeAt(0)
  function getDecryptedCharCode() {
    if (encryptedCharCode - times < INIT_ALPHA_CHAR_CODE) {
        const diff = INIT_ALPHA_CHAR_CODE - (encryptedCharCode - times)
        return FINAL_ALPHA_CHAR_CODE - diff
    }
    return encryptedCharCode - times
  }
  const decryptedCharCode = getDecryptedCharCode()
  const decryptedLetter = String.fromCharCode(decryptedCharCode)
  return decryptedLetter
}

function decrypt({ phrase, rawTimes }) {
    const times = parseInt(rawTimes, 10)
    const decryptedPhrase = phrase
        .split('')
        .map(letter => decryptLetter({ letter, times }))
        .reduce((acc, curr) => acc + curr, '')
    return decryptedPhrase
}

const [rounds, ...inputs] = lines

for (let i = 1; i <= rounds * 2; i += 2) {
    const [phrase, rawTimes] = lines.slice(i, i + 2)
    console.log(decrypt({ phrase, rawTimes }))
}

