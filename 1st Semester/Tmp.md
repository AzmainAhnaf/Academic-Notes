
Help Ahnaf Get Zero

Ahnaf is really fond of zeroes (not really, he actually is a **below average** student). As a result, he was not fond of his CT \textit{marks} as most of the prefix sum of his CT marks were not equal to zero. So he asked Pranshu for help. Being the cunning (and proud) CR of section B, Pranshu breached the database where CT marks were stored and gave access to Ahnaf. Being dumb, Ahnaf handed over the CT marks to you and asked you to help him.

Note: Ahnaf might get negative marks too!!!

Now you are given the marks of Ahnaf's CTs in an array $a_1, a_2, \ldots, a_n$ of length $n$. Let the prefix sum of the marks be $v_1, v_2, \ldots, v_n$ where $v_i$ = $v_1 + v_2 + \ldots + v_i$  for every index $i$ ($1 \le i \le n$ ). Ahnaf gave you the task of changing the mark of the CTs in such a way that you could maximize the number of zeros in the prefix sums $v_1, v_2, \ldots, v_n$ 

You can perform the following operation multiple times:

\begin{itemize}
\item Select an index of the mark such that the mark is zero. Formally, select an index $i$ ($1 \le i \le n$) such that $a_i = 0$;
\item Replace the mark $a_i$ with any mark of your choice (you can leave it zero as well)
\end{itemize}

Now, Ahnaf wants to know what is the maximum possible number of zeroes you can achieve from the array $a$ performing a sequence of above-mentioned operation.

\InputFile
Each test contains multiple test cases. The first line contains a single integer $t$ ($1 \le t \le 10^4$)~--- the number of test cases.

The first line of each test case contains one integer $n$ ($1 \le n \le 2 \cdot 10^5$)~--- the length of the array $a$.

The second line of each test case contains $n$ integers $a_1,a_2,\ldots,a_n$ ($-10^9 \le a_i \le 10^9$)~--- array $a$.

It is guaranteed that the sum of $n$ over all test cases does not exceed $2 \cdot 10^5$.

\OutputFile
For each test case, print the maximum number of zeroes you can achieve from the array $a$

\Example

\Note
In the first test case, it is optimal to change the value of $a_2$ to $-2$ in one operation.

The resulting array $a$ will be $[2,-2,1,-1,0]$, where the count of zero is 3

\begin{itemize}
\item $a_1+a_2=2-2=0$;
\item $a_1+a_2+a_3+a_4=2-2+1-1=0$;
\item $a_1+a_2+a_3+a_4+a_5=2-2+1-1+0=0$.
\end{itemize}

In the second test case, it is optimal to change the value of $a_3$ to $-2\,000\,000\,000$, giving us the count of zero of $1$.

In the third test case, it is not necessary to perform any operations.



# Pranshu and his Obsession with RU

One Wednesday afternoon, after finishing classes, Pranshu, Ahnaf and Aditya were hanging out at the "Low CG chattor". Pranshu being Pranshu, screamed, "Chol mama RU theke ghure asi." And Aditya, being Aditya, said, "Na re mama, basai jeye ghumaabo." Ahnaf, being Ahnaf, stayed silent. Aditya gave the excuse that his leg was hurting and he did not want to go to RU (Rajshahi University) as he might have to walk a lot (that's not true; he actually wanted to sleep). To prove Aditya wrong, Pranshu wanted to write a program that calculates the expected value of the distance they will walk. But Ahnaf and Pranshu both sucked at calculating expected value. So you, being an expert problem solver, they requested your assistance.

The structure of Rajshahi University is a tree consisting of $n$ nodes and $n−1$ roads connecting them. The length of every road is 1 unit. The tour start at node 1 where the RU gate is situated. While traversing RU, they won't visit one node more than once, as they want to walk as little as possible. From each node, they go to any other neighbouring nodes that they haven't visited before with equal probabilities, and their short trip finishes when there are no such nodes left to traverse. For example, if a node has four unvisited neighbouring nodes, they will go to one of the four nodes with a probability of $25\%$ and when they reach a node where each of its neighbouring nodes have been visited before, their short trip concludes.

They want you to calculate the expected length (expected value of length) of their short trip. To know more about expected (average) value, you can follow this link: [https://en.wikipedia.org/wiki/Expected_value](https://en.wikipedia.org/wiki/Expected_value).

They want you to calculate the expected length (expected value of length) of their short trip. To know more about expected (average) value you can follow this link \url{https://en.wikipedia.org/wiki/Expected_value}.

\InputFile
The first line contains a single integer $n$ ($1 \leq n \leq 100000$)~--- number of nodes.

Then $n-1$ lines follow. The $i$-th line of these lines contains two integers $u_i$ and $v_i$ ($1 \leq u_i,v_i \leq n$, $u_i \neq v_i$)~--- the nodes connected by the $i$-th road.

It is guaranteed that one can reach any node from any other by the roads.

\OutputFile
Print a number~--- the expected length of their short trip. The short trip starts in the node $1$.

Your answer will be considered correct if its absolute or relative error does not exceed $10^{-6}$.

\Examples

\Note
In the first sample, their short trip may end in nodes $3$ or $4$ with equal probability. The distance to node $3$ is $1$ and to node $4$ is $2$, so the expected length is $1.5$.

In the second sample, their short trip may end in node $4$ or $5$. The distance to the both nodes is $2$, so the expected length is $2$.


# Aditya Loves Stopper


The problem setters from KUET & RUET selected the problem that would be suitable for the contest, but Aditya was not satisfied with the problem set as there were no \textit{stopper}. Aditya also had a superpower of stumbling upon the stopper problem in any IUPCs he participated so far. So, we, the problem setter gave him the duty of finding a suitable stopper for the contest. Now you might wonder what a "suitable stopper" is. It a type of a problem which is easy to understand but hard to solve. So our stopper lover Aditya came with the following problem for you to solve and promised to give treat to the first solver who successfully solved his "suitable stopper".

You are on the origin (at point 0) of an infinite number line. There are $n$ objects that you can push, the $i$-th object is on a position $a_i$. All positions of the objects are distinct meaning no two same object will be in the same position. There are also $m$ super positions on the number line, the $j$-th super position is $b_j$. All the super positions are also distinct.

In one move, you can go one position to the left or to the right. If there is an object in the direction of your move, then you push the object to the next position in that direction. If the next position is taken by another object, then that object is also pushed to the next position, and so on. But you needed to follow two rules. One, you can't go through the objects. Two, You can't pull the objects toward you.

You are allowed to perform any number of moves (possibly, zero). After performing all your moves, you earn one point for every object that is placed on a super position. Your goal is to maximize your total point. Note that some objects can be initially place on super positions and your point count will only be applicable on the final state of the objects after you have finished all your moves. Read Note for more clarity.

\InputFile
The first line contains a single integer $t$ ($1 \le t \le 1000$)~--- the number of testcases.

Then descriptions of $t$ testcases follow.

The first line of each testcase contains two integers $n$ and $m$ ($1 \le n, m \le 2 \cdot 10^5$)~--- the number of objects and the number of super positions, respectively.

The second line of each testcase contains $n$ distinct integers in the increasing order $a_1, a_2, \dots, a_n$ ($-10^9 \le a_1 < a_2 < \dots < a_n \le 10^9$; $a_i \neq 0$)~--- the initial positions of the objects.

The third line of each testcase contains $m$ distinct integers in the increasing order $b_1, b_2, \dots, b_m$ ($-10^9 \le b_1 < b_2 < \dots < b_m \le 10^9$; $b_i \neq 0$)~--- the super positions.

The sum of $n$ over all testcases doesn't exceed $2 \cdot 10^5$. The sum of $m$ over all testcases doesn't exceed $2 \cdot 10^5$.

\OutputFile
For each testcase print a single integer~--- the maximum point you can achieve

\Example

\Note
In the first testcase you can go $5$ to the right: the object on position $1$ gets pushed to position $6$ and the object on position $5$ gets pushed to position $7$. Then you can go $6$ to the left to end up on position $-1$ and push a object to $-2$. At the end, the boxes are on positions $[-2, 6, 7, 11, 15]$, respectively. Among them positions $[-2, 6, 7, 15]$ are super position, thus, the answer is $4$.

In the second testcase you can push the object from $-1$ to $-10^9$, then the object from $1$ to $10^9$ and obtain the answer $2$.

The third testcase showcases that you are not allowed to pull the object, thus, you can't bring them closer to super positions.

In the fourth testcase all the objects are already on super positions, so you can do nothing and still obtain the answer $3$.

In the fifth testcase there are fewer super positions than boxes. You can move either $8$ or $9$ to the right to have some object on position $10$.

