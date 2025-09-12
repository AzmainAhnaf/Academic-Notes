
# Semiconductor

**Materials having conductivity in between conductors and insulators are called semiconductor**

Example: $Ge$, $Si$, $GaAs$ etc.
![[Pasted image 20250622231902.png]]

Semiconductors have negative temperature coefficient

## Energy Band Diagram

![[Pasted image 20250622231948.png]]

## Why $Ge$ and $Si$

1. Purification
2. Alterable characteristics
3. Availability


## Classification of Semiconductor

Conductor can be broadly classified as two types. Intrinsic and extrinsic semiconductor.

### Intrinsic Semiconductor
- Semiconductor in its pure form
- Level of purity, $1:10^{10}$ (one in 10 billion)
- Carriers present in such materials is called intrinsic carriers, due to photo-ionization and thermal-ionization
- Bonding of atoms strengthen by the sharing of electrons

### Extrinsic Semiconductor
- Semiconductors subjected to doping process
- Extrinsic semiconductors are of p and n types


## Fermi Level and Fermi Energy

![[Pasted image 20250622233015.png]]

- Fermi level is the highest energy level that an electron can occupy at the absolute zero temperature.
- The Fermi level lies between the valence band and conduction band because at absolute zero temperature, the electrons are all in the lowest energy state.


## n-type Semiconductor

![[Pasted image 20250622233138.png]]

In an n-type material, the electron is called the majority carrier and the hold the minority carrier

- Semiconductors with impurity having five valence electrons (pentavalent atoms) are called n-type semiconductor.
- $Sb$, $As$, $P$ etc. have five valence electrons
- Impurities having five valence electrons are called donor atoms
- Carrier concentration increases to $10^{5}:1$
- $E_g$ becomes $0.005eV$ ($Si$) or $0.01eV$ ($Ge$)
- n-type semiconductors are electrically neutral as there are equal numbers of positive and negative charged carriers
- Fermi level lies close to the conduction band.

![[Pasted image 20250622233439.png]]


## p-type Semiconductor

- Semiconductors with impurity having three valence electrons (trivalent atoms) are called p-type semiconductor.
- $B$, $Ga$, $In$ etc. have three valence electrons
- Impurities having three valence electrons are called acceptor atoms.
- Carrier concentration increases to $10^5:1$ 
- Fermi level lies close to the valence band.

![[Pasted image 20250622233643.png]]

![[Pasted image 20250622233652.png]]



# Ideal Diode and Switch

- A two terminal semiconductor device
- Made up of either $Ge$ or $Si$
- Characteristics similar to an ideal switch
- Conducts current in one direction
- Used as an uncontrolled switch


# P-N Junction Under No Bias

In the absence of an applied bias voltage, the net flow of charge in any one direction for a semiconductor is zero.
![[Pasted image 20250622234113.png]]

![[Pasted image 20250622234223.png]]

- The positive and negative ions (in the depletion region) set up the electric field from positive to negative direction
- These remaining ions (in the depletion region) are immobile and creates a barrier potential which is $0.7V$ for $Si$ and $0.3V$ for $Ge$.



# P-N Junction Under Reverse Bias

![[Pasted image 20250622234520.png]]

- The number of uncovered ions in the depletion region will increase due to the large number of "free" carriers drawn by the applied voltage
- The net effect, there is a widening of the depletion region
- This widening of the depletion region will establish too great a barrier for the majority carriers to overcome effectively reducing the majority carrier flow to zero
- The number of minority carriers in the depletion region will not change, resulting in minority-carrier flow.


# P-N Junction Under Forward Bias

![[Pasted image 20250622234716.png]]

- Reduce the width of the depletion region
- Reduction in the width of the depletion region results in a heavy majority flow across the junction.


# Diode Equation and Characteristics

![[Pasted image 20250622234953.png]]

Here, 
$I_s$ = Reverse Saturation Current

![[Pasted image 20250622235000.png]]

- There is a point where the application of too negative a voltage with a reverse polarity will result in a sharp change in the characteristics: the current increases at a very rapid rate in a direction opposite of that of + voltage region
- The amount of - voltage responsible for the situation is called breakdown/Zener voltage


# Avalanche and Zener Mechanism

- With increase in the reverse voltage, the velocity of the minority carriers responsible for the reverse saturation current $I_S$ also increases. When the kinetic energy of the carriers sufficient (at $V_Z$) t release additional carriers through collisions with other atoms. That is called impact ionization.

# Effect of Temperature

![[Pasted image 20250622235549.png]]


# Zener Diode

- Zener diodes are specially designed diodes.
![[Pasted image 20250622235627.png]]

- Used as a voltage regulator
- Act as a protection device
- It is used to establish reference voltage level


## Zener Diode i-v characteristic

![[Pasted image 20250622235711.png]]


# PIV or PRV

- Peak Inverse Voltage or Peak Reverse Voltage
- The maximum reverse-bias potential that can be applied before entering the Zener region
- PIV or PRV should be slightly less than $V_Z$
- Where, $V_Z$ is the breakdown or Zener Potential.


# Diode Models

1. Piecewise-linear model
2. Simplified model
3. Ideal Model

![[Pasted image 20250623000003.png]]

# Transition and Diffusion Capacitance

![[Pasted image 20250623000525.png]]

 - The transition capacitance is the predominant capacitive effect in the reverse bias region
 - The diffusion capacitance is the predominant capacitive effect in the forward bias region

# Reverse Recovery Time

- When a FB diode is switch to RB, state of carrier change
- This large number of minority carrier results in a large reverse current until the carriers come back to their original majority state