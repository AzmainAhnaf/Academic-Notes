
# Sinusoids

- A sinusoid is a signal the form of the since or cosine function
- A sinusoidal signal is easy to generate and transmit
- Sinusoidal voltage generated through out the world and supplied to homes, factories, laboratories, and so on.

Consider the sinusoidal $v(t) = V_M\sin{(\omega t)}$ 
Where,
	$V_M$ = the amplitude of the sinusoid
	$\omega$ = the angular frequency in radians/s

![[Pasted image 20250331211850.png]]

$T$ = Time period of the sinusoid
$$
T = \frac {2\pi}{\omega}
$$
$v(t)$ repeats itself every $T$ seconds
$$
v(t + T) = V_m\sin{\omega(t + T)}
$$
$$
= V_m\sin{\omega \left(t + \frac{2\pi}{\omega}\right)}
$$
$$
= V_m\sin{(\omega t + 2\pi)}
$$
$$
= V_m\sin{\omega t}
$$
$$
= v(t)
$$
$$
\therefore v(t + T) = v(t)
$$

A periodic function is one that satisfied $f(t) = f(t + nT)$, for all $t$ and all integers $n$.

Time period $T$ of the periodic function is the time of one complete cycle
![[Pasted image 20250401011916.png]]
$$
\omega T = 2\pi
$$
$$
T = \frac{2\pi}{\omega}
$$
The number of cycles per second, known as the frequency $f$
$$
f = \frac 1T
$$
Unit of $f$ is hertz (Hz)

Expression for the sinusoid
$$
v(t) = V_m\sin{(\omega t + \phi)}
$$
Where, 
	$\phi$ is the phase
$$
\omega t + \phi = 0
$$
$$
\omega t = -\phi
$$
"-" sign indicate signal start from the left side of origin
![[Pasted image 20250401012634.png]]

Likewise, "+" sign indicate signal start from the right side of origin and if $\omega t = 0$ then signal start from origin.

A sinusoid can be expressed in either sine or cosine form. For example,
$$
v_2 = 12\sin{(\omega t - 10 \degree)} = 12\cos{(\omega t - 100 \degree)}
$$
When comparing two sinusoids, both sinusoids is expressed as either sine or cosine with positive amplitudes.

Sine to cosine conversion or vice versa are achieved by using the following trigonometric formula
$$
\sin{(\omega t \pm 180 \degree)} = -\sin{(\omega t)}
$$
$$
\cos{(\omega t \pm 180 \degree)} = -\cos{(\omega t)}
$$
$$
\sin{(\omega t \pm 90 \degree)} = \pm \cos{(\omega t)}
$$
$$
\cos{(\omega t \pm 90 \degree)} = \mp \sin{(\omega t)}
$$

## Phase Angles

Consider the following two equations
$$
v_1 = 10\sin{(\omega t - 40 \degree)}
$$
$$
v_2 = 12\sin{(\omega t - 10 \degree)}
$$
Phase angle between $v_1$ and $v_2$ = phase angle of $v_1$ - phase angle of $v_2$ = $(-40 \degree) - (-10 \degree)$ = $-30 \degree$

As the sign is negative, it means that $v_1$ lags $v_2$ by $30 \degree$ or vice versa which is $v_2$ leads $v_1$ by $30 \degree$
![[Pasted image 20250401062933.png]]



# Phasors

- Sinusoids are easily expressed in terms of phasors
- Phasors are more convenient to work with than sine and cosine functions
- A phasor is a complex number that represents the amplitude and phase of a sinusoid
- Phasors provide a simple means of analyzing linear circuits excited by sinusoidal sources
- A complex number $z$ can be written in rectangular form as
$$
z = x + jy
$$
Where $j = \sqrt{-1}$; $x$ is the real part of $z$; $y$ is the imaginary part of $z$ 
$z$ can be represented in three ways
1. Rectangular form
$$
z = x + jy
$$
2. Polar form
$$
z = r\angle(\phi)
$$
3. Exponential form
$$
z = re^{j\phi}
$$

Where, $r$ is the magnitude of $z$, and $\phi$ is the phase of $z$

The relationship between the rectangular form and the polar form is shown in following figure
![[Pasted image 20250401063642.png|300]]

We can get $r$ and $\phi$ as
$$
r = \sqrt{x^2 + y^2}
$$
$$
\phi = \tan^{-1}{(\frac yx)}
$$
We can obtain $x$ and $y$ as
$$
x = r\cos \phi
$$
$$
y = r \sin \phi
$$

Complex number $z$ may be written as
$$
z = x + jy = r \angle(\phi) = r(\cos \phi + j \sin \phi)
$$

Addition and subtraction of complex numbers are better performed in rectangular form
$$
z_1 = x_1 + jy_1
$$
$$
z_2 = x_2 + jy_2
$$
Addition:
$$
z_1 + z_2 = (x_1 + x_2) + j(y_1 + y_2)
$$
Subtraction:
$$
z_1 - z_2 = (x_1 - x_2) + j(y_1 - y_2)
$$

Multiplication and division of complex numbers are better done in polar form
$$
z_1 = r_1\angle{(\phi_1)}
$$
$$
z_2 = r_2\angle{(\phi_2)}
$$
Multiplication:
$$
z_1z_2 = r_1r_2\angle{(\phi_1 + \phi_2)}
$$
Division:
$$
\frac {z_1}{z_2} = \frac {r_1}{r_2}\angle{(\phi_1 - \phi_2)}
$$

Reciprocal:
$$
\frac 1z = \frac 1r \angle{(-\phi)}
$$
Square Root:
$$
\sqrt{z} = \sqrt{r}\angle{(\phi / 2)}
$$
Complex Conjugate:
$$
z^* = x - jy = r\angle{(-\phi)}
$$
$$
\frac 1j = -j
$$

Time Domain vs phasor domain:
$$
\frac{dv}{dt} \Leftrightarrow j\omega V
$$
$$
\int vdt \Leftrightarrow \frac{V}{j\omega}
$$
$$
v(t) = V_m\cos{(\omega t + \phi)} \Leftrightarrow V = V_m\angle{\phi}
$$
Before representing in phasor domain we make our sinusoidal function to cosine.
![[Pasted image 20250401065544.png]]

![[Pasted image 20250401065917.png]]

