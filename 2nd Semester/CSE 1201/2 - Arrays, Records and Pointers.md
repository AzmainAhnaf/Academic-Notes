
# Linear Arrays

A linear array is a list of a finite number of homogeneous data elements (i.e., data elements of the same type).


## Traversing Linear Arrays

**Algorithm:** (Traversing a Linear Array) Here LA is a linear array with lower bound LB and upper bound UB. This algorithm traverses LA applying on operation PROCESS to each element LA

1. \[Initialize counter] Set $K := LB$ 
2. Repeat Steps 3 and 4 while $K \le UB$.
3.     \[Visit element] Apply PROCESS to $LA[k]$
4.     \[Increase counter] Set $K := K + 1$
	\[End of Step 2 loop]
5. Exit

**Flow Chart:**
![[Pasted image 20250617001052.png]]



## Inserting into A Linear Array

**Algorithm:**
$INSERT(LA, N, K, ITEM)$
Here $LA$ is a linear array with $N$ elements and $K$ is a positive integers such that $K \le N$. This algorithm inserts an element $ITEM$ into the $K$th position in $LA$.

1. \[Initialize counter] SET $J := N$
2. Repeat steps 3 and 4 while $J \ge K$
3.         \[Move $J$th element downward] Set $LA[J + 1] := LA[J]$
4.         \[Decrease counter] Set $J := J - 1$
	\[End of Step 2 loop]
5. \[Insert element] Set $LA[K] := ITEM
6. \[Reset N] Set $N := N + 1$
7. Exit

**Flow Chart:**
![[Pasted image 20250617001845.png]]


## Deletion from a Linear Array

**Algorithm:**
$DELETE(LA, N, K, ITEM)$
Here $LA$ is a linear array with $N$ elements and $K$ is a positive integer such that $K \le N$. This algorithm deletes the $K$th element from $LA$.

1. Set $ITEM := LA[K]$
2. Repeat for $J = K$ to $N - 1$:  Set $LA[J] := LA[J + 1]$
	\[End of loop]
3. Set $N := N - 1$
4. Exit

**Flow Chart:**
![[Pasted image 20250617002244.png]]



## Sorting: Bubble Sort

**Algorithm**:
$BUBBLE(DATA, N)$
Here $DATA$ is an array with $N$ elements. This algorithm sorts the elements in $DATA$.

1. Repeat Steps 2 and 3 for $K = 1$ to $N - 1$
	2. Set $PTR := 1$
	3. Repeat while $PTR \le N - K$:
		(a) If $DATA[PTR] > DATA[PTR + 1]$, then: Interchange $DATA[PTR]$ and $DATA[PTR + 1]$
		(b) Set $PTR := PTR + 1$
		\[End of inner loop]
	 \[End of Step 1 outer loop]
	4. Exit

