
# Some Properties of Definite Integral

$$
\int_a^b f(x)dx = \int_a^bf(z)dz
$$
$$
\int_a^bf(x)dx = -\int_b^af(x)dx
$$
$$
\int_a^bf(x)dx = \int_a^cf(x)dx + \int_c^bf(x)dx, \text{ if},\ a < c < b
$$
$$
\int_0^af(x)dx = \int_0^af(a - x)dx
$$
$$
\int_0^{na} f(x)dx = n\int_0^af(x)dx,\ \text{if}\ f(a + x) = f(x)
$$
$$
\int_{-a}^af(x)dx = 2\int_0^af(x)dx,\ \text{if}\ f(-x) = f(x)\ or,\ = 0,\ \text{if}\ f(-x) = -f(x)
$$


# Walli's Formula

**Statement**:

If $n$ be positive integer
$$
\int_0^{\frac \pi 2} \sin ^n xdx = \int_0^{\frac \pi 2} \cos ^ndx 
$$
If $n$ is even
$$
= \frac{n - 1}n \cdot \frac{n - 3}{n - 2}\cdot\frac{n - 5}{n - 4}\ ...\ \frac 34 \cdot \frac 12 \cdot \frac \pi 2
$$
If $n$ is odd
$$
= \frac{n - 1}n \cdot \frac{n - 3}{n - 2}\cdot\frac{n - 5}{n - 4}\ ...\ \frac 45 \cdot \frac 23 \cdot 1
$$

**Proof**:

Let,
$$
I_n = \int \sin ^n dx = \int \sin ^{n - 1}x\ \sin xdx
$$
$$
= \sin ^{n - 1}x(-\cos x) + (n - 1)\int \sin^{n - 2}x\ \cos^2xdx
$$
$$
= -\sin^{n - 1}x\cos x + (n - 1)\int \sin^{n - 2}x - (n - 1) \int \sin^nxdx
$$
$$
= -\sin^{n - 1}x\cos x + (n - 1)\int \sin^{n - 2}x - (n - 1)I_n
$$
$$
\Rightarrow nI_n = -\sin^{n - 1}x\cos x + (n - 1)\int \sin^{n - 2}x
$$
Applying limit $0\ to\ \frac \pi 2$
$$
I_n = \left[ \frac{-\sin^{n - 1}x\cos x}{n} \right]_0^\frac \pi 2 + \frac {n - 1}n \int_0^{\frac \pi 2}\sin^{n - 2}xdx
$$
$$
I_n = \frac {n - 1}n I_{n - 2}
$$
Similarly if we proceed we get
$$
I_n = \frac{n - 1}n \cdot \frac{n - 3}{n - 2}\cdot\frac{n - 5}{n - 4}\ ...\ \frac 34 \cdot \frac 12 \cdot I_0
$$
$$
I_n = \frac{n - 1}n \cdot \frac{n - 3}{n - 2}\cdot\frac{n - 5}{n - 4}\ ...\ \frac 45 \cdot \frac 23 \cdot I_1
$$
according as $n$ is even or odd
$$
I_0 = \int_0^{\frac \pi 2}dx = \left[x\right]_0^{\frac \pi 2} = \frac \pi 2
$$
$$
I_1 = \int_0^{\frac \pi 2}\sin xdx = \left[ - \cos x\right]_0^{\frac \pi 2} = 1
$$
Hence Walli's Theorem is proved

**Theorem**: $\int_0^{\frac \pi 2} \sin^m x \cos^n xdx$ 

$(i)$ If both $m$ and $n$ are even
$$
\int_0^{\frac \pi 2} \sin^m x \cos^n xdx = \frac{(m - 1)\cdot (m - 3)...3\cdot 1\cdot (n - 1) \cdot (n - 3)...3\cdot 1}{(m + n)(m + n - 2)...6\cdot 4\cdot 2} \cdot \frac \pi 2
$$

$(ii)$ if $m$ is even $n$ is odd
$$
\int_0^{\frac \pi 2} \sin^m x \cos^n xdx = \frac{(m-1)(m-3)...3 \cdot 1(n - 1)(n - 3)...\cdot4\cdot2}{(m + n)(m + n - 2)...5\cdot3\cdot1}\cdot1
$$

$(iii)$ If both $m$ and $n$ are odd
$$
\int_0^{\frac \pi 2} \sin^m x \cos^n xdx = \frac{(m-1)(m-3)...4 \cdot 2(n - 1)(n - 3)...\cdot4\cdot2}{(m + n)(m + n - 2)...6\cdot4\cdot2}\cdot \frac 12
$$
