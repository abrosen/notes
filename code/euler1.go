package main

import "fmt"

func multipleSum(x int, y int, limit int)  int {
	sum := 0
	for i := 0;  i < limit; i++ {
		if i % x == 0 || i % y == 0 {
			sum += i
		}
	}
	return sum
}

func main() {
	sum := multipleSum(3,5,1000)
	fmt.Println(sum)
}
