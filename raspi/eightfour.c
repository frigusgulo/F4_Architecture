#include <stdio.h>
#include <string.h>

char string[200];
char *ptr = string;

int main(void){
	printf("Enter a string\n");
	fgets(string,200,stdin);
	printf("You entered: %s\n",string);
	while( (*ptr) != '\n'){ptr++;}
	*ptr  = '\0';
	return 0;
}