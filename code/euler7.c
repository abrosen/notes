/*
Project Euler 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
*/

#include <stdio.h>
#include <math.h>


#define TARGET 10001


int is_prime(int num) {
	int i;
	for(i = 2;  i < num/2 +1; i++) {
		if( num % i  == 0 ) {
			return 0;
		}
	}
	return 1;
}



int main() {
	int i;
	int primes_found = 0;
	
	for(i=2; ; i++) {
		if( is_prime(i)) {
			primes_found++;
		}
		if(primes_found == 10001){
			break;
		}
	}
	printf("%d\n",i);
	
	return 0;
}

