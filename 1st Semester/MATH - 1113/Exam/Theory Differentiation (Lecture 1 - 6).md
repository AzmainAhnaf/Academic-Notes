
# Function

**Function**: A function is a relation between dependent and independent variables.
Examples: $(i)\ f(x) = x^2 + 2$.  $(ii)\ y = 2x + 1$ 

**Odd Function:** A function $f(x)$ is said to be odd if it changes sigh with the change of the sign of the variable $x$ that is if $f(-x)$ = $-f(x)$
Example: $f(x) = x^3$, $f(x) = \sin{(x)}$ 

**Even Function:** A function $f(x)$ is said to be even if it does not change sign with the change of sign of the variable $x$ that is if $f(-x) = f(x)$ 
Example: $f(x) = x^2$, $f(x) = \cos{(x)}$ 

**Monotone Function:** Let $x_1$, $x_2$ be any two points such that $x_1 < x_2$ in the interval of definition of a function $f(x)$, then $f(x)$ is said to be monotonically increasing if $f(x_1) < f(x_2)$ and monotonically decreasing if $f(x_1) > f(x_2)$.


# Limit

**Define Limit.**
A function $f(x)$ is said to have a limit $l$ at $x$ tends to $a$ if for every positive number $\epsilon$, we can determine another small positive number $\delta$, such that $|f(x) - l| < \epsilon$ for all values of $x$ which satisfying the inequality $|x - a| \le \delta$ and it is denoted by
$$
\lim_{x \to a} f(x) = l.
$$

**Define Right Hand Limit**
A function $f(x)$ is said to have a right hand limit $l_1$ at $x$ tends to $a$ if for every positive number $\epsilon$, we can determine another small positive number $\delta$, such that $|f(x) - l_1| < \epsilon$ for all values of $x$ which satisfying the inequality $x - a \le \delta$ and it is denoted by
$$
\lim_{x \to a^+}f(x) = l_1
$$
$$
\lim_{h \to 0}f(a + h) = l_1
$$

**Define Left Hand Limit**
A function $f(x)$ is said to have a left hand limit $l_2$ at $x$ tends to $a$ if for every positive integer $\epsilon$, we can determine another small positive integer $\delta$, such that $|f(x) - l_2| < \epsilon$ for all values of $x$ which satisfying the inequality $a - x \le \delta$ and it is denoted by
$$
\lim_{x \to a^-} f(x) = l_2
$$
$$
\lim_{h \to 0}f(a - h) = l_2
$$

**What are the differences between $\lim_{x \to a} f(x)$ and $f(a)$**
The statement $\lim_{x \to a} f(x)$ is a statement about the value of $f(x)$ when $x$ has any arbitrary value near to $a$ except $a$. But $f(a)$ stands for value of $f(x)$ when $x$ is exactly equal to $a$ or else by substitution of $a$ for $x$ in the expression $f(x)$ when it exists.


# Continuity


**Define Continuity**
a function $f(x)$ is said to be continuous at $x = a$ if its limit exists at that point and equal to its functional value at $x = a$ i.e., 
$$
\lim_{x \to a^+}f(x) = \lim_{x \to a^-} = f(a) \text{ or,}
$$
$$
\lim_{h \to 0} f(a + h) = \lim_{h \to 0}f(a - h) = f(a)
$$


# Differentiation 

**Define differentiability**
A function $f(x)$ is said to be differentiable at $x = a$ if
$$
\lim_{h \to 0^+} \frac{f(a + h) - f(a)}{h} = \lim_{h \to 0^-} \frac{f(a - h) - f(a)}{-h}
$$




# Successive Differentiation

**Define Successive Differentiation**
If $y = f(x)$ be a general function of $x$, then its differential coefficient $y_1 = \frac{dy}{dx} = f'(x)$ is called the first derivative of $f(x)$. The differential coefficient of $f'(x)$ is called the 2nd derivative of $f(x)$ and it is denoted by $f''(x)$. Similarly, the differential coefficient of $f''(x)$ is called the 3rd derivative of $f(x)$ and it is denoted by $f'''(x)$ and so on. If $f(x)$ is differentiated $n$ times with respect to $x$ then it is called the $nth$ derivative of $f(x)$ and it is denoted by $f^n(x)$. So the successive derivatives of $y = f(x)$ are denoted by $f'(x)$, $f''(x)$, $\ldots \ldots$, $f^n(x)$, $\ldots$ $\ldots$ 


**State Leibnitz's Theorem**
If $u$ and $v$ are two functions of $x$, then the $nth$ derivative of their product is
$$
(uv)_n = u_nv + n_{c_1}u_{n - 1}v_1 + n_{c_2}u_{n - 2}v_2 + \ldots + n_{c_r}u_{n - r}v_r + \ldots + uv_n
$$
