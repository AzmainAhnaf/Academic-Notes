
# Series Resistors

![[Pasted image 20250326084411.png|239]]

The two resistors are in series, since the same current $i$ flows in both of them.

Voltage across in each resistors are $v_1 = iR_1$ and $v_2 = iR_2$

Applying [[2 - Law#Kirchhoff's Voltage Law (KVL)|KVL]] to loop, we obtain

$$
-v + v_1 + v_2 = 0
$$
$$
\Rightarrow v = v_1 + v_2 = i(R_1 + R_2)
$$
![[Pasted image 20250326084235.png]]
$$
V = iR_{eq}
$$
$$
\therefore R_{eq} = R_1 + R_2
$$
The equivalent resistance of any number of resistors connected in series is the sum of the individual resistances

For $N$ resistors in series then
$$
R_{eq} = R_1 + R_2 +\ ...\ ...\ + R_N = \sum_{n = 1}^{N}R_n
$$


# Voltage Divider Principle

![[Pasted image 20250326084948.png]]

Voltage across in each resistors are
$$
v_1 = iR_1 \text{ and } v_2 = iR_2
$$
$$
i = \frac{v}{R_1 + R_2}
$$
putting value of $i$ in $v_1$ and $v_2$
$$
v_1 = \frac{R_1}{R_1 + R_2}v
$$
$$
v_2 = \frac{R_2}{R_1 + R_2}v
$$

If a voltage divider has $N$ resistors in series with the source voltage $v$, the nth resistor ($R_n$) will have a voltage drop of
$$
v_n = \frac{R_n}{R_1 + R_2 + R_3 +\ ...\ ...\ + R_N}v
$$

Voltage divider rule is applied in the series connected circuit


# Parallel Resistor

![[Pasted image 20250326085340.png]]

Two resistors are connected in parallel with voltage source and therefore have the same voltage across them
$$
v = i_1R_1 = i_2R_2
$$
$$
i_1 = \frac v{R_1} \text{ and } i_2 = \frac v{R_2}
$$
Applying [[2 - Law#Kirchhoff's Current Law (KCL)|KCL]] to node $a$, we obtain
$$
i = i_1 + i_2 = \frac v{R_1} + \frac v{R_2} = v \left( \frac 1{R_1} + \frac 1{R_2} \right) = \frac v{R_{eq}}
$$
$$
\therefore \frac 1{R_{eq}} = \frac 1{R_1} + \frac 1{R_2}
$$
![[Pasted image 20250326085804.png]]
$$
R_{eq} = \frac{R_1R_2}{R_1 + R_2}
$$
The equivalent resistance of two parallel resistors is equal to the product of their resistances divided by their sum

For $N$ resistors in parallel then
$$
\frac 1{R_{eq}} = \frac 1{R_1} + \frac 1{R_2} +\ ...\ ...\ + \frac1{R_N}
$$

$R_{eq}$ is always smaller than the resistance of the smallest resistor in the parallel combination



# Current Divider Principle

![[Pasted image 20250326090801.png]]

Voltage across the resistor is
$$
v = R_{eq}i = \frac{R_1R_2}{R_1 + R_2}i
$$
Current flow through in each resistors are
$$
i_1 = \frac v{R_1} \Rightarrow i_1 = \frac{R_2}{R_1 + R_2}i
$$
$$
i_2 = \frac v{R_2} \Rightarrow i_2 = \frac{R_1}{R_1 + R_2}i
$$

Current divider rule using conductance
$$
G = \frac 1R
$$
![[Pasted image 20250326093947.png]]
$$
i_1 = \frac{G_1}{G_1 + G_2}i
$$
$$
i_2 = \frac{G_2}{G_1 + G_2}i
$$

If a current divider has $N$ resistors in parallel with the source current $i$, the $n$-th resistors $R_n$ will have current
$$
i_n = \frac{G_n}{G_1 + G_2 +\ ...\ ...\ + G_n}i
$$




# Wye-Delta Transformations

![[Pasted image 20250327124059.png]]

![[Pasted image 20250327124121.png]]


## Delta to Wye Conversion

![[Pasted image 20250327124310.png]]

To obtain the equivalent resistances in the wye (Y) network, we compare the two networks and make sure that the resistance between each pair of nodes in the $\Delta$ (or $\pi$) network is the same as the resistance between the same pair of nodes in the $Y$ (or $T$) network.

![[Pasted image 20250327125110.png]]
$$
R_{12}(Y) = R_1 + R_3
$$
$$
R_{12}(\Delta) = R_b || (R_a + R_c) = \frac{R_b(R_a + R_c)}{R_a + R_b + R_c}
$$
$$
\therefore R_1 + R_3 = \frac{R_b(R_a + R_c)}{R_a + R_b + R_c}\ ......(i)
$$

Similarly,
$$
R_{13} = R_1 + R_2 = \frac{R_c(R_a + R_b)}{R_a + R_b + R_c}\ ......(ii)
$$
$$
R_{34} = R_2 + R_3 = \frac{R_a(R_b + R_c)}{R_a + R_b + R_c}\ ......(iii)
$$

Solving equation $(i)$, $(ii)$ and $(iii)$ we get delta to wye conversion as follows
![[Pasted image 20250327132250.png]]
$$
R_1 = \frac{R_bR_c}{R_a + R_b + R_c}
$$
$$
R_2 = \frac{R_aR_c}{R_a + R_b + R_c}
$$
$$
R_3 = \frac{R_aR_b}{R_a + R_b + R_c}
$$

and similarly we also get the equation for wye to delta conversion
![[Pasted image 20250327132517.png]]
$$
R_a = \frac{R_1R_2 + R_2R_3 + R_3R_1}{R_1}
$$
$$
R_b = \frac{R_1R_2 + R_2R_3 + R_3R_1}{R_2}
$$
$$
R_c = \frac{R_1R_2 + R_2R_3 + R_3R_1}{R_3}
$$
