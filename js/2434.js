const lines = [
    '6 -200',
    '-100',
    '1000',
    '-2000',
    '100',
    '-50',
    '2000'
]

const [, initialBalance] = lines[0]
    .split(' ')
    .map(e => parseInt(e, 10))
let lowestBalance = initialBalance
lines
    .slice(1)
    .map(e => parseInt(e, 10))
    .filter(e => !Number.isNaN(e))
    .reduce((acc, curr) => {
        const currentBalance = acc + curr
        if (currentBalance < lowestBalance) {
            lowestBalance = currentBalance
        }
        return currentBalance
    }, initialBalance)

console.log(lowestBalance)

