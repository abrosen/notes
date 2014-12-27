#include <stdio.h>
#define TARGET 200
int coins[] = {1,2,5,10,20,50,100,200};




int main() {
    int ways[TARGET + 1] = {0};
    int numCoins = sizeof(coins)/sizeof(ways[0]);
    int i;
    int j;
    ways[0] = 1;
    
    
    printf("%d\n", numCoins);    
    
    for(i = 0;i<numCoins;i++){
        for(j = coins[i] ; j < TARGET+1; j++) {
            ways[j]+= ways[j - coins[i]];
        }
        
        printf("COIN %d:\t\t[", coins[i]);
        for(j = coins[i] ; j < TARGET+1; j++){
            printf("%d, ", ways[j]);
        }
        printf("]\n");
    }
    
    
    printf("%d\n", ways[TARGET]);    
    return 0;
}
