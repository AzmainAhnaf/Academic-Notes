
# Expansion of Functions

**State Rolle's Theorem**
If,
- $(i)$ $f(x)$ is continuous in the closed interval $a \le x \le b$ or, $x \in [a, b]$ 
- $(ii)$ $f'(x)$ exists in the open interval $a < x < b$ or, $x \in (a, b)$
- $(iii)$ $f(a) = f(b)$, then
there exists at least one value of $x$ (say $k$) between $a$ and $b$ such that $f'(k) = 0$.


**State Mean Value Theorem**
If,
- $(i)$ $f(x)$ is continuous in the closed interval $a \le x \le b$ or, $x \in [a, b]$
- $(ii)$ $f'(x)$ exists in the open interval $a < x < b$ or, $x \in (a, b)$,
then there exists at least one value $x$ (say $k$) between $a$ and $b$ such that $f(b) - f(a) = (b - a)f'(k)$


**State Taylor's Series in Finite Form / Generalized Mean Value Theorem**
If $f^{n - 1}(x)$ is continuous in $[a, b]$  and $f^n(x)$ exists in $(a, b)$ then
$$
f(b) = f(a) + (b - a)f'(a) + \frac{(b - a)^2}{2!}f''(a) + \ldots + \frac{(b - a)^{n - 1}}{(n - 1)!}f^{n - 1}(a) + \frac{(b - a)^n}{n!}f^n(k)
$$
and if $b = a + h$ so that $b - a = h$ then
$$
f(a + h) = f(a) + hf'(a) + \frac{h^2}{2!}f''(a) + \ldots + \frac{h^{n - 1}}{(n - 1)!}f^{n - 1}(a) + \frac{h^n}{n!}f(a + \theta h)
$$
where $\theta \in (0, 1)$, now replacing $x$ for $a$ then we obtain 
$$
f(x + h) = f(x) + hf'(x) + \frac{h^2}{2!}f''(x) + \ldots + \frac{h^{n - 1}}{(n - 1)!}f^{n - 1}(x) + \frac{h^n}{n!}f(x + \theta h)
$$

The above mentioned 3 series are also called Taylor's series with remainder in Lagrange's form, the remainder being $\frac{(b - a)^n}{n!}f^n(k)$ or, $\frac{h^n}{n!}f^n(x + \theta h)$ which is generally denoted by $R_n$

If we put $n=1$ in Taylor's Series we will get the equation for Mean Value Theorem $f(b) - f(a) = (b - a)f'(k)$ 

Again putting $x = 0$ and $h = x$ in Taylor's series we get Maclaurin's series for $f(x)$ i.e.,
$$
f(x) = f(0) + xf'(0) + \frac{x^2}{2!}f''(0) + \ldots + \frac{x^{n - 1}}{(n - 1)!}f^{n - 1}(0) + \frac{x^n}{n!}f^n(\theta x)
$$


# Maxima and Minima

**Define Maxima and Minima**
A function $f(x)$ is said to be maxima or, minima at $x = a$ if its value is greater or, less than any other neighboring values of the function.

**Define Points of Inflexion**
The point at which a function have neither a maximum value nor a minimum values are called the point of inflexion


# Partial Differentiation


**Define Homogeneous Function**
A function $f(x, y)$ is said to be homogeneous of degree $n$ in the variables $x$ and $y$ if it can be expressed in the form $x^n \phi \left( \frac yx \right)$ or in the form $y^n \phi \left( \frac xy \right)$.

**State Euler's Theorem on Homogeneous Function**
If $f(x, y)$ be a homogeneous function of $x$ and $y$ of degree $n$ then $x \frac {\partial f}{\partial x} + y \frac{\partial f}{\partial y} = nf(x, y)$

**State Generalized Euler's Theorem on Homogeneous Function**
If $f(x, y, z)$ be a homogeneous function of $x$, $y$ and $z$ of degree $n$ then generalized Euler's theorem is $x \frac{\partial f}{\partial x} + y \frac{\partial f}{\partial y} + z \frac{\partial f}{\partial z} = nf(x, y, z)$



# Tangent and Normal


**Define Tangent**
The tangent at any point $P$ to a given curve is defined as the limiting position of the secant $PQ$ as the point $Q$ approaches $P$ along the curve


**Define Normal**
The normal at any point $P$ to a given curve is the straight line through that point drawn perpendicular to the tangent at that point $P$.


# Curvature

**Define Curvature**
The curvature is the rate of change of direction of the curve with respect to the arc that is the curvature at any point $P$ on the curve is
$$
P = \lim_{\partial s \to \infty} \frac{\partial \psi}{\partial s} = \frac{d \psi}{ds}
$$

**Define Radius of Curvature**
The reciprocal of the curvature at any point $P$ is called the radius of curvature a $P$, and it is denoted by $\rho$, Thus,
$$
\rho = \frac 1P = \frac{ds}{d \psi}
$$

**Define Evolute**
The locus of the centre of curvature of all points of a given curve is called the evolute of the curve.