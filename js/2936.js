function main(lines) {
    const dChicaPortion = 225
    const portions = [300, 1500, 600, 1000, 150]
    const rounds = lines
        .filter(e => e)
        .map(e => parseInt(e, 10))
    const guestsTotal = rounds.reduce(
        (acc, curr, idx) => acc + (curr * portions[idx])
        , 0)
    const total = guestsTotal + dChicaPortion
    console.log(total)
}

[[1, 1, 1, 1, 1], [2, 2, 2, 2, 2]].map(main)
