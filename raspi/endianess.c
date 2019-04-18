#include <stdio.h>

int main(void){
	unsigned char *ptr;
	int x,i;
	int bigEndian = 0;
	ptr = (unsigned char *)&x;

	printf("Enter a (perferably large) number in decimal greater than zero \n");
	scanf("%d", &x);
	printf("You entered: %d\n",x);
	//Store in big endian
	for (i = 0; i < 4; i++)
    		printf("   %p: %02x\n", ptr + i, *(ptr + i));

  	bigEndian = (*ptr == (unsigned char)(0xff & (x >> 24))) &&
            (*(ptr + 1) == (unsigned char)(0xff & (x >> 16))) &&
            (*(ptr + 2) == (unsigned char)(0xff & (x >> 8))) &&
            (*(ptr + 3) == (unsigned char)(0xff & x));
	
	if(bigEndian){printf("Your Computer is bigEndian\n");}
	else{printf("Your Computer is littleEndian\n");}
	
}
