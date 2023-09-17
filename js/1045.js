// const lines = ['7.0 5.0 7.0']
// const lines = ['6.0 6.0 10.0']
const lines = ['6.0 6.0 6.0']
// const lines = ['5.0 7.0 2.0']
// const lines = ['6.0 8.0 10.0']

const isActue = (a, b, c) => (a * a) < ((b * b) + (c * c))
const isRect = (a, b, c) => (a * a) === ((b * b) + (c * c))
const isObtuse = (a, b, c) => (a * a) > ((b * b) + (c * c))
const isEquilateral = (a, b, c) => a === b && a === c
const isIsoceles = (a, b, c) => {
    if (a === b && a === c) return false
    const hasTwoSameSizes = [
        a === b,
        b === c,
        a === c
    ].includes(true)
    if (!hasTwoSameSizes) return false
    return true
}

const [a, b, c] = lines[0]
    .split(' ')
    .map(parseFloat)
    .sort((a, b) => b - a)
console.log(a, b, c)
if (a >= (b + c)) console.log('NAO FORMA TRIANGULO')
else {
    const result = [
        isActue(a, b, c) && 'ACUTANGULO',
        isRect(a, b, c) && 'RETANGULO',
        isObtuse(a, b, c) && 'OBTUSANGULO',
        isEquilateral(a, b, c) && 'EQUILATERO',
        isIsoceles(a, b, c) && 'ISOSCELES'
    ].filter(e => e)
    result.map(e => console.log(`TRIANGULO ${e}`))
}

