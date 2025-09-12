

**Conditions**
- Periodic meaning time period same
- Amplitude same
- Restoring force is always directed towards the main or equilibrium position.

![[Pasted image 20250706112131.png]]

If all the conditions are fulfilled, then the motion will be considered as simple harmonic motion.



## Derivation
![[Pasted image 20250706113032.png]]

$$
F \propto y
$$
$$
\Rightarrow F = -ky
$$
$$
F = m \frac{d^2y}{dt^2}
$$
$$
\therefore m \frac{d^2y}{dt^2} + ky = 0
$$
$$
\Rightarrow \frac{d^2y}{dt^2} + \frac km y = 0
$$
$$
\Rightarrow \frac{d^2y}{dt^2} + \omega^2 = 0 \ \ \ \ , \omega = \sqrt{\frac km}
$$
Here,
	$\omega$ = Angular Velocity

The equation is a second order linear homogeneous equation.

This is the differential equation of simple harmonic motion

Solving the equation of simple harmonic motion

$$
\frac{d^2y}{dt^2} = -\omega^2y
$$
Multiplying both sides by $2 \frac{dy}{dt}$
$$
2 \cdot \frac{dy}{dt} \cdot \frac{d^2y}{dt^2} = -\omega^2y \cdot2\cdot \frac{dy}{dt}
$$
$$
\text{or, } 2 \cdot \frac{dy}{dt} \cdot \frac{d^2y}{dt^2} = -\omega^2 \cdot2\cdot \frac{dy}{dt}\cdot y
$$
Integrating with respect to time, we have
$$
\left( \frac{dy}{dt} \right)^2 = -\omega^2y^2 + C
$$
Where, $C$ is the constant of integration.

Velocity is $0$ when displacement is maximum
Therefore, when $y = a$(amplitude), $\frac{dy}{dt} = 0$

Substituting for these values we get

$$
0 = -\omega^2a^2 + C
$$
$$
\text{or, } C = \omega^2a^2
$$

Again substituting the value of $C$ we get

$$
\left(\frac{dy}{dt}\right)^2 = -\omega^2y^2 + \omega^2a^2 = \omega^2(a^2 - y^2)
$$
$$
\text{or, } \frac{dy}{dt} = v = \pm\omega\sqrt{a^2 - y^2} = \pm\sqrt{\frac km}\sqrt{a^2 - y^2}
$$

This equation can be rearranged as

$$
\frac{dy}{\sqrt{a^2 - y^2}} = \omega \cdot dt
$$
Integrating the equation we get,
$$
\sin ^{-1} \frac{y}{a} = \omega t + \phi
$$
$$
\therefore y = a\sin{(\omega t + \phi)}
$$

This is the solution of differential equation of harmonic motion.

If we plot $t$ at x axis and $y$ at y axis, we get.

![[Pasted image 20250706120645.png]]

if we further deconstruct the equation

$$
y = a\sin{(\omega t + \phi)}
$$
$$
\Rightarrow y = a\sin{\omega t}\cos{\phi} + a\cos{\omega t}\sin{\phi}
$$
$$
= A\sin{\omega t} + B\cos{\omega t}
$$

In special cases either $A$ or $B$ maybe $0$
$$
y_1 = A\sin{\omega t}
$$
$$
y_2 = B\cos{\omega t}
$$
$y = y_1 + y_2$ satisfies the differential equation

There is an another form of the equation'
$$
y(t) = \text{Real}(Ae^{i(\omega t + \phi)}) = \text{Real}(A\cos{(\omega t + \phi)} + if(t))
$$
$$
f(t) =A\sin{(\omega t + \phi)}
$$
here $f(t)$ is a real function. if $f(t)$ is arbitrary, plotting the $y(t)$ we will fund that the locus will be mysterious

If $f(t)$ is confined that is a periodic and real function, the locus will be a circle.

![[Pasted image 20250706122950.png]]

The projection will rotate across the circumference. Here we get two simple harmonic motion simply by the particles rotating around the circumference, one is across the x-axis, other is across the y-axis. combining these two we get our main equation $y = y_1 + y_2$ 

Let,
$$
y = e^{mt}
$$
$$
y' = me^{mt}
$$
$$
y'' = m^2 e^{mt}
$$
$$
y'' + \omega^2 y = 0
$$
$$
\Rightarrow (m^2 + \omega ^2)e^{mt} = 0
$$

Here, $e^{mt}$ cannot be $0$

$$
\therefore m^2 + \omega^2 = 0
$$$$
\Rightarrow m = \pm i\omega
$$

The two solutions are,
$$
y_1 = Ae^{i \omega t}
$$
$$
y_2 = Be^{-i\omega t}
$$
Both are the solution of the differential equation of SHM

Now differentiating the resultant with respect to $\omega t$ won't change the result at all. This is the simple harmonic motion characteristic. This cannot be killed by differentiation. So, it is compared to the phoenix bird. 


# Generalized Equation

The generalized equation for SHM is
$$
y = A\sin{\omega t} + B\cos{\omega t}
$$
$$
y_1 = A\sin{\omega t}
$$
$$
y_2 = B\cos{\omega t}
$$
$$
y = Ae^{\pm i\omega t}
$$
![[Pasted image 20250706133601.png]]


# Examples of SHM

Examples of SHM can be spring, AC circuit, atomic vibration, electromagnetic wave ($\overrightarrow{E}$ and $\overrightarrow{H}$), motion of piston in gas chamber, motion of mercury in U-tube


## Simple Pendulum

![[Pasted image 20250706134434.png]]

Restoring force here is $mg\sin{\theta}$ which is the only effective component. If $\theta$ is small so it can be written as $mg \theta$. As it is a restoring force, there will be a negative sign

Linear Displacement,
$$
y = l \sin \theta = l \theta
$$
$$
\dot{y} = l \frac{d \theta}{dt}
$$
$$
\ddot{y} = l \frac{d ^2 \theta}{dt^2}
$$

$$
m\ddot{y} = m \overrightarrow{a} = ml \frac{d ^2 \theta}{dt^2}
$$

From Newton's second law of motion,
$$
ml \frac{d ^2 \theta}{dt^2} = -mg \theta
$$
$$
\Rightarrow \frac{d ^2 \theta}{dt^2} + \frac gl \theta= 0
$$
$$
\Rightarrow \frac{d ^2 \theta}{dt^2} + \omega ^2 \theta= 0
$$
$$
\omega = \sqrt{\frac gl}
$$

This equation looks very similar to the differential equation of SHM (as it is one lol)

Solution of the equation is,
$$
\theta = \theta _r \sin{(\omega t + \phi)}
$$

This indicates that the motion is oscillatory


## LC Circuit

![[Pasted image 20250706140211.png]]

![[Pasted image 20250706140238.png]]

At first capacitor will be charged by disconnecting the inductor and connecting the batter and later on it will be discharged.

![[Pasted image 20250706140315.png]]

The LC circuit will continue to charge and discharge.

If the charge is $Q$, the voltage across capacitor,
$$
V = \frac QC
$$
The emf developed in the inductor due to the change of current through it will be,
$$
E = L \frac{di}{dt}
$$
Considering it a mechanical hindrance, there will be a negative sign

$$
\frac QC = -L \frac{di}{dt}
$$
$$
\Rightarrow L\frac{d^2 Q}{dt^2} + \frac QC = 0
$$
We can get this by applying KVL too,
$$
L \frac{di}{dt} + V = 0
$$
$$
\frac{d^2Q}{dt^2} + \frac Q{LC} = 0
$$
$$
\frac{d^2Q}{dt^2} + \omega ^2Q = 0
$$
$$
\omega^2 = \frac 1{LC}
$$

this equation is the equation of the motion of charge between the capacitor and the inductor which is very similar to the equation of SHM (Because it is the equation of SHM LMAO)

So, we can say that the motion of the charge in an ideal (DC resistance = 0) LC circuit is a SHM

Solution of the equation will be
$$
Q = Q_o\sin{(\omega t + \phi)}
$$

![[Pasted image 20250706141302.png]]

The nature of the motion of the charge, current and voltage will be oscillatory.

If the circuit is not ideal, then the motion will be oscillatory but the amplitude will be 0 after a period of time, the equation,
$$
\frac{d^2Q}{dt^2} + \omega ^2Q + iR= 0
$$
![[Pasted image 20250706141409.png]]

For non-conservative force affecting the system, we have to add all of them to the SHM equation.


# Energy of SHM
(In the absence of any non-conservative force)

The total energy of a harmonic oscillator will be the sum of kinetic and potential energy

$$
E = K.E. + P.E.
$$
$$
= \frac 12 mv^2 + P.E.
$$
$$
= \frac 12m \{a \omega \cos{(\omega t + \phi)}\}^2 + \frac 12 ky^2
$$
$$
= \frac 12 m a^2 \omega ^2 \cos ^2 (\omega t + \phi) + \frac 12 ka^2 \sin ^2 (\omega t + \phi)
$$
$$
= \frac 12 ka^2 [\sin ^2 (\omega t + \phi) + \cos ^2 (\omega t + \phi)]
$$
$$
= \frac 12 ka^2 = \frac 12 m\omega^2a^2 = 2 \pi ^2 n^2 a^2 m
$$
where,
	$n$ = frequency

The graph of energy will be like this

![[Pasted image 20250706142719.png]]
Energy vs displacement

Average kinetic energy
$$
K.E. = \frac 1T \int_{0}^{T}\frac 12mv^2dt = \frac 14 ka^2
$$
Average potential energy
$$
P.E. = \frac 1T \int_0^TP.E. dt = \frac 14ka^2
$$



# Composition of Simple Harmonic Motion

Two simple harmonic motion acting simultaneously in a straight line.
The two SHM's are,
$$
y_1 = a_1\sin{(\omega t + \alpha _1)} = a_1(\sin \omega t \cos \alpha _1 + \cos \omega t\sin \alpha _1)
$$
$$
y_2 = a_2\sin{(\omega t + \alpha _2)} = a_2(\sin \omega t \cos \alpha_2 + \cos \omega \sin \alpha_2 )
$$

The resultant motion will be vector sum of individual displacement

$$
y = y_1 + y_2
$$
$$
= (a_1\cos \alpha_1 + a_2\cos \alpha_2)\sin \omega t + (a_1 \sin \alpha_1 + a_2 \sin \alpha_2)\cos \omega t
$$
Let,
$$
A\cos \phi = (a_1\cos \alpha_1 + a_2\cos \alpha_2)
$$
$$
A\sin\phi = (a_1 \sin \alpha_1 + a_2 \sin \alpha_2)
$$

Resultant motion will be
$$
y = A\sin{(\omega t + \phi)}
$$
which is SHM motion so the nation of the motion will be oscillatory, however the amplitude will be different.

$$
A = \sqrt{a_1^2 + a_2^2 + 2a_1a_2\cos{(\alpha_1 - \alpha_2)}}
$$

if $\alpha_1 = \alpha_2 = \alpha$, that means two vibrations in same phase then,
$$
A = a_1 + a_2
$$
if $\alpha_1 - \alpha_2 = (2n + 1)\pi$, then
$$
A = a_1 - a_2
$$
![[Pasted image 20250706163930.png]]


## Composition of Two Perpendicular SHM Motion

Let,
$$
x = a\sin(\omega t + \phi)
$$
$$
y = b \sin \omega t
$$
$$
\therefore \frac xa = \sin \omega t \cos \phi + \cos \omega t \sin \phi
$$
$$
\therefore \frac yb = \sin \omega t
$$
Plotting values of $\frac yb$ in the equation of $\frac xa$
$$
\frac xa = \frac yb \cos \phi + \sqrt{1 - \frac{y^2}{b^2}}\sin \phi
$$
$$
\left( \frac xa - \frac yb\cos\phi \right)^2 = \left( 1 - \frac{y^2}{b^2} \right)\sin^2\phi
$$
$$
\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{2xy}{ab}\cos\phi = \sin ^2 \phi
$$
The equation is a general equation of conic. The shape will depend upon $\phi$, $a$ and $b$. The waveform mapped in oscilloscope of such two simple harmonic motion is called Lissajous figures 

If,
	$phi$ = $0, 2\pi, 4\pi, \dots, 2n\pi$ 
then,
$$
\left( \frac xa - \frac yb \right)^2 = 0
$$
$$
\Rightarrow y = \pm \frac bax
$$
It represents the equation of a pair of coincident straight lines passing through the origin.

If two SHM phased perpendicularly act simultaneously on a particle then the resultant motion will trace some figures. These figure is called Lissajous Figure.

![[Pasted image 20250706221624.png]]

Angle of inclination will be $45 \degree$ when $a = b$


If,
	$\phi = \pi$ 
then,
$$
y = \mp \frac ba x
$$
![[Pasted image 20250706222225.png]]

if,
	$\phi$ = $\frac \pi 2$ 
Then,
$$
\frac {x^2}{a^2} + \frac{y^2}{b^2} = 1
$$
Equation of a symmetrical ellipse. If $a = b$, then it will be an equation of circle

![[Pasted image 20250706222342.png]]


Again let,
$$
x = a\sin{(2 \omega t + \phi)}
$$
$$
y = b\sin{\omega t}
$$
Here, time period in the ratio of $\frac 12$
$$
\frac yb = \sin{\omega t}
$$
$$
\frac xa = \sin2 \omega t \cos\phi + \cos 2 \omega t \sin \phi
$$
$$
= 2 \sin \omega t \cos \omega t \cos \phi = (1 - 2 \sin^2 \omega t)\sin \phi
$$
$$
\frac xa = 2\frac yb \sqrt{1 - \frac {y^2}{b^2}} \cos \phi + \left( 1 - 2 \frac{y^2}{b^2} \right)\sin \phi
$$
$$
\Rightarrow \left( \frac xa - \sin \phi\right)^2 + \frac{4y^4}{b^4}\sin^2 \phi + 2\left( \frac xa - \sin \phi \right)\cdot2\frac{y^2}{b^2}\sin^2\phi = \frac{4y^2}{b^2} \cos^2\phi 
$$

The equation is unclear as of now, khatai kore pore dekhbo

Final equation.

![[Pasted image 20250706224721.png]]

This is the equation of a curve having two loops.

When $\phi = 0$
$$
\frac{x^2}{a^2} + \frac{y^2}{b^2}\left( \frac{y^2}{b^2} - 1\right) = 0
$$

It will display the figure of eight.

![[Pasted image 20250706224824.png]]


if $\phi = \frac \pi 2$ 
then,
$$
y^2 = -\frac{b^2}{2a}(x-a)
$$
![[Pasted image 20250706224907.png]]
