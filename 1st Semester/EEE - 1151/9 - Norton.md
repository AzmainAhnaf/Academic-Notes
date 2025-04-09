
# Norton's Theorem

**Norton's theorem states that a [[7 - Superposition#Linearity Property|linear two-terminal circuit]] can be replaced by any equivalent circuit consisting of a current source $I_N$ in parallel with resistor $R_N$, where $I_N$ is the [[2 - Law#Short Circuit|short-circuit]] current through the terminals and $R_N$ is the input or equivalent resistance at the terminals when the [[1 - Introduction#Independent Source|independent sources]] are turned off**
![[Pasted image 20250328153144.png]]
Two circuits are said to be equivalent if they have the same voltage-current relation at their terminals.
![[Pasted image 20250328153222.png]]

[[8 - Thevenin|Thevenin]] and Norton resistances are equal, $R_N = R_{Th}$

Relationship between Norton's and [[8 - Thevenin|Thevenin's]] theorem is
$$
I_N = \frac{V_{Th}}{R_{Th}}
$$

If the network had [[1 - Introduction#Dependent Source|dependent sources]], we turn of all [[1 - Introduction#Independent Source|independent sources]]. [[1 - Introduction#Dependent Source|Dependent sources]] are not to be turned off because they are controlled by circuit variables. We apply a voltage source $v_o$ at terminals a and be and determine the resulting current. Then $R_N = \frac{v_o}{i_o}$
![[Pasted image 20250328153855.png|300]]


Alternatively, we may insert a current [[1 - Introduction#Source|source]] at terminals $i_o$ a-b as shown in figure and find the terminal voltage. Again then $R_N = \frac{v_o}{i_o}$
![[Pasted image 20250328154002.png|300]]



