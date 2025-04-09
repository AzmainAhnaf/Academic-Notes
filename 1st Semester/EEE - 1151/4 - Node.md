
# Nodal Analysis

Nodal analysis provides a procedure for analyzing circuits using node voltages as the circuit variables

**Steps to Determine Node Voltages** \[Important]

1. Select a node as the reference node. Assign voltages $v_1$, $v_2$,..., $v_{n - 1}$ to the remaining $n - 1$ nodes. The voltages are reference with respect to the reference node.
2. Apply [[2 - Law#Kirchhoff's Current Law (KCL)|KCL]] to each of the $n - 1$ nonreference nodes. Use Ohm's law to express the branch currents in terms of node voltages.
3. Solve the resulting simultaneous equations to obtain the unknown node voltages.



# Nodal Analysis with Voltage Sources

If a voltage source is connected between the reference node and a nonreference node, we simply set the voltage at the nonreference node equal to the voltage of the voltage source

![[Pasted image 20250328023950.png]]

In this picture $v_1$ will be set to $10V$


If the voltage source (dependent or independent) is connected between two nonreference nodes, the two nonreference nodes form a generalized node or supernode; we apply both KCL and KVL to determine the node voltages.

A supernode is formed by enclosing a (dependent or independent) voltage source connected between two nonreference nodes and any elements connected in parallel with it.

A supernode has no voltage of its own

A supernode requires the application of both [[2 - Law#Kirchhoff's Current Law (KCL)|KCL]] and [[2 - Law#Kirchhoff's Voltage Law (KVL)|KVL]]


