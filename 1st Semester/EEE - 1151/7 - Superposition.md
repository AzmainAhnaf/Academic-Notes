
# Homogeneity Property

**The homogeneity property states that if the input is multiplied by a constant, then the output(also called the response) is multiplied by the same constant.**

For a resistor, [[2 - Law#Ohm's Law|Ohm's law]] relates the input $i$ to the output $v$.
$$
v = iR
$$

If the current is increased by a constant $k$, then the voltage increases correspondingly by $k$; that is,
$$
kv = kiR
$$


# Additivity Property

**The additivity property requires that the response to a sum of inputs is the sum of the responses to each input applied separately**

If $i_1$ ampere current separately applied to the resistor then output voltage is $v_1 = i_1R$ 

If $i_2$ ampere current separately applied to the resistor then output voltage is $v_2 = i_2R$

If ($i_1 + i_2$) ampere current applied to the resistor then output voltage is
$$
v = (i_1 + i_2)R = i_1R + i_2R = v_1 + v_2
$$


# Linearity Property

**The linearity property is a combination of both the [[7 - Superposition#Homogeneity Property|homogeneity property]] and the [[7 - Superposition#Additivity Property|additivity property]]**

A circuit is linear if it has both additive and homogenous property

A linear circuit consists of only linear [[1 - Introduction#Circuit Elements|elements]], linear [[1 - Introduction#Dependent Source|dependent sources]], and [[1 - Introduction#Independent Source|independent sources]].

A linear circuit is one whose output is linearly related (or directly proportional) to its input.

A resistor is a linear element because the voltage-current relationship satisfied both the homogeneity and the additivity property


**Relationship between [[14 - Power|power]] and voltage (or current) is nonlinear**

$p_1 = i_1^2R$, $p_2 = i_2^2R$
$$
p = (i_1 + i_2)^2R = i_1^2R + i_2^2R + 2i_1i_2R
$$
$$
\therefore p \ne p_1 + p_2
$$


# Superposition Theorem

**The superposition principle states that the voltage across (or current through) an element in a linear circuit is the algebraic sum of the voltages across (or currents through) that element due to each independent source acting alone**

The principle of superposition helps us to analyze a linear circuit with more than one independent source by calculating the contribution of each independent source separately

We must keep two things in mind:
1. We consider one [[1 - Introduction#Independent Source|independent sources]] at a time while all other [[1 - Introduction#Independent Source|independent sources]] are turned off. This implies that we replace every voltage source by 0$V$ (or a short circuit), and every current source by 0$A$ (or an open circuit). This way we obtain a simpler and more manageable circuit.
2. [[1 - Introduction#Dependent Source|dependent sources]] are left intact because they are controlled by circuit variables

**Steps to apply superposition principle:**

1. Turn of all [[1 - Introduction#Independent Source|independent sources]] except one source. Find the output (voltage or current) due to that [[1 - Introduction#Circuit Elements|active source]] using [[5 - Mesh|mesh analysis]] or [[4 - Node|nodal analysis]]
2. Repeat step 1 for each of the other [[1 - Introduction#Independent Source|independent sources]].
3. Find the total contribution by adding algebraically all the contributions due to each the [[1 - Introduction#Independent Source|independent sources]].