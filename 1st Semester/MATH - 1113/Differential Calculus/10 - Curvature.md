
# Curvature

**The curvature is the rate of change of direction of the curve with respect to the arc that is the curvature at any point $P$ on the arc is**
$$
P = \lim_{\partial s \to \infty}\frac{\partial \psi}{\partial s} = \frac{d \psi}{d s}
$$

# Radius of Curvature

**The reciprocal of the curvature at any point $P$ is called the radius of curvature at $P$, and it is denoted by $\rho$. Thus**
$$
\rho = \frac1P = \frac{ds}{d \psi}
$$

$(i)$ radius of curvature at origin when $y = f(x)$
$$
\rho = \frac {(1 + (y_1)^2)^\frac32}{y_2}
$$
$(ii)$ Radius of curvature when $x = f(t), y = f(t)$
$$
\rho = \frac{x'^{2} + y'^{2}}{x'y'' - y'x''}
$$
$(iii)$ Getting radius of curvature by expanding $y$
$$
y = px + \frac{qx^2}{2!} +\ ...\ ...
$$
Where,
$$
p = y_1
$$
$$
q = y_2
$$
$(iv)$ General formula for curvature at any point
$$
\rho = \frac{(f_x^2 + f_y^2)^{\frac32}}{f_x^2f_{yy} - 2f_xf_yf_{xy} + f_y^2f_{xx}}
$$


# Evolute 

**The locus of the centre of curvature of all points of a given curve is called the evolute of the curve**

Center of curvature,
$$
\bar{x} = x - \frac{y_1(1 + y_1^2)}{y_2}
$$
$$
\bar{y} = y + \frac{1 + y_1^2}{y_2}
$$

### Find the chord of curvature through the pole of curve

Given, $r = f(\theta)$
$$
tan \phi = r \frac{d \theta}{dr}
$$
Solve for $\phi$

Get the radius of curvature
$$
\rho = \frac{(r^2 + (\frac{dr}{d\theta})^2)^\frac32}{r^2 + 2(\frac{dr}{d\theta})^2 - r \frac{d^2r}{d\theta ^2}}
$$

Length of the chord of curvature through the pole
$$
= 2\rho sin\phi
$$
