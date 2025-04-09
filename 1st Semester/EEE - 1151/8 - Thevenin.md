# Thevenin's Theorem

**Thevenin's theorem states that a [[7 - Superposition#Linearity Property|linear two-terminal circuit]] can be replaced by an equivalent circuit consisting of a [[1 - Introduction#Source|voltage source]] $V_{Th}$ in series with a resistor $R_{Th}$, where $V_{Th}$ is the [[2 - Law#Open Circuit|open-circuit]] voltage at the terminals and $R_{Th}$ is the input or equivalent resistance at the terminals when the independent sources are turned off.**
![[Pasted image 20250328145147.png]]
Two circuits are said to be equivalent if they have the same voltage current relation at their terminals.
![[Pasted image 20250328145236.png]]


If the network has dependent sources, we turn off all [[1 - Introduction#Independent Source|independent sources]]. Dependent sources are not to be turned off because they are controlled by circuit variables. We apply a voltage source $v_o$ at terminals a and b and determine the resulting current. Then $R_{Th} = \frac{v_o}{i_o}$
![[Pasted image 20250328152221.png]]

Alternatively, we may insert a current source at terminals $i_o$ a-b as shown in following figure and find the terminal voltage. Again then $R_{Th} = \frac{v_o}{i_o}$ 