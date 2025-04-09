

# Resistor

Materials in general have a characteristic behavior of resisting the flow of electric charge. **The physical property, or ability to resist current, is known as resistance** and is represented by the symbol $R$ 
![[Pasted image 20250326074900.png]]

The resistance of any material with uniform cross-sectional area $A$ depends on $A$ and its length $l$, that is

$$
R = \rho \frac lA
$$

Where, $\rho$ is known as the resistivity of the material

Good conductors, such as copper and aluminium, have low resistivity, while insulators, such as mica and paper, have high resistivity.



# Ohm's Law

**Ohm's law states that the current through a conductor between two points is directly proportional to the voltage across the two points**
$$
i \propto v
$$
$$
i = vG
$$
Where, $G$ is the proportionality constant
$$
G = \frac 1R
$$
$$
v = iR
$$


## Conductance

**Reciprocal of resistance is known as conductance ($G$).**

The resistance $R$ of an element denotes its ability to resist the flow of electric current; it is measure in ohms ($\ohm$).

Conductance is the ability of an element to conduct electric current; it is measure in mhos or siemens ($S$).


## Short Circuit

A short circuit is a circuit element with resistance approaching zero.
![[Pasted image 20250326075532.png]]


## Open Circuit

An open circuit is a circuit element with resistance approaching infinity

![[Pasted image 20250326075601.png]]


## Nodes, Branches and Loops

A branch represents a single element such as voltage source source or a resistor. A branch represents any two-terminal element.

A node is the point of connection between two or more branches

A loop is any closed path in a circuit

![[Pasted image 20250326075730.png]]



## Series Connection

Two or more elements are in series if they carry the same current

![[Pasted image 20250326075759.png]]

Elements are in series when they are chain-connected or connected sequentially, end to end


## Parallel Connection

Two or more elements are in parallel if they are connected to the same two nodes and consequently have the same voltage across them.



# Kirchhoff's Current Law (KCL)

**Kirchhoff's Current Law (KCL) states that the algebraic sums of currents entering a node is zero.**

![[Pasted image 20250326075958.png]]

$$
i_1 + (-i_2) + i_3 + i_4 + (-i_5) = 0
$$
$$
i_1 + i_3 + i_4 = i_2 + i_5
$$

The sum of the currents entering a node is equal to the sum of the currents leaving the node.


# Kirchhoff's Voltage Law (KVL)

**Kirchhoff's Voltage Law (KVL) states that the algebraic sum of all voltages around a closed path (or loop) is zero**

$$
\sum_{m = 1}^{M}V_m = 0
$$
![[Pasted image 20250326082550.png]]

$$
-v_1 + v_2 + v_3 - v_4 + v_5 = 0
$$