package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func sum(array []int) int {
	result := 0
	for _, v := range array {
		result += v
	}
	return result
}

func getElfCalories(filePath string) [][]int {
	dat, err := os.ReadFile(filePath)
	if err != nil {
		panic(err)
	}
	calorieString := string(dat)
	calorieSlice := strings.Split(calorieString, "\n\n")
	calorieSlices := [][]int{}
	for _, v := range calorieSlice {
		elfCalories := strings.Split(v, "\n")
		elfCalorieInts := []int{}
		for _, v := range elfCalories {
			calorieInt, err := strconv.Atoi(v)
			if err != nil {
				panic(err)
			}
			elfCalorieInts = append(elfCalorieInts, calorieInt)
		}
		calorieSlices = append(calorieSlices, elfCalorieInts)
	}
	return calorieSlices
}

func main() {
	calorieSlices := getElfCalories("./inputs")
	totalElfCalories := []int{}
	for _, v := range calorieSlices {
		totalElfCalories = append(totalElfCalories, sum(v))
	}
	sort.Ints(totalElfCalories)

	sort.Sort(sort.Reverse(sort.IntSlice(totalElfCalories)))
	fmt.Print(totalElfCalories[0])
	fmt.Print("\n")
	topThreeElfSlice := totalElfCalories[:3]
	fmt.Print(sum(topThreeElfSlice))

}
