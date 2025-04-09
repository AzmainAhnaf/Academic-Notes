
# Transfer Function

**The frequency response of a circuit is the variation in its behavior with change in signal frequency**

The transfer function $H(\omega)$ (also called the network function) is a useful analytical tool for finding the frequency response of a circuit. In fact, the frequency response of a circuit is the plot of the circuit's transfer function $H(\omega)$ versus $\omega$, with $\omega$ varying from $0$ to $\infty$.

The transfer function $H(\omega)$ of a circuit is the frequency-dependent ration of a phasor output $Y(\omega)$ (an element voltage or current) to a phasor input $X(\omega)$ (source voltage or current)
![[Pasted image 20250402070440.png]]
$$
H(\omega) = \frac{Y(\omega)}{X(\omega)}
$$
Assuming zero initial conditions. Since the input and output can be either voltage or current at ay place in the circuit, there are four possible transfer functions:

	$H(\omega) = \text{Voltage gain} = \frac{V_o(\omega)}{V_i(\omega)}$
	$H(\omega) = \text{Current gain} = \frac{I_o(\omega)}{I_i(\omega)}$
	$H(\omega) = \text{Transfer Impedance} = \frac{V_o(\omega)}{I_i(\omega)}$
	$H(\omega) = \text{Transfer Admittance} = \frac{I_o(\omega)}{V_i(\omega)}$


# Series Resonance

![[Pasted image 20250402083425.png]]

Series resonance in an RLC circuit occurs when the inductive and capacitive reactance are equal, resulting in a purely resistive impedance, maximum current, and unity power factor at a specific resonant frequency.

In the above circuit the equivalent impedance would be,
$$
Z_{eq} = R + j(\omega L - \frac 1{\omega C})
$$
Let,
$$
X_L = j \omega L
$$
$$
X_C = \frac{-j}{\omega C} 
$$
Series resonance occur if $X_L = X_C$ 
$$
\omega L - \frac 1{\omega C} = 0
$$
Solving for $\omega$ we get,
$$
\omega = \frac{1}{\sqrt{LC}}
$$
We know frequency, $\omega = 2\pi f$ 
So the resonance frequency will be,
$$
f_o = \frac{1}{2\pi \sqrt{LC}}
$$
When the resonance condition is met,
1. The impedance is purely resistive, thus $Z = R$. In other words, the $LC$ series combination acts like a short circuit, and the entire voltage is across $R$
2. The voltage $V_s$ and the current $I$ are in phase, so that the power factor is unity.
3. Current $I$ is maximum

![[Pasted image 20250402085037.png|400]]

The average power dissipated by the RLC circuit is,
$$
P(\omega) = \frac 12I_2R
$$
The highest power dissipated occurs at resonance, when $I = V_m/R$, so that
$$
P(\omega_0) = \frac 12 \frac{V_m^2}{R}
$$
At certain frequencies $\omega = \omega_1, \omega_2$, the dissipated power is half the maximum value; that is,
$$
P(\omega_1) - P(\omega_2) = \frac 12 \cdot \frac{(V_m/\sqrt2)^2}{2} = \frac{V_m^2}{4R}
$$
Hence, $\omega_1$ and $\omega_2$ are called the half-power frequencies or cutoff frequency.

The half-power frequencies are obtained by setting Re($Z$) equal to $\sqrt2 R$,
$$
\sqrt{R_2 + \left( \omega L - \frac 1{\omega C} \right)^2} = \sqrt 2R
$$
Solving for $\omega$, we obtain
$$
\omega_1 = -\frac R{2L} + \sqrt{\left( \frac{R}{2L} \right)^2 + \frac 1{LC}}
$$
$$
\omega_2 = \frac R{2L} + \sqrt{\left( \frac{R}{2L} \right)^2 + \frac 1{LC}}
$$
If the length of the whole bandwidth is $B$ then,
$$
B = \omega_2 - \omega_1
$$
$$
\omega_1 = \omega_0 - \frac{B}2
$$
$$
\omega_2 = \omega_0 + \frac{B}2
$$
We can relate the half-power frequencies with the resonant frequency
$$
\omega_0 = \sqrt{\omega_1 \omega_2}
$$

# Quality Factor

The "sharpness" of the resonance in a resonant circuit is measured quantitatively by the quality factor $Q$. At resonance, the reactive energy in the circuit oscillates between the inductor and the capacitor. The quality factor relates the maximum or peak energy stored to the energy dissipated in the circuit per cycle of oscillation:
$$
Q = 2\pi\frac{\text{Peak energy stored in the circuit}}{\text{Energy dissipated by the circuit in one period at resonance}}
$$
It is also regarded as a measure of the energy storage property of a circuit in relation to its energy dissipation property. In the series RLC circuit, the peak energy stored is $\frac 12 LI^2$ or $\frac 12 CV^2$, while the energy dissipated in one period is $\frac 12(I^2R) \times T$ where $T = \frac 1{f_0}$
$$
Q = 2 \pi\frac{\frac 12 LI^2}{\frac 12 I_2R(1/f_0)} = \frac{2\pi f_0L}{R}
$$
By plotting, $f_0 = \omega_0 / 2\pi$ 
$$
or,\ Q = \frac{\omega_0 L}{R}
$$
Now we know that, $\omega_0L = \frac{1}{\omega_0 C}$ 
$$
or,\ Q = \frac{\omega_0 L}{R} = \frac 1{\omega_0 CR}
$$

Solving following three equation:
$$
\omega_1 = -\frac R{2L} + \sqrt{\left( \frac{R}{2L} \right)^2 + \frac 1{LC}}
$$
$$
\omega_2 = \frac R{2L} + \sqrt{\left( \frac{R}{2L} \right)^2 + \frac 1{LC}}
$$
$$
B = \omega_2 - \omega_1
$$
We get relationship between the Bandwidth $B$ and the quality factor $Q$,
$$
B = \frac RL = \frac {\omega_0}Q = \omega_0^2CR
$$