const notes = [100, 50, 20, 10, 5, 2, 1]

function countNotes(value, notesCount = [], noteIndex = 0) {
    if (noteIndex === notes.length) return notesCount
    const noteValue = notes[noteIndex]
    const noteCount = Math.trunc(value / noteValue)
    const rest = value % noteValue
    return countNotes(rest, [...notesCount, noteCount], noteIndex + 1)
}

function main(lines) {
    const value = parseInt(lines[0], 10)
    const notesCount = countNotes(value)
    console.log(value)
    notesCount.forEach((noteCount, i) => {
        console.log(`${noteCount} nota(s) de R$ ${notes[i]},00`)
    })
}

[['576'], ['11257'], ['503'], ['1257']].forEach(main)
