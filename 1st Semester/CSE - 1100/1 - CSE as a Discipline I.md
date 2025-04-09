

# Bachelors vs Diploma

## Bachelors

A bachelor's degree is an undergraduate academic degree awarded by colleges and universities. It takes 3 to 4 years to complete study. Being a more comprehensive degree, a bachelor's degree focuses more on theoretical academic knowledge.

## Diploma

A diploma degree is an academic degree awarded by institute/polytechnic institute. It takes 1 to 2 years to complete study. A diploma degree focuses on making students ready for the job industry.


For example,
BSc in CSE will teach all the building blocks of computer science and computer engineering so that any software/hardware can be build from scratch.




# Computer Science vs Computer Engineering vs Software Engineering

## Computer Science Discipline

Computer science is a discipline that is the study of algorithmic processes and computational machines.
	Algorithmic Processes = Programming + Algorithms
	Computational Machines = Theoretical Computer Science

## Computer Engineering Discipline

Computer Engineering is a discipline of engineering that integrates several fields of computer science and electronic engineering required to develop computer hardware and software.

## Software Engineering Discipline

Software Engineering is a discipline that focuses on an engineering approach to software development. It includes courses like: Software Requirements  Analysis, Software Project Management, Design Patterns, Software Testing etc.



Roughly,
	Computer Science Discipline = Software/Programming Courses
	Computer Engineering Discipline = Hardware/Electrical Engineering Courses
	Software Engineering Discipline = Software Management Courses


## Theoretical Computer Science

Theoretical Computer Science is a subset of general computer science and mathematics that focuses on mathematical aspects of computer science.


## Curriculum Summary

BSc in Computer Science = 50% CS + 30% TCS + 15% CE + 5% SE
BSc in Computer Engineering = 40% CS + 5% TCS + 50% CE + 5% SE
BSc in Software Engineering = 30% CS + 5% TCS + 15% CE + 50% SE


# Map of CSE

![[Pasted image 20250204193250.png]]



# Theoretical Computer Science

Theoretical Computer Science (TCS) is a subset of general computer science and mathematics that focuses on mathematical aspects of computer science

![[Pasted image 20250204193514.png]]

There are two courses based on Theoretical Computer Science
1. Discrete Mathematics
2. Theory of Computation


## Discrete Mathematics

Discrete Mathematics is a branch of mathematics involving discrete elements that uses algebra and arithmetic. It is increasing being applied in the practical fields of mathematics and computer science.

Topics of Discrete Mathematics
1. Logic and Proof Techniques (Algorithms etc.)
2. Number Theory (Security, Cryptography etc.)
3. Relations (Database etc.)
4. Graph Theory (Networking, AI etc.)


Example of Proof Technique:

Suppose you are writing a program to add 1 to n number. You have checked that your program gives correct answer up to n = 100000000

Whether your program will give correct answers cannot be guaranteed until it is proved using proof techniques. This can be proved using technique called mathematical induction.


Example of Number Theory:

The RSA encryption algorithm which is commonly used in secure commerce web sites, is based on the fact that it is easy to take two (very large) prime numbers and multiply them. While it is extremely hard to do the opposite - meaning: take a very large number, give which it has only two prime factors, and find them.



## Theory of Computation

Theory of computation deals with the definitions and properties of mathematical models of computation. These models play a role in several applied areas of computer science.

![[Pasted image 20250204194244.png]]

Example of Turing Machine:

Turing Machine is the mathematical model of real-life computers. It basically deals with one question: What are the fundamental capabilities and limitations of computers?

All algorithms developed are based on Turing Machine. It means algorithms are not written with particular CPU like Intel, AMD etc. in mind.

It is not possible to create Turing machine in real-life as mathematical theory considers infinite memory which is not possible.

Turing machines are mathematically equivalent to each other. Modern CPUs like Intel, AMD, ARM are Turing complete which means they are mathematically equivalent to each other. It also means they are capable of running same algorithms.

It is mathematically proved that there is no mathematical/theoretical machine that is more computationally powerful (not considering efficiency of computation) than Turing machine.

It means it is possible to speed up real-life CPU but we can not create a CPU which can compute something that Turing machine cannot.

For example, Turing machine cannot solve "Halting problem". It also means real-life CPU cannot solve "Halting problem" no matter how powerful CPU you use.