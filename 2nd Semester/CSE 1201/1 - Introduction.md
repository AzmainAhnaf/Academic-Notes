
# Basic Terminology

**Data:** It is simply a value or set of values

**Data Item:** Refers to single unit of value. Data items that cannot be divided into sub items are called **Elementary Items**. otherwise, it is called **Group Data Items**.

**Entity:** An entity is something that has certain attributes or properties which may be assigned some values. The values themselves may be either numeric or non-numeric

![[Pasted image 20250616231827.png]]


**Information:** Refers to meaningful or processed data. Example: 21 is simply a data but if it is an age then it is an information.

**Field:** An attribute of an entity
**Record:** The collection of field values of a given entity
**File:** The collection of records of the entities in a given entity set
**Database:** Several file makes a database

**Key:** A unique value that can be used to distinguish one record from the others.


# Basics of Data Structure

**What is Data Structure?**
A data structure is a specialized format for organizing, processing, retrieving and storing data.

**Classification of DS**
![[Pasted image 20250616225325.png]]

**Linear Data Structure:** A linear data structure traverses the data elements sequentially, in which one data element can directly be reached. Example: Arrays, Linked Lists.

**Non-Linear Data Structure:** Every [[1 - Introduction#Basic Terminology|data item]] is attached to several other data items in a way that is specific for reflecting relationships. The data items are not arranged in a sequential structure. Example: Trees, Graphs.



# Data Structure Operation

**Four Basic Operations**

1. **Traversing:** Accessing each record exactly once so that certain items in the record may be processed.
2. **Searching:** Finding the location of the record(s) with a given key value/conditions.
3. **Insertion:** Adding a new record to the structure
4. **Deletion:** Removing a record from the structure


**Two Special Operations**

1. **Sorting:** Arranging the records in some logical order.
2. **Merging:** Combining records from different files.



# Abstract Data Type

**Definition:** Abstract Data Type (ADT) is a mathematical model with a collection of operations defined on that model

**Model** of a data type contains -
- Properties of the data
- Operations that can be performed on that data

Example: Complex Number, Set


# Algorithm & Flow Chart


## Flow Chart


**Flowchart** is a pictorial presentation of an algorithm

**Important Diagram for Flowchart**

![[Pasted image 20250616231017.png]]
![[Pasted image 20250616231027.png]]
![[Pasted image 20250616231036.png]]
![[Pasted image 20250616231046.png]]

**Examples of Flow Chart**

![[Pasted image 20250616231130.png]]

![[Pasted image 20250616231140.png]]


## Algorithm

**Definition:** A well-defined list of steps for solving a particular problem.

Two major measure of the efficiency of an algorithm are:
- Time and
- Space

**Complexity:** The complexity of an algorithm is the function which gives the running time and/or space in terms of input size.

**Time-Space Trade-Off in Algorithms**
A tradeoff is a situation where one thing increases and another thing decreases. It is a way to solve problem in-
- Either in less time and by using more space, or
- In very little space by spending a long amount of time


### Algorithm Notation

**Problem:** An array DATA of numerical values is in memory. We want to find the location LOC and the value MAX of the largest element of DATA. Given no other information about DATA, one way to solve the problem is as follows:

**Solution:** Initially begin with LOC = 1 and MAX = DATA\[1]. Then compare MAX with each successive element DATA\[K] of DATA. If DATA\[K] exceeds MAX, then update LOC and MAX so that LOC = K and MAX = DATA\[K]. The final values appearing in LOC and MAX give the location and value of the largest element of DATA

The solution can be drawn in a flow chart like this
![[Pasted image 20250616234326.png]]

The solution should be proposed in an algorithm like this
![[Pasted image 20250616234245.png]]


**Comments**
Each step may contain a comment in brackets which indicates the main purpose of the step. The comment will usually appear at the beginning or end of the step.

**Variable Names**
Variable names will use capital letters, as in MAX and DATA. Single-letter names of variables used as counters or subscripts will also be capitalized in the algorithms (K and N, for example). Even though lowercase may be used for these same variables in the accompanying mathematical description and analysis.

**Assignment Statement**
Assignment statements will use the dots-equal notation :=

**Input and Output**
Data may be input and assigned to variables by means of a **Read** statement. With the following form
```
Read: Variable name/s
```
Similarly, messages, placed in quotation marks, and data in variables may be output by means of a write or print statement with the following form:
```
Write: Message and/or variable names
```


### Types of Complexities

1. Best Case: the minimum value of $c(n)$ for any possible input. For linear search, best case $c(n) = 1$. This is also called the Big $\Omega$ notation.
2. Worst Case: The maximum value of $c(n)$ for any possible input. For linear search, worst case $c(n) = n$. This is also called the Big O notation.
3. Average Case: the average value of $c(n)$ for any possible input. For linear search, average case $c(n) = \frac{n + 1}2$. This is also called the Big $\theta$ notation.


