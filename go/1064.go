package main

import (
	"bufio"
	"fmt"
	"os"
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

func parseToFloat(str string) float32 {
	raw := strings.ReplaceAll(str, " ", "")
	val, _ := strconv.ParseFloat(raw, 10)
	return float32(val)
}

func main() {
	userInput := input()
	var positives []float32
	sum := float32(0)
	for _, each := range userInput {
		value := parseToFloat(each)
		if (value >= 0) {
			positives = append(positives, value)
			sum += value
		} 
	}
	avg := (sum / float32(len(positives)))
	fmt.Println(len(positives), "valores positivos")
	fmt.Printf("%.1f\n", avg)
}
