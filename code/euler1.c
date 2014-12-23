#include <stdio.h>

int main(int argc, char *argv[]) {
    if(argc != 4) {
        fprintf(stderr,"No no no... %d \n", argc);
        return(-1);
    }
    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    int limit = atoi(argv[3]);
    
    
    int i = 0;
    int sum = 0;
    for(i = 0; i<limit;i++) {
        if(i % a == 0 || i % b == 0 ){
            sum +=i;
        }
    }
    
    printf("%d\n",sum);
    return(0);
}
