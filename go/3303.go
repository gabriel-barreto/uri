package main

import (
	"bufio"
	"fmt"
	"os"
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

func main() {
	userInput := input()
	for _, v := range userInput {
		if len(v) >= 10 {
			fmt.Println("palavrinha")
		} else {
			fmt.Println("palavrao")
		}
	}
}
