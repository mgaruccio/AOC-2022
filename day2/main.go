package main

import (
	"fmt"
	"os"
	"strings"
)

func position(ss []string, s string) int {
	for i, v := range ss {
		if v == s {
			return i
		}
	}
	panic("unable to find position of string in slide")
}

// func rotatess(ss []string, k int) []string {
// 	if k < 0 || len(ss) == 0 {
// 		return ss
// 	}

// 	r := len(ss) - k%len(ss)

// 	ss = append(ss[r:], ss[:r]...)

// 	return ss
// }

func findRotatedItem(ss []string, k int) string {
	i := len(ss) - k - 1
	return ss[i]
}

func rotateis(is []int, k int) []int {
	if k < 0 || len(is) == 0 {
		return is
	}

	r := len(is) - k%len(is)

	is = append(is[r:], is[:r]...)

	return is
}

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
	intArr := []int{3, 0, 6}
	stringArr := []string{"A", "B", "C"}
	rotation := 0
	if me == "A" {
		rotation = 0
	}
	if me == "B" {
		rotation = 1
	}
	if me == "C" {
		rotation = 2
	}
	pos := position(stringArr, elf)
	rotatedArr := rotateis(intArr, rotation)
	return rotatedArr[pos]
}

func determineRequiredShape(elf string, outcome string) string {
	arr := []string{"A", "B", "C"}
	rotation := 0
	if outcome == "X" {
		rotation = 2
	}
	if outcome == "Z" {
		rotation = 1
	}
	pos := position(arr, elf)
	return findRotatedItem(arr, rotation+pos)
	// return rotatedArr[pos]
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
	determineRequiredShape("A", "Y")
	for _, v := range inputs {
		choices := strings.Split(v, " ")
		outcome := choices[1]
		elf := choices[0]
		fmt.Println(elf + " " + outcome)
		me := determineRequiredShape(elf, outcome)
		roundScore := determineWinner(me, elf)
		shapeScore := getShapeScore(me)
		score := roundScore + shapeScore
		scoreAccumulator += score
	}
	fmt.Print(scoreAccumulator)

}
