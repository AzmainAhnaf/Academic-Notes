
# Superposition Theorem

**The superposition principle states that the voltage across (or current through) an element in a linear circuit is the algebraic sum of the voltage across (or current through) that element due to each independent source acting alone.**

The principle of superposition helps us to analyze a linear circuit with more than one independent source by calculating the contribution of each independent source separately

We must keep two things in mind

1. We consider one independent source at a time while all other independent sources are turned off. This implies that we replace every voltage source by 0 V(or a short circuit), and every current source by 0 A (or an open circuit). This way we obtain a simpler and more manageable circuit.
2. Dependent sources are left intact because they are controlled by circuit variables


**Steps to apply superposition principle:**

1. Turn off all independent sources except one source
2. Find the frequency domain circuit for frequency of the active independent source
3. Find the output (voltage or current) due to that active source using mesh analysis or nodal analysis
4. Repeat step 1 to step 3 for each of the other independent sources.
5. Find the total contribution by adding all the contributions due to each the independent sources in ==time domain==
