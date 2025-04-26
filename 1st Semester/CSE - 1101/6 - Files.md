
File Handling in C is the process in which we create, open, read, write and close operations on a file. C language provides different functions such as `fopoen()` `fwrite()` `fread()` `fseek()` `fprintf()` etc. to perform input, output, and many different C file operations in our program.

**Types of Files in C**

A file can be classified into two types based on the way the file stores the data. They are as follows:
- Text Files
- Binary Files


**File Pointer in C**

A file pointer is a reference to a particular position in the opened file. It is used in file handling to perform all file operations such as read, write, close, etc. We use the FILE macro to declare the file pointer variable. The FILE macro is defined inside `<stdio.h>` header file.
```c
FILE* pointer_name;
```


**Open a File in C**

For opening a file in C, the `fopen()` function is used with the filename or file path along with the required access modes.

Syntax of `fopen()`
```c
FILE* fopen(const char *file_name, const char *access_mode);
```
Parameter:
- `file_name`: name of the file when present in the same directory as the source file. Otherwise, full path.
- `access_mode`: Specifies for what operation the file being opened
Return Value:
- If the file is opened successfully, returns a file pointer to it.
- If the file is not opened, then returns NULL


**Access Mode**
- r: opening file for reading
- w: opening file for writing
- a: opening file for appending
Note: Returns NULL if unable to open


```c
#include <stdio.h>

int main(){
	FILE* fptr;

	// opening the file in read mode
	fptr = fopen("exam_in.txt", "r");

	// checking if the file is opened successfully
	if (fptr == NULL) {
		printf("The file is not found\n");
		return -1;
	}
	return 0;
}
```



**Create a File in C**

The `fopen()` function can not only open a file but also can create a file if it does not exist already. For that, we have to use modes that allow the creation of a file if not found such `"w"`.

```c
#include <stdio.h>

int main() {
	FILE* fptr;

	// creating file using fopen() access mode "w"
	fptr = fopen("file.txt", "w");

	// checking if the file is created
	if (fptr == NULL) {
		printf("The file is not opened");
		return -1;
	}
	else {
		printf("The file is created successfully");
	}

	return 0;
}
```


**Reading From a File**

The file read operations in C can be performed using functions `fscanf()` or `fgets()`. 

```c
FILE* fptr;
fptr = fopen("fileName.txt", "r");
fscanf(fptr, "%s %s %s %d", str1, str2, str3, &year);
char c = fgetc(fptr);
```


**Closing a File**

The `fclose()` function is used to close the file. After successful file operations, you must always close a file to remove it from the memory

```c
fclose(file_pointer)
```
Example:
```c
FILE* fptr;
fptr = fopen("file_name.txt", "w");
// -------- Some file operations -------
fclose(fptr);
```