

# Practical 2

## Verify Ohm's Law

**State Ohm's Law**
Ohm's Law states that, in constant temperature, the electric current through a conductor between two points is directly proportional to the voltage across the two points
$$
V \propto I
$$

**What is the SI unit of resistance?**
ohm ($\ohm$)

**What are the instruments used to measure voltage, current, and resistance in your setup?**
A voltmeter measures voltage, an ammeter measures current, and a multimeter measures resistance

**Why is the voltmeter connected in parallel and the ammeter in series?**
A voltmeter measures the potential difference across a component, so it must be connected in parallel. An ammeter measures the current flowing through a component, so it must be connected to series.

**What are the internal resistance of an ideal ammeter and voltmeter?**
An ideal ammeter has $0\ \ohm$ resistance and an ideal voltmeter has $\infty \ \ohm$  resistance


# Practical 3

## Verify Kirchhoff's Voltage Law (KVL)

**State KVL**
Kirchhoff's Voltage Law states that the algebraic sums of all voltages around any closed loop in a circuit is zero. mathematically, $\sum V = 0$

**What is the significance of KVL in circuit analysis?**
KVL helps in analyzing complex circuits by providing a relationship between the voltages across different components in a closed loop.

**What does KVL imply about energy conservation in a circuit?**
KVL is based on the principle of conservation of energy, which states that the total energy supplied by the power source is equal to the total energy consumed by the components in the circuit.

**How does KVL apply to circuits with multiple loops?**
In circuits with multiple loops, KVL is applied to each independent loop separately, and the equations are solved simultaneously.



# Practical 4

## Verify Kirchhoff's Current Law (KCL)

**State Kirchhoff's Current Law**
KCL states that the algebraic sum of currents entering and leaving a node (or junction) in circuit is zero. Mathematically, $\sum I_{in} = \sum I_{out}$ 

**What is the significance of KCL in circuit analysis?**
KCL helps in analyzing complex circuits by providing a relationship between the currents at a junction, ensuring charge conservation.

**What does KCL imply about charge conservation in a circuit?**
KCL is based on the principle of conservation of charge, which states that the total charge entering a junction must equal the total charge leaving the junction.




# Practical 5

## Verify Thevenin's Theorem

**State Thevenin's Theorem**
Thevenin's Theorem states that any linear circuit with voltage and current sources and resistances can be replaced by an equivalent circuit consisting of a single voltage source in series with a single resistance

**What is the significance of Thevenin's Theorem in circuit analysis?**
Thevenin's Theorems simplifies complex circuits into a simpler equivalent circuit, making it easier to analyze and calculate the current, voltage, or power in a specific load.

**What is the condition for applying Thevenin's Theorem?**
The circuit must be linear (composed of linear components like resistors, voltage source, and current sources)

**What is a linear circuit?**
A linear circuit is a circuit that follows the law of superposition principle and homogeneity.

**State superposition principle**
In a linear circuit with multiple independent sources, the voltage across or current through any element is equal to the algebraic sum of the voltages or currents produced by each independent source acting alone, while all other independent sources are turned off

**State law of homogeneity**
If the input of a linear circuit is multiplied by a constant factor, the output will also be multiplied by the same constant factor.



# Practical 6

## Verify Maximum Power Transfer Theorem

**State Maximum Power Transfer Theorem**
The Maximum Power Transfer Theorem states that maximum power is transferred from a source to a load when the load resistance is equal to the internal resistance of the source or equal to the Thevenin resistance of the circuit.

**Why is the Maximum Power Transfer Theorem important in practical applications?**
It is crucial in applications like audio amplifiers, communication systems, and impedance matching, where efficient power transfer is required

**What is the efficiency of the circuit at the point of maximum power transfer?**
The efficiency is $50 \%$, as half the power is dissipated in the source resistance

**How to achieve maximum efficiency without caring for maximum power?**
when, $R_L >> R_{Th}$

