
**API**: Application Programming Interface
- Also known as a "library"
- Contains predefined Java code that we can use to develop Java programs

**JDK**: Java Development Kit
- Set of programs that enable us to develop our programs
- Contains JRE(Java Runtime Environment) that is used to run our programs
- JVM executes our java programs on different machines

**IDE**: Integrated Development Environment
A program that allows us to
- Write | source code
- Compile | machine code
- Debug | tools to find errors
- Build | files that can be executed by JVM
- Run | execute our program

# Java: Basic Concepts

- Classes & Objects
- Methods
- Naming Conventions
- Java Program Structure
- Packages

**Java: Class Structure**
```java
class class_name {
	// code block
}
```

**Java: Methods**
```java
return_type method_name(parameters){
	// code block
}
```
Every method is written inside a Class. A class is a container of methods

**Java: Naming Convention**
1. Pascal case convention: ThisISAName
2. Camel case convention: thisIsAName
3. Snake case convention: this_is_a_name


**Java: Programming Structure**
```java
public class Main {

	public static void main(String[] args) {
	
	}

}
```

**Java: Package**
Java package is a container for classes
![[Pasted image 20250806003029.png]]

**Java: println() method**
```java
System.out.println("hello");
System.out.println("123");
System.out.println("");
System.out.println("456");
```

**Java: System.out**
- *out* is can object of the "PrintStream" class.
- out has the `print()` and `println()` methods
- `out` refers to the standard output device. (Screen)
- `System` is a Class


![[Pasted image 20250806003527.png]]

**Java Virtual Machine**, or JVM, loads, verified and executes Java bytecode. It is known as the interpreter or the core of Java programming language because it executes Java programming.

# Java: Program

**Program 1: print a message/text**

```java
public class First {
	public static void main(String[] args){
		System.out.print("Welcome to Java World")
	}
}
```

Output:
```
Welcome to Java World
```

**Program 2: print a message/text**

```java
package CSE1203;

public class Second {
	public static void main(String[] args){
		System.out.print("Talk less listen more");
	}
}
```
A class Second is created under the package CSE1203

**Program 2(ex): call main() of second**
```java
package CSE1203;
public class First {
	public static void main(String[] args) {
		System.out.println("Welcome to Java World");
		Second.main(null);
	}
}
```

Output:
```
Welcome to Java World
Talk less listen more
```
Notes: in the First class just write the class name if you want to call other classes method

**Program 2(ex): change second class**
```java
package CSE1203;
public class Second {
	public static void main(String[] args){
		System.out.println("Talk less listen more");
		Display();
	}
	public static void Display(){
		System.out.println("Honest is the best policy");
	}
}
```


**Access Modifier: 4 types**
1. public: access from everywhere
2. private: access only inside the class
3. protected: access only inside the class and child class
4. default: access from everywhere

**Non-Access Modifier:** static
We can access fields/methods using the class name


**Program 3**: private method
```java
package CSE1203;
public class Second {
	public static void main(String[] args){
		System.out.println("Talke less listen more");
		Display();
	}
	private static void Display(){
		System.out.println("Honesty is the best policy");
	}
}
```

Output:
```
Talk less listen more
Honesty is the best policy
```
Note: Now Display() can't be called outside the class