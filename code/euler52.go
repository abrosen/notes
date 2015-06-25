package main

//import "math"
//import "fmt"

func isPermutation(a int, b int) bool {
	var aDigits [10]int
	var bDigits [10]int
	for i := a; i > 0; i /= 10 {
		aDigits[i%10]++
	}
	for i := b; i > 0; i /= 10 {
		bDigits[i%10]++
	}
	for i := 0; i < 10; i++ {
		if aDigits[i] != bDigits[i] {
			return false
		}
	}

	return true
}

func doComparisons(a int) bool {
	for i := 2; i <= 6; i++ {
		if !isPermutation(a, a*i) {
			return false
		}
	}
	return true
}

func main() {
	for i := 100000; i < 3000000; i++ {
		if doComparisons(i) {
			println(i)
			break
		}
	}

}
