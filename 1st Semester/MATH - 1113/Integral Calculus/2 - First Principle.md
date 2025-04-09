

![[Pasted image 20250316175127.png]]

Area of region by the curve $f(x)$ with the $x$-axis bounded by $x = a$ and $x = b$ is
$$
\lim_{h \to 0} \left[ hf(a) + hf(a + h) + hf(a + 2h) +\ ...\ + hf(a + (n - 1)h) \right]
$$
$$
\Rightarrow \lim_{h \to 0}\ h\sum_{r = 0}^{n - 1}f(a + rh)
$$
Putting $h = \frac {b - a}n$. When $h \to 0$ then $n \to \infty$
$$
\lim_{n \to \infty} \frac {b - a}n \sum_{r = 0}^{n - 1}f(a + r \frac{b - a}n)
$$
Formally,
$$
\int_a^b f(x)dx = \lim_{h \to 0}\ h\sum_{r = 0}^{n - 1}f(a + rh) = \lim_{n \to \infty}\ \frac{b - a}n \sum_{r = 0}^{n - 1}f(a + r \frac{b - a}n)
$$
if $a = 0$ and $b = 1$ then
$$
\int_0^1 f(x)dx = \lim_{h \to 0}\ h\sum_{r = 0}^{n - 1}f(rh) = \lim_{n \to \infty}\ \frac 1n \sum_{r = 0}^{n - 1}f(\frac rn)
$$


$$
a + ar + ar^2 + ar^3\ +\ ...\ ...\ + ar^{n - 1}
$$
if $r > 0$ then
$$
sum = \frac {a(r^n - 1)}{r - 1}
$$
If $r < 0$ then
$$
sum = \frac {a(1 - r^n)}{1- r}
$$
