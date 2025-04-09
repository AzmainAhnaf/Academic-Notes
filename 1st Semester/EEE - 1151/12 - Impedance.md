
# Capacitors

- A capacitor is a [[1 - Introduction#Circuit Elements|passive element]]
- Capacitor stores energy in its electric field
- A capacitor consists of two conducting plates separated by an insulator (or dielectric)
- Plates may be aluminum foil the dielectric may be air, ceramic, paper etc.
![[Pasted image 20250401070559.png|300]]
- When a voltage [[1 - Introduction#Source|source]] is connected to the capacitor, the source deposits a positive charge $q$ on one plate
![[Pasted image 20250401070807.png]]
- A negative charge deposits on the other plate. The capacitor store the electric charge.
- The amount of charge stored, represented by $q$, is directly proportional to the applied voltage so that
$$
q = CV
$$
- Where, $C$, the constant of proportionality, is known as the capacitance of the capacitor. The unit of capacitance is the farad $(F)$
- Capacitance depends on the physical dimensions of the capacitor
$$
C = \frac{\epsilon A}{d}
$$
![[Pasted image 20250401071018.png|200]]
Where,
	$A$ = the surface area of each plate
	$d$ = distance between the plates
	$\epsilon$ = the permittivity of the dielectric material between the plates
![[Pasted image 20250401071115.png]]

- Current-voltage relationship for a capacitor is
$$
i = C \frac{dv}{dt}
$$
- Energy stored in the capacitor is
$$
w = \frac 12 Cv^2
$$
- A capacitor is an [[2 - Law#Open Circuit|open circuit]] to dc
![[Pasted image 20250401071926.png]]
- The ideal capacitor does not dissipate energy. It takes [[14 - Power|power]] from the circuit when storing energy in its field and return previously stored energy when delivering power to the circuit


**Equivalent Capacitance:**

![[Pasted image 20250401072053.png]]

Equivalent capacitance $C_{eq}$ of the parallel connected capacitor is
$$
C_{eq} = C_1 + C_2 + C_3 +\ ... \ + C_N
$$

![[Pasted image 20250401072253.png]]

Equivalent capacitance $C_{eq}$ of the series connected capacitor is
$$
\frac 1{C_{eq}} = \frac 1{C_1} + \frac 1{C_2} + \frac 1{C_3} +\ ...\ + \frac 1{C_N}
$$



# Inductor

- Inductor is a [[1 - Introduction#Circuit Elements|passive element]]
- Inductor store energy in its magnetic field
- An inductor consists of a coil of conducting wire
	![[Pasted image 20250401072510.png]]
- Voltage across the inductor is directly proportion to the time rate of change of current
$$
v = L\frac{di}{dt}
$$
- Where $L$ is the constant of proportionality called the inductance of the inductor. The unit of inductance is the henry $(H)$
- Energy stored in inductor is
$$
w = \frac 12 Li^2
$$
- An inductor acts like a [[2 - Law#Short Circuit|short circuit]] to dc
	![[Pasted image 20250401072701.png]]
- Ideal inductor does not dissipate energy. The energy stored in it can be returned at a later time.

	![[Pasted image 20250401072757.png]]
- The equivalent inductance of series-connected inductor is
$$
L_{eq} = L_1 + L_2 + L_3 +\ ...\ + L_N
$$

	![[Pasted image 20250401073126.png]]
- The equivalent inductance of parallel-connected inductor is
$$
\frac 1{L_{eq}} = \frac 1{L_1} + \frac 1{L_2} + \frac 1{L_2} +\ ...\ + \frac 1{L_N}
$$


# [[11 - Phasor|Phasor]] Relationships for [[3 - Resistance|Resistor]]

Assume, current through a [[3 - Resistance|resistor]] $R$ is
$$
i = I_m\cos{(\omega t + \phi)}
$$
![[Pasted image 20250401080437.png]]

voltage across the resistor is
$$
v = iR = RI_m\cos{(\omega t + \phi)}
$$
[[11 - Phasor|Phasor]] form of this voltage is
$$
V = RI_m\angle \phi
$$
[[11 - Phasor|Phasor]] representation of the current is
$$
I = I_m\angle \phi
$$
Voltage-current relationship in [[11 - Phasor|phasor]] form is
$$
V = RI
$$
Voltage-current relation for the resistor in the [[11 - Phasor|phasor]] domain is shown in the following figure
![[Pasted image 20250401080654.png]]
Voltage and current are in phase


# [[11 - Phasor|Phasor]] Relationships for [[12 - Impedance#Inductor|Inductor]]

Assume the current through the [[12 - Impedance#Inductor|inductor]] is
$$
i = I_m\cos{(\omega t + \phi)}
$$
![[Pasted image 20250401080933.png]]

Voltage across the [[12 - Impedance#Inductor|inductor]] is
$$
v = L\frac{di}{dt}
$$
$$
= -\omega LI_m\cos{(\omega t + \phi)}
$$
$$
= \omega LI_m\sin{(\omega t + \phi + 90 \degree)}
$$
$$
= \omega LI_m\angle{(\phi + 90 \degree)}
$$
$$
\omega L I_m\angle \phi \cdot 1\angle 90 \degree
$$
$$
\therefore V = j\omega LI
$$
[[11 - Phasor|Phasor]] diagram for inductor is
![[Pasted image 20250401081445.png]]

[[11 - Phasor#Phase Angles|Phase angle]] between voltage and current = $(\phi + 90 \degree) - \phi$ = $90 \degree$
Voltage leads current by $90 \degree$
Current lags voltage by $90 \degree$


# [[11 - Phasor|Phasor]] Relationships for [[12 - Impedance#Capacitors|Capacitor]]

Assume the voltage across [[12 - Impedance#Capacitors|capacitor]] is
$$
v(t) = V_m\cos{(\omega t + \phi)}
$$
Current through the [[12 - Impedance#Capacitors|capacitor]] is
$$
i = C\frac{dv}{dt}
$$
$$
= -\omega CV_m\sin{(\omega t + \phi)}
$$
$$
= \omega CV_m \cos{(\omega t + \phi + 90 \degree)}
$$
$$
\omega CV_m\angle {(\phi + 90 \degree)}
$$
$$
I = j\omega CV
$$
[[11 - Phasor#Phase Angles|phase angle]] between voltage and current = $\phi - (\phi + 90 \degree)$ = $-90 \degree$
Voltage lags current by $90 \degree$

Phasor diagram for capacitor is
![[Pasted image 20250401082446.png]]


| Element | Time Domain           | Frequency Domain           |
| ------- | --------------------- | -------------------------- |
| $R$     | $v = Ri$              | $V = RI$                   |
| $L$     | $v = L \frac{di}{dt}$ | $V = j \omega LI$          |
| C       | $i = C\frac{dv}{dt}$  | $V = \frac{I}{j \omega C}$ |
# Impedance

Voltage-current relations for the three [[1 - Introduction#Circuit Elements|passive elements]] are given in the above table, those equations may be written in terms of the ratio of the [[11 - Phasor|phasor]] voltage to the [[11 - Phasor|phasor]] current as
$$
\frac VI = R
$$
$$
\frac VI = j \omega L
$$
$$
\frac VI = \frac 1{j \omega C}
$$
[[2 - Law#Ohm's Law|Ohm's law]] in [[11 - Phasor|phasor]] form for any type of [[1 - Introduction#Circuit Elements|element]] as
$$
Z = \frac VI\ or,\ V = ZI
$$
Where $Z$ is a [[11 - Phasor#Sinusoids|frequency]]-dependent quantity known as impedance, measure in ohms

The impedance $Z$ of a circuit is the ratio of the [[11 - Phasor|phasor]] voltage $V$ to the [[11 - Phasor|phasor]] current $I$

The impedance of [[12 - Impedance#11 - Phasor Phasor Relationships for 3 - Resistance Resistor|resistor]] is
$$
Z = R
$$
The impedance of [[12 - Impedance#11 - Phasor Phasor Relationships for 12 - Impedance Inductor Inductor|inductor]] is
$$
Z = j \omega L
$$
The impedance of [[12 - Impedance#11 - Phasor Phasor Relationships for 12 - Impedance Capacitors Capacitor|capacitor]] is
$$
Z = \frac1 {j \omega C}
$$
Impedances may be expressed in the rectangular form as
$$
Z = R+ jX
$$
where,
	$R$ = $Re(Z)$, is called the resistance
	$X$ = $Im(Z)$, is called the reactance

Impedance is inductive when $X$ is positive or capacitive when $X$ is negative

Impedance $Z = R + jX$ is said to be inductive or lagging since current lags voltage

Impedance $Z = R - jX$ is said to be capacitive or leading since current leads voltage

The impedance may also be expressed in polar form as
$$
Z = |Z|\angle \theta = R + jX
$$
where
$$
|Z| = \sqrt{R^2 + X^2}
$$
$$
\theta = \tan^{-1} \frac XR
$$
and
$$
R = |Z|\cos \theta
$$
$$
X = |Z| \sin \theta
$$

The admittance $Y$ is the reciprocal of impedance

The admittance $Y$ of an element (or a circuit) is the ration of the phasor current through to it to the phasor voltage across it
$$
Y = \frac 1Z = \frac IV
$$
$$
Y = G + jB
$$

Where $G = Re(Y)$ is called the conductance and $B = Im(Y)$ is called the susceptance

Unit of admittance, conductance, susceptance is siemens (or mhos)


| Element | Impedance                  | Admittance                |
| ------- | -------------------------- | ------------------------- |
| $R$     | $Z = R$                    | $Y = \frac 1R$            |
| $L$     | $Z = j \omega L$           | $Y = \frac 1{j \omega L}$ |
| $C$     | $Z = \frac{1}{j \omega C}$ | $Y = j \omega C$          |


# Circuit Theorem

[[2 - Law#Kirchhoff's Voltage Law (KVL)|Kirchhoff's voltage law]] and [[2 - Law#Kirchhoff's Current Law (KCL)|current law]] can also be applied in phasor form resulting in following two equations
In a [[5 - Mesh|mesh]], 
$$
V_1 + V_2 + \ ...\ + V_n = 0
$$
In a [[4 - Node|node]],
$$
I_1 + I_2 +\ ...\ I_n = 0
$$
[[2 - Law#Ohm's Law|Ohm's law]] in [[11 - Phasor|phasor]] form 
$$
V = ZI
$$


# Impedance Combinations

![[Pasted image 20250401090300.png]]

The same current $I$ flows through the impedances

Applying [[2 - Law#Kirchhoff's Voltage Law (KVL)|KVL]] around the loop
$$
V = V_1 + V_2 + \ ...\ V_N = I(Z_1 + Z_2 +\ ...\ Z_N)
$$
 The equivalent impedance at the input terminals is
$$
Z_{eq} = \frac VI = Z_1 + Z_2 +\ ...\ + Z_N
$$


![[Pasted image 20250401090435.png]]

The voltage across each impedance is the same

Applying [[2 - Law#Kirchhoff's Current Law (KCL)|KCL]] at the top node,
$$
I = I_1 + I_2 + \ ...\ I_N = V(\frac 1{Z_1} + \frac 1{Z_2} + \ ...\ + \frac 1{Z_N})
$$
The equivalent impedance is,
$$
\frac 1{Z_{eq}} = \frac IV = \frac 1{Z_1} + \frac 1{Z_2} + \ ...\ + \frac 1{Z_N}
$$

[[3 - Resistance#Wye-Delta Transformations|Delta-to-wye]] and wye-to-delta transformations for impedance is same as resistive circuit

![[Pasted image 20250401091024.png]]

$Y-\Delta$ conversion:
$$
Z_a = \frac{Z_1Z_2 + Z_2Z_3 + Z_1Z_3}{Z_1}
$$
$$
Z_b = \frac{Z_1Z_2 + Z_2Z_3 + Z_1Z_3}{Z_2}
$$
$$
Z_c = \frac{Z_1Z_2 + Z_2Z_3 + Z_1Z_3}{Z_3}
$$


![[Pasted image 20250401091206.png]]

$\Delta-Y$  conversion:
$$
Z_1 = \frac{Z_bZ_c}{Z_a + Z_b + Z_c}
$$
$$
Z_2 = \frac{Z_cZ_a}{Z_a + Z_b + Z_c}
$$
$$
Z_3 = \frac{Z_aZ_b}{Z_a + Z_b + Z_c}
$$

A delta or wye circuit is said to be balanced if it has equal impedances in all three branches.

When a $\Delta-Y$ circuit is balanced, the equation may write
$$
Z_{\Delta} = 3Z_Y
$$
