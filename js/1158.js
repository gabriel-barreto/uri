const lines = ['2', '4 3', '11 2']

function sumNextOdds(count, num) {
    let sum = 0;
    let counter = 0;
    let x = num;
    while(counter < count) {
        if (x % 2 !== 0) {
            sum += x;
            counter += 1;
        }
        x += 1;
    }
    console.log(sum)
}

lines
    .slice(1)
    .filter(e => e)
    .map((e) => {
        const [num, count] = e.split(' ').map(e => parseInt(e, 10))
        sumNextOdds(count, num)
    })

