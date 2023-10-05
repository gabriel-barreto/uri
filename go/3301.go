package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func input() []string {
	scanner := bufio.NewScanner(os.Stdin)
	var input []string
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			break
		}
		input = append(input, line)
	}
	return input
}

type Nephew struct {
	Name string
	age int64
}

func parseInt(str string) int64 {
	num, err := strconv.ParseInt(str, 10, 0)
	if err != nil {
		fmt.Println(str, err)
		return 0
	}
	return num
}

func main() {
	userInput := input()
	ages := strings.Split(userInput[0], " ")
	nephews := []Nephew{
		Nephew{Name: "huguinho", age: parseInt(ages[0])},
		Nephew{Name: "zezinho", age: parseInt(ages[1])},
		Nephew{Name: "luisinho", age: parseInt(ages[2])},
	}
	sort.Slice(
		nephews,
		func (i, j int) bool { return nephews[i].age < nephews[j].age },
	)
	fmt.Println(nephews[1].Name)
}