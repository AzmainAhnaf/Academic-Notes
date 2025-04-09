
# Maximum Power Transfer Theorem

Practical source have internal [[3 - Resistance|resistance]]

Power loss occurred in the internal [[3 - Resistance|resistance]]

In any electric circuit, the electrical energy is delivered to the load where it is converted into a useful work.

For give circuit with known internal [[3 - Resistance|resistance]], the load size always affects the amount of [[14 - Power|power]] transferred from the supply [[1 - Introduction#Source|source]]

Any change in the load [[3 - Resistance|resistance]] results to change in power transfer to the load.

![[Pasted image 20250329035213.png|250]]

Our main objective is to deliver maximum power to load. Maximum power transfer theorem determine the condition that transfer the maximum power to the load.

The [[8 - Thevenin|Thevenin equivalent]] is useful in finding the maximum power a [[7 - Superposition#Linearity Property|linear circuit]] can deliver to a load

![[Pasted image 20250329035419.png]]

The [[14 - Power|power]] delivered to the load is
$$
p = i_2R_L = \left( \frac{V_{Th}}{R_{Th} + R_L}\right)^2R_L
$$

For a given circuit, $V_{Th}$ and $R_{Th}$ are fixed

By varying the load resistance $R_L$, the power delivered to the load varies as sketched in the following figure.
![[Pasted image 20250329035814.png|250]]

When, $R_L = R_{Th}$, $P$ = $P_{max}$
When, $R_L < R_{Th}$, $P < P_{max}$
When, $R_L > R_{Th}$, $P < P_{max}$

Maximum power is transferred to load when $R_L = R_{Th}$

**Maximum power transfer theorem states that maximum power is transferred to the load when the load resistance equals to the [[8 - Thevenin|Thevenin]] Resistance**. $(R_L = R_{Th})$

**Derivation**
![[Pasted image 20250329050203.png|300]]


Power delivered to the load $R_L$ is
$$
P = i^2R_L
$$
$$
= \left( \frac{V_{Th}}{R_{Th} + R_L} \right)^2R\ \ .......(i)
$$

We differentiate equation $(i)$ with respect to $R_L$ and set the result equal to zero
$$
\frac{dP}{dR_L} = V_{Th}^2 \left[  \frac{(R_{Th + R_L})^2 - 2R_L(R_{Th} + R_L)}{(R_{Th} + R_L)^4} \right]
$$
$$
\Rightarrow V^2_{Th}\left[ \frac{R_{Th} + R_L - 2R_L}{(R_{Th} + R_L)^3} \right] = 0
$$
But $(R_{Th} + R_L)^3$ cannot be zero hence $R_{Th} + R_L - 2R_L = 0$ which further evolves to $R_{Th} = R_L$

The maximum power transferred to the load is
$$
P = i_2R_L = \left( \frac{V_{Th}}{R_{Th} + R_L} \right)^2R_L
$$
$$
P_{max} = \frac{V^2_{Th}}{4R_{Th}}
$$
