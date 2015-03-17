/* The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million. 
*/


#include <stdio.h>
#define LIMIT 1000000 

int array[LIMIT]; 


// given positive int start, returns the len of the collatz senquence
int collatz_len(long start) {
	int len = 1;
	long  i = start;
	while (i > 1) {
		
		if(i < start) {
			array[start] = len + array[i]; 
			return  array[start];
		}
		
		
		
		if(i % 2 == 0) {  //if term is even, divide by two
			i = i/2;
		} 
		else {  // if odd, *3 +1
			i = 3*i + 1;
		}
		len++;
	}
	array[start] = len;
	return len;
}


int main() {
	long num;
	int largest_seq = -1;
	int largest_num = -1;
	array[1] = 1;
	array[2] = 2;

	
	
	for(num = 1; num < LIMIT; num++) {
		long len = collatz_len(num);
		if(len > largest_seq){
			largest_seq = len;
			largest_num = num;
		}
	}
	
	printf("%d \t %d", largest_seq, largest_num);
	
	return 0;
}
