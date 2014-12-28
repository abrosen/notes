#include <stdio.h>
#include <math.h>
#define TARGET 10000

/*
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
*/


// sum of proper divisors of n, excluding n.
unsigned int aliquot_sum(unsigned int n) {
	unsigned int sum = 1, i = 2;
	for(i =2;  i <n/2 +1; i++) {
		if(n % i == 0) {
			sum += i;
		}
	}
	return sum;
}


int main() {
	int i;
	int aliquot[TARGET+1] = {0}; //init all to 0 
	int amicable_sum  = 0;
	
	for(i = 1; i< TARGET;i++){
		aliquot[i] = aliquot_sum(i);
	}
	
	for(i = 1; i<TARGET;i++){
		if(aliquot[i] < TARGET  && aliquot[aliquot[i]] == i  && aliquot[i] != i) {
			amicable_sum += i;
			printf("%d\t%d\n", i, aliquot_sum(i));
		}
	}
	printf("%d\n", amicable_sum);
}