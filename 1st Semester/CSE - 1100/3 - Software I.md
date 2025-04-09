

# Programming Language

- A programming language is a vocabulary and set of grammatical rules for instructing a computer or computing device to perform specific tasks
- Coding schemes used to write both systems and application software
- A programming language is an artificial language that can be used to control the behavior of a machine, particularly a computer.
- Programming languages, like human languages, are defined through the use of **syntactic** and **semantic** rules, to determine structure and meaning respectively.
- In computer science, the syntax of a computer language is the set of rules that defines the combinations of symbols that are considered to be correctly structured statements or expressions in that language
- The C basic syntax consists of header files, main function, and program code
- In computer science, the term **semantics** refers to the meaning of language constructs, as opposed to their form

**Semantic Errors:**
Errors recognized by semantic analyzer are as follows:
- Type mismatch
- Undeclared variables
- Reserved identifier misuse



# Non-computational Languages

- Non-computational languages, such as markup languages like HTML or formal grammars are usually not considered programming languages
- Often a programming language is embedded in the non-computational language


# Computer Languages

Computer languages can be broadly separated into three categories

- Low Level Language (Machine Language)
	- Use 1's and 0's to create instructions
	- Example: Binary Language
- Middle Level Language (Assembly Language)
	- Use mnemonics to create instructions
	- Example: Assembly Language
- High Level Language
	- Similar to human language
	- Example: COBOL, FORTRAN, BASIC C, C++, JAVA


## Machine Language

- 1st generation programming language
- Machine languages are the only languages understood by computers
- Considered a low-level language because it involved basic coding using the binary symbols 1 and 0

![[Pasted image 20250204213044.png|300]]

- While easily understood by computers, machine languages are almost impossible for humans to use because they consist entirely of numbers
- For example, an x86/IA-32 processor can execute the following binary instruction as expressed in machine language:
	Binary: 10110000 011000001 (Hexadecimal: 0x061)
- It does not need any translator program

### Advantage
- The only advantage is that program of machine language run very fast because no translation program is required for the CPU

### Disadvantages
- It is very difficult to program in machine language. The programmer has to know details of hardware to write program
- The programmer has to remember a lot of codes to write a program which results in program errors most of the time.
- It is difficult to debug the program



## Assembly Language

- 2nd generation language
- An assembly language is a low-level language for programming computers
- It implements a symbolic representation of the numeric machine codes and other constants needed to program a particular CPU architecture
- Replaced binary digits with mnemonics (e.g., "ADD") programmer could more easily understand


### Advantages
- Assembly language is easier to understand and saves a lot of time and effort of the programmer
- It is easier to correct errors and modify program instructions
- Assembly Language had the same efficiency of execution as the machine level language. Because this is one-to-one translator between assembly language program and its corresponding machine language program

### Disadvantages
- One of the major disadvantages is that assembly language is machine dependent. A program written for one computer might not run in other computers with different hardware configuration



## High Level Language

- High-level languages are relatively easy to learn because the instructions bear a close resemblance to everyday language, and because the programmer does not require a detailed knowledge of the internal workings of the computer.
- Each instruction in a high-level language is equivalent to several machine-code instructions, there is is more compact than equivalent low-level programs.
- High-level languages are used to solve problems and are often describes as problem-oriented languages.
- Example of HLL:
	- BASIC was designed to be easily learnt by first-time programmers
	- COBOL is used to write programs solving business problems
	- FORTRAN is used for programs solving scientific and mathematical problems.
	- With the increasing popularity of windows-based systems the next generation of programming languages was designed to facilitate the development of GUI interfaces
		- For example, Visual Basic wraps the BASIC language in a graphical programming environment
	- Support for object-oriented programming has also become more common, for example in C++ and JAVA

### Advantage
- Higher level languages have a major advantage over machine and assembly languages that higher level languages are easy to learn and use. It is because that they are similar to the languages used by us in our day to day life.



# Assembler

- Is used to translate assembly language statements into the target computer's machine code
- The assembler performs a more or less isomorphic translation (a one-to-one mapping) from mnemonic statements into machine instructions and data
- Fundamental functions
	- translating mnemonic operation codes to their machine language equivalents
	- assigning machine addresses to symbolic labels

![[Pasted image 20250204215904.png]]


# Compiler

- A compiler is a program that reads a program in one language - the source language and translates into an equivalent program in another language - the target language.
- A compiler is a special program that processes statements written in a particular programming language called as source code and converts them into machine language or "machine code" that a computer's processor uses.
- Compiler translates high level language programs directly into machine language program. This process is called compilation

![[Pasted image 20250204220128.png]]


# Linker and Loader

![[Pasted image 20250204220155.png]]

## Linker

- A linker or link editor is a program that takes one or more objects generated by compilers and assembles them into a single executable program
- Linkers can take objects from a collection called a library. The objects are program modules containing machine code and information for the linker
- The linker takes care of arranging the objects in a program's address space


## Loader

- A loader is the part of any operating system that is responsible for loading programs into memory, preparing them for execution and then executing them
- To run an executable file, the loader must copy all the instructions into and direct the CPU to begin execution with the first instruction
- As the program executes, it takes input data from source(s) and sends results to output devices.
- In Unix, the loader is the handler for they system call execve().



# Interpreter

- An interpreter is a computer program that translates and executes instruction written in a computer programming language line-by-line, unit by unit etc.
- An interpreter needs to be able to analyze, or parse, instructions written in the source language
- Example: LISP systems
- An interpreter translates high-level instructions into an intermediate form, which it then executes
- Compiled programs generally run faster than interpreted programs
- The advantage of an interpreter, however, is that it does not need to go through the compilation stage during which machine instructions are generated
- This process can be time-consuming if the program is long


# Interpreter vs Compiler


| Interpreter                                                                                                     | Compiler                                                                                                        |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Translates program one statement at a time                                                                      | Scans the entire program and translates it as a whole into machine code                                         |
| It takes less amount of time to analyze the source code but the overall execution time is slower                | It takes large amount of time to analyze the source code but the overall execution time is comparatively faster |
| No intermediate object code is generated, hence are memory efficient                                            | Generates intermediate object code which further requires linking, hence requires more memory                   |
| Continues translating the program until the first error is met, in which case it stops. Hence debugging is easy | It generates the error message only after scanning the whole program. Hence debugging is comparatively hard     |
| Programming languages like Python, Ruby, Basic use interpreters                                                 | Programming language like C, C++, Java use compilers                                                            |


# Flow of execution

![[Pasted image 20250204221042.png]]



# Object Oriented Programming

- OOP is a computer programming model that organized software design around data, or objects, rather than functions and logic
- An object can be defined as data field that has unique attributes and behavior.
- Additional benefits of OOP include code reusability, scalability and efficiency
- The first step in OOP is to collect all of the objects a programmer wants to manipulate and identify how they relate to each other.
- Class: A class describes the contents of the objects that belongs to it: it describes an aggregate of data fields (called instance variables), and defines the operations (called methods).
- Object: An object is an element (or instance) of a class; objects have the behaviors of their class. The object is the actual component of programs, while the class specifies how instances are created and how they behave.
- Method: A method is an action which an object is able to perform

![[Pasted image 20250204221641.png]]

Object-oriented programming languages
- While **Simula** is credited as the first object-oriented programming language, the most popular OOP languages are:
- Java
- Javascript
- Python
- C++
- Visual Basic.NET
- Ruby
- PHP


#  Data Structures

- A data structure is a particular way of organizing data in a computer so that it can be used effectively
- For example, we can store a list of items having the same data-type using the *array* data structure.

![[Pasted image 20250204221919.png]]
![[Pasted image 20250204221928.png]]

- Topics
	- Array
	- Linked List
	- Stack
	- Queue
	- Binary Tree
	- Binary Search Tree
	- Heap
	- Hashing
	- Graph
	- Matrix
	- Advanced Data Structure


# Algorithms

- In mathematics and computer science, an algorithm is a finite sequence of well-defined, computer-implementable instructions, typically to solve a class of problems or to perform a computation
- Algorithms are always unambiguous and are used as specifications for performing calculations, data processing, automated reasoning, and other tasks.

Typical steps in the development of algorithms
- Problem definition
- Development of a model
- Specification of the algorithm
- Designing an algorithm
- Checking the correctness of the algorithm
- Analysis of algorithm
- Implementation of algorithm
- Program testing
- Documentation preparation

Topics
- Analysis of Algorithms
- Searching and Sorting
- Greedy Algorithms
- Dynamic Programming
- Patter Searching
- Other String Algorithms
- Backtracking
- Divide and Conquer
- Geometric Algorithms
- Mathematical Algorithms
- Bit Algorithms
- Graph Algorithms
- Randomized Algorithms
- Branch and Bound
- Quizzes on Algorithms

