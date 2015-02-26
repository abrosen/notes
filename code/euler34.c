#include <stdio.h>


int LIMIT  = 1000000;
int factorial(int);
int digit_factorial(int);

int main() {
    
    int i;
    int total = 0;
    for (i=3; i<LIMIT; i++) {
        if (i == digit_factorial(i)) {
            total += i;
        }

    }
    printf("%d\n",total);
    return 0;
}




int digit_factorial(int n) {
    int total = 0;
    
    while (n > 0) {
        int lowest_digit = n % 10;
        total += factorial(lowest_digit);
        n = n / 10;
    }
    return total;
}


int factorial(int n) {
    if (n ==0 || n==1) {
         return 1;
     }
    return n*factorial(n-1);
}
