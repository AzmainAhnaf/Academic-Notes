
$$
\int x^ndx = \frac{x^{n + 1}}{n + 1} + c
$$
$$
\int e^xdx = e^x + c
$$
$$
\int sinxdx = -cosx + c
$$

# Method of Substitution

$$
\int \frac{\sin^{-1}x}{\sqrt{1 - x^2}}dx
$$
Let, $sin^{-1}x = z$  $\therefore \frac{dx}{\sqrt{1 - x^2}} = dx$ 
Substituting we get
$$
\int zdz = \frac {z^2}2 + c = \frac{(sin^{-1}x)^2}2 + c
$$

Similarly by substituting we can get the following formulas
$$
\int \frac{dx}{a^2 - x^2} = \frac 1{2a}ln \left| \frac{a + x}{a - x} \right| + c
$$
$$
\int \frac{dx}{x^2 - a^2} = \frac 1{2a}ln \left| \frac{x - a}{x + a} \right| + c
$$
$$
\int \sqrt{a^2 - x^2}dx = \frac x2\sqrt{a^2 - x^2} + \frac {a^2}2 \sin^{-1}\frac xa + c
$$
$$
\int \sqrt{x^2 - a^2}dx = \frac x2 \sqrt{x^2 - a^2} + \frac {a^2}2ln \left| x + \sqrt{x^2 - a^2} \right| + c
$$


# Integration by Parts

if $u$ and $v$ both is a function of $x$ then
$$
\int uvdx = u\int vdx - \int \left\{ \frac {du}{dx}\int vdx \right\}dx
$$


# Partial Fraction

$$
\frac {x^2}{(x - 2)(x - 3)(x + 4)} = \frac A{x - 2} + \frac B{x - 3} + \frac C{x + 4}
$$

$$
\frac {x^2}{(x - 2)(x - 3)^2} = \frac A{x - 2} + \frac B{x - 3} + \frac C{(x - 3)^2}
$$

