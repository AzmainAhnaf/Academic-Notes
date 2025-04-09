

# Mesh Analysis

A mesh is a loop which does not contain any other loops with it.

Mesh analysis provides another general procedure for analyzing circuits.

Mesh currents is used as the circuit variables
![[Pasted image 20250328024714.png]]

**Steps to Determine Mesh Currents**

1. Assign mesh currents $i_1,\ i_2,\ ...\ ...\ ,\ i_n$ to the $n$ meshes
2. Apply [[2 - Law#Kirchhoff's Voltage Law (KVL)|KVL]] to each of the $n$ meshes. Use Ohm's law to express the voltages in terms of mesh currents
3. Solve the resulting $n$ simultaneous equations to get the mesh currents



# Mesh Analysis with Current Sources


When a current source exist only in one mesh, mesh current can be determined directly. Consider the following circuit, we can set $i_2$ = $-5A$ and write a mesh equation for the other mesh in the usual way.
![[Pasted image 20250328025202.png]]

When a current source exists between two meshes, we create a supermesh by excluding the current source and any elements connected in series with it.
![[Pasted image 20250328025241.png]]