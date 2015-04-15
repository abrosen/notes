/*
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define FILENAME "p022_names.txt"
#define MAX_NAMES 10000

int getNameScore(char *name) {
    int n = strlen(name);
    int i;
    int score = 0;
    for(i = 0 ; i < n; i++){
        score += (name[i] - 'A'  + 1);
    }
    return score;
}


int qcompare(const void *a, const void *b) 
{ 
    const char **x = (const char **)a;
    const char **y = (const char **)b;
    return strcmp(*x, *y);
} 

int main() {

    // FILE is a type
    // fp is a pointer to a file
    FILE  *fp;
    fp =  fopen(FILENAME, "r"); 
    int names_read = 0;


    int c;
    int i = 0;
    char *names[MAX_NAMES] = {0}; 
    names[names_read] =  (char *) malloc(sizeof(char) * 20);
    while( (c  = fgetc(fp))  != EOF) {
        if(c == '\"'){
            continue;
        } 
        
        if(c == ','){
            names[names_read][i] = '\0';
            i = 0;
            names_read++;
            names[names_read] = (char *) malloc(sizeof(char) * 20);
        }
        else{
            names[names_read][i] = c;
            i++;
        }
    }
    names[names_read][i] = '\0';
    printf("%s\n",names[names_read]);
    names_read++;

    qsort(names, names_read, sizeof(char *), qcompare);
    long score = 0; 
    for(i = 0; i < names_read; i++){ 
        printf("%s\n", names[i]);
        score += getNameScore(names[i]) * (i+1);
        free(names[i]);
    }

    printf("%ld\n", score);


    return 0;
}
