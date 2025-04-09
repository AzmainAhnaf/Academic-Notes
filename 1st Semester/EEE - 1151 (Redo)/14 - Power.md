
# Power

The average power is 
$$
P = \frac 12V_mI_m\cos{(\theta_v - \theta_i)}
$$
$$
P = \frac {V_m}{\sqrt2} \cdot \frac{I_m}{\sqrt2} \cos{(\theta_v - \theta_i)}
$$
$$
P = V_{rms}I_{rms}\cos{(\theta_v - \theta_i)}
$$
Here $\cos{(\theta_v - \theta_i)}$ is called the power factor

The power factor is the cosine of the phase difference between voltage and current

Impedance is
$$
Z = \frac VI = \frac{V_{rms}}{I_{rms}} = \frac{v_{rms}}{i_{rms}}\angle{(\theta_v - \theta_i)}
$$
The power factor is also called the cosine of the angle of the load impedance.

**Apparent Power**:

The apparent power (in VA) is the product of the rms values of voltage and current
$$
S = V_{rms}I_{rms}
$$

Unit: volt-amperes or VA

The power factor is dimensionless, since it is the ratio of the average power to the apparent power.
$$
pf = \frac PS =  \cos{(\theta_v - \theta_i)}
$$


# Complex Power

Complex power absorbed by the AC load is the product of the voltage and the complex conjugate of the current
$$
S = \frac 12VI^*
$$
In terms of RMS value,
$$
S = V_{rms}I^*_{rms}
$$
Where,
$$
V_{rms} = \frac{V}{\sqrt2} = V_{rms}\angle{\theta_v}
$$
$$
I_{rms} = \frac I{\sqrt2} = I_{rms}\angle {\theta_i}
$$
Hence complex power is,
$$
S = V_{rms}I_{rms}\angle{(\theta_v - \theta_i)}
$$
$$
= V_{rms}I_{rms}\cos{(\theta_v - \theta_i)} + jV_{rms}I_{rms}\sin{(\theta_v - \theta_i)}
$$
Real part of the complex power is called real power or average power. Average or real power depends on the load's resistance
$$
P = V_{rms}I_{rms}\cos{(\theta_v - \theta_i)} = I^2_{rms}R
$$
The real power is the average power delivered to a load; it is the only useful power. It is the actual power dissipated by the load.

Unit of real power is watt

Imaginary part of the complex power is called reactive power. Reactive power depends on the load's reactance
$$
Q = V_{rms}I_{rms}\sin{(\theta_v - \theta_i)} = I_{rms}^2X
$$
The reactive power is a measure of the energy exchange between the source and the reactive part of the load.

Energy storage elements (capacitor and inductor) do not dissipate power.

Reactive power is being transferred back and forth between the load and the source

Unit of reactive power is volt-ampere reactive (VAR)

1. $Q = 0$ for resistive loads (unity pf)
2. $Q < 0$ for capacitive loads (leading pf)
3. $Q > 0$ for inductive loads (lagging pf)


Complex power (in VA) is the product of the RMS voltage phasor and the complex conjugate of the RMS current phasor.

Complex power contains all power information of a load. Complex power contains information of real power $P$, reactive power $Q$, apparent power $S$, and power factor $pf$
$$
\text{Complex Power = }S = P + jQ = V_{rms}I^*_{rms} = V_{rms}I_{rms}\angle{(\theta_v - \theta_i)}
$$
$$
\text{Apparent Power = } = s = |S| = V_{rms}I_{rms} = \sqrt{P^2 + Q^2}
$$
$$
\text{Real Power = } Re(S) = P = |S|\cos{(\theta_v - \theta_i)}
$$
$$
\text{Reactive Power = } Im(S) = Q = |S|\sin{(\theta_v - \theta_i)}
$$
$$
\text{Power Factor = } \frac PS = \cos{(\theta_v - \theta_i)}
$$

