#include <stdio.h>

int even_fib(int limit);
int LIMIT = 4000000;
	


int main() {
	int sum = even_fib(LIMIT);
	printf("%d",sum);
	return(0);

}

int even_fib(int limit) {
	int sum = 0;
	int n_minus_2 = 1;
	int n_minus_1 = 1;
	int n;	
	
	while(n_minus_1<limit) {
		// calculate n
		n = n_minus_2 + n_minus_1;

		// add even n to sum
		if(n%2 ==0) { 
			sum +=n; 
		}

		// update for next iteration
		n_minus_2 = n_minus_1;
		n_minus_1 = n;

	}

	return sum;
}
