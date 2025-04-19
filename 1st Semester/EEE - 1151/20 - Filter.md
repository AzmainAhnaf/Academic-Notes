
There are two types of filter that exists, Active filter and passive filter. For the sake of simplicity, we are just going to discuss about passive filters.

# Low Pass Filter

A typical lowpass filter is formed when the output of an RC circuit is taken off the capacitor as shown in the following figure.
![[Pasted image 20250402105351.png]]
The [[19 - Resonance#Transfer Function|transfer function]]
$H(\omega) = \frac{V_o}{V_i} = \frac{1 / j \omega C}{R + 1 / j \omega C} = \frac{1}{1 + j \omega RC}$
Note that, $H(0) = 1$, $H(\infty) = 0$
![[Pasted image 20250402110843.png]]
$$
H(\omega_c) = \frac 1{\sqrt{1 + \omega_c^2R^2C^2}} = \frac 1 {\sqrt 2}
$$
$$
\Rightarrow \omega_c = \frac 1{RC}
$$
The cutoff frequency is also called the rolloff frequency

A lowpass filter is designed to pass only frequencies from dc up to the cutoff frequency $\omega_c$ 

A lowpass filter can also be formed when the output of an RL circuit is taken off the resistor.


# Highpass Filter

A highpass filter is formed when the output of an RC circuit is taken off the resistor as shown in the following figure.
![[Pasted image 20250402112627.png]]
The [[19 - Resonance#Transfer Function|transfer function]] is,
$$
H(\omega) = \frac {V_o}{V_i} = \frac{R}{R + 1/j \omega C} = \frac{j \omega RC}{1 + j \omega RC}
$$
Note that $H(0) = 0$, $H(\infty) = 1$.
![[Pasted image 20250402112928.png]]
Again, the corner or cutoff frequency would be,
$$
\omega_c = \frac{1}{RC}
$$

A highpass filter is designed to pass all frequencies above its cutoff frequency $\omega_c$

A highpass filter can also be formed when the output of an RL circuit is taken off the inductor


# Bandpass Filter

The RLC series resonant circuit provides a bandpass filter when the output is taken off the resistor as shown in the following figure.
![[Pasted image 20250402114045.png]]
The [[19 - Resonance#Transfer Function|transfer function]] is,
$$
H(\omega) = \frac{V_o}{V_i} = \frac R{R + j(\omega L - 1/\omega C)}
$$
We observe that $H(0) = 0$, $H(\infty) = 0$.
![[Pasted image 20250402114307.png]]
The bandpass filter passes a band of frequencies $(\omega_1 < \omega < \omega_2)$ centered on $\omega_0$, the center frequency, which is given by \([[19 - Resonance#Series Resonance|Learn More!!]])
$$
\omega_0 = \frac{1}{\sqrt{LC}}
$$

# Bandstop Filter

A filter that prevents a band of frequencies between two designated values $(\omega_1$ and $\omega_2)$ from passing is variably known as a bandstop, band-reject, or notch filter. A bandstop filter is formed when the output of an RLC series resonant circuit is taken off the LC series combination as shown in the following figure.
![[Pasted image 20250402120937.png]]
The transfer function is
$$
H(\omega) = \frac{V_o}{V_i} = \frac{j(\omega L - 1 / \omega C)}{R + j(\omega L - 1 / \omega C)}
$$
Here, $H(0)$ = 1, $H(\infty)$ = 1.
![[Pasted image 20250402122403.png]]
Again, the center frequency is given by,
$$
\omega_0 = \frac 1{\sqrt{LC}}
$$
Here, $\omega_0$ is called the frequency of rejection, while the corresponding bandwidth ($B = \omega_2 - \omega_1$) is known as bandwidth of rejection.

A bandstop filter is designed to stop or eliminate all frequencies within a band of frequencies, $\omega_1 < \omega < \omega_2$



