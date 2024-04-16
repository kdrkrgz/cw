package main

import (
	"fmt"
	"strconv"
)

func main() {
	for p := range genFib {
		fmt.Println(p)
		if p > 1000 {
			break
		}
	}
}

func case1() int {
	a := "123"
	i, _ := strconv.Atoi(a)
	return i
}

func RepeatStr(repetitions int, value string) string {
	var res string
	for i := 0; i < repetitions; i++ {
		res += value
	}
	return res
}

func century(year int) int {
	if year%100 == 0 {
		return year / 100
	}
	return year/100 + 1
}

func genFib(yield func(int) bool) bool {
	a, b := 1, 1
	for {
		if !yield(a) {
			return false
		}
		a, b = b, a+b
	}
	return true
}
