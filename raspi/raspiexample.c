#include <stdio.h>
#include <stdlib.h>

typedef struct resizingArray
{
	int size;
	int capacity;
	int* data;
} Array;

void Array_init(Array* Arr, int capacity){
	Arr->data = malloc(capacity*sizeof(int));
	Arr->size = 0;
	Arr->capacity = capacity;
}

void resize(Array* Arr){

	if(Arr->size == Arr->capacity){
	Arr->capacity = 2*(Arr->capacity);
	Arr->data = (int*)realloc(Arr->data,2*Arr->size*sizeof(int));
	}
	else if(Arr->size < .25*(Arr->capacity)){
	Arr->capacity = .25*(Arr->capacity);
	Arr->data = (int*)realloc(Arr->data,.25*Arr->size*sizeof(int));
	}
	
}

void push(Array* Arr,int add){
	*(Arr->data + Arr->size) = add;
	Arr->size++;
	printf("Push: %d\n",add);
	resize(Arr);
}

void pop(Array* Arr){
	Arr->size--;
	printf("Pop\n");
	resize(Arr);
}
void peek(Array* Arr){
	printf("Peek: \n");
	for(int i = 0; i < Arr->size; i++){ printf("%d\n",*(Arr->data + i));}
}


int main(){
	register int* ptr;
	Array resize_Array;
	Array_init(&resize_Array,5);
	printf("Resizing Array initialize. Enter an integer to add it, -1 to remove the last element within the array,-2 to view the elements, and -3 to Quit.\n" );
	int temp;
	for(;;){
		scanf("%d",&temp);
		if(temp == -3){break;}
		else if(temp == -1){
			if(resize_Array.size < 1){printf("ERROR: EMPTY ARRAY");}
			else{
				pop(&resize_Array);
				resize(&resize_Array);
			}
		}
		else if(temp >= 0){
			push(&resize_Array,temp);
			resize(&resize_Array);
			ptr = &resize_Array.data[resize_Array.size-1];
		}
		else if(temp == -2){
			peek(&resize_Array);
		}
		else{
			printf("Enter int greater than -3\n");
		}

	}





	return 0;
}