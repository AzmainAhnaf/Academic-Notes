
# Structure

Structure is a collection of variables (can be different types) referenced under one name

**Purpose:** Keeping related information together

**Structure Declaration**
```c
struct Nayok {
	char Original_Name[30]; // 30 bytes
	double Height; // 8 bytes
	int No_of_Films; // 4 bytes
	int No_of_Awards; // 4 bytes
};
struct Nayok UK, Razzak, RK; // 46 bytes
```
**Accessing Structure Members** (Continuation of Previous Code)
```c
UK.No_of_Films = 203;
gets(UK.Original_Name);
```

We can also create array for a specific structure



# Union

Union is an user-defined data type that can contain elements of the different data types just like structure. But unlike structures, all the members in the C union are stored in the same memory location.

Union is defined as similar way as structure. The only difference is that the union creates only one memory space. The size of the memory computed by the maximum size of its data members.
```c
Union Student {
	int id;
	char name[10];
	float gpa;
} student;
// The Union creates 10 bytes of space
```
Union variable saves the latest assignment of its members
```c
student.id = 100;
student.gpa = 3.75;
printf("%d %f\n", student.id, student.gpa);
```
Output:
```
<garbage value> 3.75
```



# Enumeration

An enumeration (or enum) is an user defined data type that contains a set of named integer constants. It is used to assign meaningful names to integer values, which makes a program easy to read and maintain

```c
enum enum_name {
	n1, n2, n3, ...
};
```
Explanation:
Here, n1, n2, n3, . . .  are names assigned to an integer value. By default, first name **n1** is assigned 0, **n2** is assigned 1 and the subsequent ones are incremented by 1;

```c
#include <stdio.h>

// Defining enum
enum direction {
	EAST, NORTH, WEST, SOUTH
};

int main() {

	// creating enum variable
	enum direction dir = NORTH;
	printf("$d\n", dir);

	// This is valid too
	dir = 3;
	printf("%d\n", dir);
	return 0;
}
```
Output
```
1
3
```

