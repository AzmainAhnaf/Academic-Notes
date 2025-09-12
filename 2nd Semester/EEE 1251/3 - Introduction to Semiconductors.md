
# Rectification

- AC signals have zero average or DC value
- To create DC level, rectification is necessary
	![[Pasted image 20250718042637.png]]
- Rectifiers are of two types, half wave and full wave rectifiers

# Half Wave Rectification

![[Pasted image 20250718042714.png]]
![[Pasted image 20250718042834.png]]
![[Pasted image 20250718042848.png]]
![[Pasted image 20250718042858.png]]

# DC Output

Average or DC value of a signal is
$$
V_{dc} = \frac 1T \int_0^TV_m\sin{t}dt
$$
For half wave rectifier,
$$
V_{dc} = \frac1T \left[ \int_0^{\frac T2}V_m\sin{t}dt + \int_{\frac T2}^T 0dt \right]
$$
$$
= \frac{V_m}\pi = 0.318V_m
$$
For practical diode,
$$
V_{dc} \cong 0.318(V_m - V_T)
$$

# Full Wave Bridge Rectifier

![[Pasted image 20250718043233.png]]
![[Pasted image 20250718043244.png]]

DC output would twice as that of a half wave rectifier
$$
V_{dc} = \frac{2V_m}\pi = 0.636V_m
$$

# Center-tap Transformer Rectifier

![[Pasted image 20250718043422.png]]
![[Pasted image 20250718043434.png]]


# Peak Inverse Voltage of a Diode

PIV, or Peak Inverse Voltage, refers to the maximum reverse voltage that a diode can withstand without being damaged.


# Oscilloscope Display

![[Pasted image 20250718043712.png]]


# Half Wave Rectifier with Capacitor Filter
![[Pasted image 20250718043737.png]]


# Full Wave Rectifier with Capacitor Filter

![[Pasted image 20250718043803.png]]



# Efficiency (not clear will complete later)

$$
\text{Efficiency}(\eta) = \frac{\text{DC Output Power}}{\text{AC Input Power}}
$$
$$
\text{DC Ootput Ppower of HWR} = V_oI_o = (I_o)^2R_L
$$


# Ripple Factor

The ripple factor for a half-wave rectifier is 1.21

This value indicates the degree of AC ripple present in the rectified output, with a higher value suggesting greater AC content

The ripple factor of a full-wave rectifier is 0.48

This value is a measure of the amount of AC ripple or fluctuations present in the DC output of a rectifier circuit

A lower ripple factor indicates a cleaner, more stable DC output.