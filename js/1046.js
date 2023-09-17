function main(lines) {
    const [raw] = lines
    const [begin, end] = raw.split(' ').map(e => parseInt(e))

    function getDuration() {
        if (begin === end) return 24
        if (begin > end) {
            const restOfTheDay = 24 - begin
            return restOfTheDay + end
        } 
        return end - begin
    }

    console.log(`O JOGO DUROU ${getDuration()} HORA(S)`)
}

[['16 2'], ['0 0'], ['2 16']].map(main)
