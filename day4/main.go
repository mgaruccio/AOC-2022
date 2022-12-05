package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getInputs(filePath string) [][]string {
	dat, err := os.ReadFile(filePath)
	if err != nil {
		panic(err)
	}
	inputString := string(dat)
	inputSlice := strings.Split(inputString, "\n")
	iss := [][]string{}
	for _, s := range inputSlice {
		splitInput := strings.Split(s, ",")
		iss = append(iss, splitInput)
	}
	return iss
}

func makeRange(min int, max int) []int {
	arr := make([]int, max-min+1)
	for i := range arr {
		arr[i] = min + i
	}
	return arr
}

func convertZone(zone string) []int {
	splitZone := strings.Split(zone, "-")
	min, err := strconv.Atoi(splitZone[0])
	if err != nil {
		panic(err)
	}
	max, err := strconv.Atoi(splitZone[1])
	if err != nil {
		panic(err)
	}
	return []int{min, max}
}

func compareZones(x []int, y []int) bool {
	if x[0] >= y[0] && x[1] <= y[1] {
		return true
	} else {
		return false
	}
}

func intInSlice(k int, is []int) bool {
	for _, i := range is {
		if i == k {
			return true
		}
	}
	return false
}

func compareZonesTwo(x []int, y []int) bool {
	xr := makeRange(x[0], x[1])
	yr := makeRange(y[0], y[1])

	for _, i := range xr {
		present := intInSlice(i, yr)
		if present {
			return true
		}
	}
	return false
}

func main() {
	inputs := getInputs("input")
	phaseOneResults := 0
	for _, input := range inputs {
		elfOne := convertZone(input[0])
		elfTwo := convertZone(input[1])
		if compareZones(elfOne, elfTwo) || compareZones(elfTwo, elfOne) {
			phaseOneResults += 1
		}
	}
	phaseOneString := strconv.Itoa(phaseOneResults)

	fmt.Println("Phase 1 = " + phaseOneString)

	phaseTwoResults := 0
	for _, input := range inputs {
		elfOne := convertZone(input[0])
		elfTwo := convertZone(input[1])
		if compareZonesTwo(elfOne, elfTwo) || compareZonesTwo(elfTwo, elfOne) {
			phaseTwoResults += 1
		}
	}
	phaseTwoString := strconv.Itoa(phaseTwoResults)
	fmt.Println("Phase 2 = " + phaseTwoString)

}
