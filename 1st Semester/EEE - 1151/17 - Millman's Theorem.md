
Through the application of Millman's theorem, any number of parallel voltage sources can be reduced to one

![[Pasted image 20250402064232.png]]

Firstly, we need to convert each of the voltage source to it's corresponding current source by applying [[6 - Source Transformation|source transformation]]
![[Pasted image 20250402064325.png]]

Then, we need to combine all the parallel current sources.
![[Pasted image 20250402064357.png]]
Where,
	$I_T = I_1 + I_2 + I_3$
	$G_T = G_1+ G_2 + G_3$


Next, we need to convert the resulting current source to a voltage source by using source transformation and that will result in the desired single-source network
![[Pasted image 20250402064548.png]]

$$
E_{eq} = \frac {I_T}{G_T} = \frac{\pm I_1 \pm I_2 \pm I_3 \pm\ ...\ \pm I_N}{G_1 + G_2 + G_3 +\ ...\ G_N}
$$
$$
\therefore E_{eq} = \frac{\pm E_1G_1 \pm E_2G_2 \pm E_3G_3 \pm\ ...\ \pm E_NG_N}{G_1 + G_2 + G_3 +\ ...\ G_N}
$$

The plus-and-minus signs appear in those cases where the sources may not be supplying energy in the same direction.

The equivalent resistance would be,
$$
R_{eq} = \frac{1}{\frac 1{R_1} + \frac 1{R_2} + \frac 1{R_3} +\ ...\ +\frac 1{R_N}}
$$
