package main

import (
	"fmt"
	"os"
	"strings"
)

func getInputs(filePath string) []string {
	dat, err := os.ReadFile(filePath)
	if err != nil {
		panic(err)
	}
	inputString := string(dat)
	inputSlice := strings.Split(inputString, "\n")
	return inputSlice
}

func determineWinner(me string, elf string) int {
	if me == "A" {
		if elf == "A" {
			return 3
		}
		if elf == "B" {
			return 0
		}
		if elf == "C" {
			return 6
		}
	}
	if me == "B" {
		if elf == "A" {
			return 6
		}
		if elf == "B" {
			return 3
		}
		if elf == "C" {
			return 0
		}
	}
	if me == "C" {
		if elf == "A" {
			return 0
		}
		if elf == "B" {
			return 6
		}
		if elf == "C" {
			return 3
		}
	}
	panic("no winner determined")
}

func determineRequiredShape(elf string, outcome string) string {
	if outcome == "X" {
		if elf == "A" {
			return "C"
		}
		if elf == "B" {
			return "A"
		}
		if elf == "C" {
			return "B"
		}
	}
	if outcome == "Y" {
		return elf
	}
	if outcome == "Z" {
		if elf == "A" {
			return "B"
		}
		if elf == "B" {
			return "C"
		}
		if elf == "C" {
			return "A"
		}
	}
	panic("unable to determine correct play")
}

func getShapeScore(shape string) int {
	switch shape {
	case "A":
		return 1
	case "B":
		return 2
	case "C":
		return 3
	}
	panic("cannot determine shape score")
}

func main() {
	inputs := getInputs("./input")
	scoreAccumulator := 0
	for _, v := range inputs {
		choices := strings.Split(v, " ")
		outcome := choices[1]
		elf := choices[0]
		me := determineRequiredShape(elf, outcome)
		roundScore := determineWinner(me, elf)
		shapeScore := getShapeScore(me)
		score := roundScore + shapeScore
		scoreAccumulator += score
	}
	fmt.Print(scoreAccumulator)

}
