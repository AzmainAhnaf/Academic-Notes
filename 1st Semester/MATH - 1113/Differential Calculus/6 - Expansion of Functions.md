

# Rolle's Theorem

[Online Reference Lecture](https://www.youtube.com/watch?v=IFtjDDB8fzo)

Statement:
$$
(i)\ f(x)\ is\ continuous\ in\ the\ closed\ interval\ a \le\ x\ \le\ b\ or,\ x\ \in\ [a,b],
$$
$$
(ii)\ f'(x)\ exists\ in\ the\ open\ interval\ a\ <\ x\ <\ b\ or, x\ \in\ (a,b),
$$
$$
(iii)\ f(a)\ =\ f(b)
$$
then there exists at lest one value of x (say k) between a and b such that
$$
f'(k)\ =\ 0
$$

# Lagrange's Mean Value Theorem

[Online Reference Lecture](https://www.youtube.com/watch?v=_rLizW7giT4&t=602s)

Statement:
$$
If\ (i)\ f(x)\ is\ continuous\ in\ the\ closed\ interval\ a\ \le\ x \le\ b\ or,\ x\ \in\ [a,b],\ and
$$
$$
(ii)\ f'(x)\ exists\ in\ the\ open\ interval\ a\ <\ x\ <\ b\ or, x\ \in\ (a,b),
$$
then there exists at lest one value of x (say k) between a and b such that
$$
f(b)\ -\ f(a)\ =\ (b\ -\ a)f'(k)
$$


# Maclaurin's Series Expansion

[Online Reference Lecture](https://www.youtube.com/watch?v=Ac1mr2WrO-g&list=PLU6SqdYcYsfKEgfOKHsHUdEq3uA8KA0w0)

## Maclaurin's Theorem

If *f(x)* be a function of the variable x such that it can be expanded in ascending power of x and this expansion be differentiated any number of times then

$$
f(x)\ =\ f(0)\ +\ \frac{x}{1!}f'(0)\ +\ \frac{x^2}{2!}f''(0)\ +\ \frac{x^3}{3!}f'''(0)\ +\ ...\ ...\ +\ \frac{x^n}{n!}f^n(x)\ +\ ...
$$

### Proof

Let,
$$
f(x) = A_0 + A_1x + A_2x^2 + A_3x^3 +\ ...\ ... -- (i)
$$
$$
f(0) = A_0
$$
$$
f'(x) = A_1 + 2A_2x + 3A_3x^2 +\ ...\ ...
$$
$$
f'(0) = A_1
$$
$$
f''(x) = 2A_2 + 6A_3x +\ ...\ ...
$$
$$
f''(0) = 2A_2\ \Rightarrow\ A_2 = \frac{f''(0)}{2!}
$$
$$
f'''(x) = 6A_3\ +\ ...\ ...
$$
$$
f'''(0) = 6A_3\ \Rightarrow\ A_3 = \frac{f'''(0)}{3!}
$$
Replacing A<sub>0</sub>, A<sub>1</sub>, A<sub>2</sub>, A<sub>3</sub> in *(i)*, we will get Maclaurin's Series.


# Taylor Series

[Online Reference Lecture](https://youtu.be/LEspaisjDFE?si=uIjLFL4xA634Ffx8)

## Taylor's Theorem

If (a + h) be a function of the variable *h* such that it can  be expanded in ascending power of h and this expansion be differentiable any number of times then

$$
f(a+h) = f(a) + hf'(a) + \frac{h^2}{2!}f''(a) + \frac{h^3}{3!}f'''(a) +\ ...\ ...
$$

Proof is same as the Maclaurin Series, we just evaluate f(a) for every derivative instead of evaluation f(0).

Let, a + h = b
Or, h = b - a

Then,
$$
f(b) = f(a) + (b-a)f'(a) + \frac{(b-a)^2}{2!}f''(a) + \frac{(b-a)^3}{3!}f''''(a)\ +\ ...\ ...
$$



# Taylor's Series in Finite Form (Generalized Mean Value Theorem)

If f<sup>n-1</sup>(x) is continuous in \[a, b] and f<sup>n</sup> exists in (a, b) then

$$
f(b) = f(a) + (b - a)f'(a) + \frac{(b-a)^2}{2!}f''(a) +\ ...\ + \frac{(b-a)^{n-1}}{(n-1)!}f^{n-1}(a) + \frac{(b-a)^n}{n!}f^n(k)\ ...(i)
$$
Where,
$$
k \in (a, b)
$$

and if,
	b = a + h
so that
	b - a = h
then

$$
f(a+h) = f(a) + hf'(a) + \frac{h^2}{2!}f''(a) +\ ...\ + \frac{h^{n-1}}{(n-1)!}f^{n-1}(a) + \frac{h^n}{n!}f^n(a + \theta h)\ ... (ii)
$$
Where,
$$
\theta \in (0,1)
$$
now replacing x for a then we obtain

$$
f(x+h) = f(x) + hf'(x) + \frac{h^2}{2!}f''(x) +\ ...\ + \frac{h^{n-1}}{(n-1)!}f^{n-1}(x) + \frac{h^n}{n!}f^n(x + \theta h)\ ...(iii)
$$

### Extension Part

The series $(i)$, $(ii)$ or, $(iii)$ is called Taylor's series with the remainder in Lagrange's form, the remainder being $\frac{(b-a)^n}{n!}f^n(k)$ or $\frac{h^n}{n!}f^n(a + \theta h)$ or  $\frac{h^n}{n!}f^n(x + \theta h)$

The original Taylor Series is
$$
f(b) = f(a) + (b - a)f'(a) + \frac{(b-a)^2}{2!}f''(a) +\ ...\ + \frac{(b-a)^{n-1}}{(n-1)!}f^{n-1}(a) + \frac{(b-a)^n}{n!}f^n(k)\ ...(i)
$$

Putting n = 1 in Taylor's series then we get the mean value theorem
$$
f(b)-f(a) = (b-a)f'(k)
$$
Another form of Taylor Series is
$$
f(x+h) = f(x) + hf'(x) + \frac{h^2}{2!}f''(x) +\ ...\ + \frac{h^{n-1}}{(n-1)!}f^{n-1}(x) + \frac{h^n}{n!}f^n(x + \theta h)\ ...(iii)
$$
Again putting x = 0 and h = x, we get Maclaurin's series for f(x) i.e.
$$
f(x) = f(0) + xf'(0) + \frac{x^2}{2!}f''(x) +\ ...\ +\ \frac{x^{n-1}}{(n-1)!}f^{n-1}(0) + \frac{h^n}{n!}f^n(\theta x)
$$


