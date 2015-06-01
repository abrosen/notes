package main

import "fmt"

var TARGET int = 600851475143

func largest_prime_factor(n int) int {
	largest_prime := -5
	if n%2 == 0 {
		largest_prime = 2
		n /= 2
	}
	for i := 3; n > 1; i += 2 {
		for n%i == 0 {
			largest_prime = i
			n = n / i
		}
	}
	return largest_prime
}

func main() {
	x := largest_prime_factor(TARGET)
	fmt.Println(x)
}
