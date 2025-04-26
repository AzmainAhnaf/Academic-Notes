
Pointer is a variable that holds a memory address of another object (typically another variable)

```c
#include <stdio.h>

int main(){
	int data = 4269;
	int *ptr = &data;
	printf("%p\t%d\n", ptr, *ptr);
}
```
Explanation:

`int *` is the data type which is a pointer pointing to an integer variable `&data` refers to the memory address of the variable named `data`. while printing `%p` is the placeholder for memory address. While, `ptr` refers to the memory address `*ptr` is called dereferencing the pointer which is basically means show me the value under this specific memory address.