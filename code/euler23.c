#include <stdio.h>
#include <stdbool.h>
#define LIMIT 28123

/*
 * 
 * A memory complacent solution to Euler 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
*/

int aliquot_sum( int n) {
	int sum = 1, i = 2;
	for(i = 2 ;  i < n/2 +1; i++) {
		if(n % i == 0) {
			sum += i;
		}
	}
	return sum;
}

int is_abundant(int n) {
	return aliquot_sum(n) > n;
}

main() {
	int i;
	int num_abundants = 0;  //number of abundant numbers below LIMIT 
	int abundants[LIMIT] = {0}; 
	// Find all abundant numbers below LIMIT
	for(i = 12; i<LIMIT;i++) {
		if(is_abundant(i)) {
			abundants[num_abundants] = i;
			num_abundants++;
		}
	}
	
	// determine which numbers
	// simple and wastes memory 
	bool is_sum_of_abundants[LIMIT+1] = {0};
	int j;
	int check;
	for(i = 0; i < num_abundants; i++) {
		for( j = i; j <num_abundants; j++) {
			check =  abundants[i] +abundants[j];
			if( check <= LIMIT) {
				is_sum_of_abundants[check] = true;
			}
		}
	}
	
	// and now sum
	int sum = 0;
	for(i = 0; i <=LIMIT;i++) {
		if(is_sum_of_abundants[i] == false) {
			sum+=i;
		}
	}
	
	printf("%d\n",sum);
}
