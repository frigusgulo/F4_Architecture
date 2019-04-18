#include <stdio.h>

int main(void){
	register int *ptr;
	int *L;
	int x,y,j;
	int k=0;
	int bigEndian = 0;
	ptr = &x;

	printf("Enter a (perferably large) number in decimal greater than zero \n");
	scanf("%d", &x);
	printf("You entered: %d\n",x);
	//Store in big endian
	for( int i = 32; i >=0; i--){
		 L = ptr+(k++); // USe for demonstrations
		 y = *(L);
		 j = x >> i;
		if( (j & y)!= y ){bigEndian = 1;}
	}
	
	if(bigEndian){printf("Your Computer is bigEndian\n");}
	else{printf("Your Computer is littleEndian\n");}
	
}