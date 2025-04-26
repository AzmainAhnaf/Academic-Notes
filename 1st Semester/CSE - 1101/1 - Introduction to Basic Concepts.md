

# Basic Structure of a C Program

```c
#include <stdio.h>

int main {
	// Write Instructions Here
	return 0;
}
```


# Output Statement

Pre-defined Function: `printf()`

Example:
```c
#include <stdio.h>
int main(){
	printf("Why so Serious?");
	return 0;
}
```
Output:
```
Why so Serious?
```

Explanation:
Here the collections of characters inside the double quotation mark inside printf() function is called string, and the semicolon refers to the end of a statement.


# Escape Sequence

For New line -> `\n`
For Horizontal Tab -> `\t`

Example:
```c
#include <stdio.h>
int main(){
	printf("Why\nSo\nSerious\n!!!");
	return 0;
}
```
Output:
```
Why
So
Serious
!!!
```

Explanation:
`\n` is creating a new line on the terminal before printing anything else that is after the `\n`.


# Variable

- Named location  in memory
- Can hold a value
- The value can be modified

**Variable is a named location in memory which can hold and modify a value stored in the memory**

**Variable Declaration**
```
Data_Type Variable_Name
```
Data_Type can be `char, int, float, double, long`


# Basic Data Types


| Data Type         | Description                            | Size    | Range                                                              |
| ----------------- | -------------------------------------- | ------- | ------------------------------------------------------------------ |
| char              | Character                              | 1 byte  | signed: -128 to 127<br>unsigned: 0 to 255                          |
| short int (short) | Short Integer                          | 2 bytes | signed: -32768 to 32767<br>unsigned: 0 to 65535                    |
| int               | Integer                                | 4 bytes | signed: $-2^{31}$ to $2^{31} - 1$<br>unsigned: $0$ to $2^{32} - 1$ |
| long int (long)   | Long Integer                           | 8 bytes | signed: $-2^{63}$ to $2^{63} - 1$<br>unsigned: $0$ to $2^{64} - 1$ |
| float             | Floating Point Number                  | 4 bytes |                                                                    |
| double            | Double Precision Floating Point Number | 8 bytes |                                                                    |


# Naming Convention

**Variable Name:**

- First character should be a letter or an underscore
- Following characters can be letters, digits or underscores.
- Special character or space is not allowed (e.g., !, ?, @, +)


# Input Statement

Pre-defined Function: `scanf()`

Writing format:
- For `printf()`: `printf("%d", num);
- For `scanf()`: `scanf("%d", &num);`


Example: A program to find the summation of two number
```c
#include <stdio.h>
int main(){
	int num1, num2; // Declaring Variable

	// taking input
	scanf("%d %d", &num1, &num2);

	// Giving output
	printf("Sum = %d\n", num1 + num);
	return 0;
}
```
Input
```
244139
303
```
Output
```
Sum = 2441442
```



# Operators

- Arithmetic Operators
	- `+ - * / %`
	- Both operands of `%` should be int
- Relational Operators
	- Greater Than: `>`
	- Greater Than or Equal to: `>=`
	- Less Than: `<`
	- Less Than or Equal to: `<=`
	- Equal to: `==`
	- Not Equal to: `!=`
	- Value of Relational Expression is either 0 or 1
- Logical Operators:
	- AND: `&&`
	- OR: `||`
	- NOT: `!`
- Assignment Operators:
	- `=`
	- Compound Assignment Operators
		- `+=` `-=` `*=` `/=` `%=`
		- `Sum += Num;` -> `Sum = Sum + Num;`
- Increment & Decrement Operators
	- `++` `--`
	- `++X;` -> `X = X + 1`


# Type Casting

Type Casting allow user to change a data type of a variable

```C
float result:
int var1, var2;

// returns an int as int / int = int
result = var1 / var2 

// returns a float as float / int = float
result = (float)var1 / var2 
```
