
## Functions

- It's a correspondance between input numbers (x-values) and output numbers (y-values) that sends each input number (x-value) to exactly one output number (y-value).
- Eg. $y = x^2 + 1$, which can also be written as $f(x) = x^2 + 1$ 
- Solving for $x = 2$ , $f(2) = 2^2 + 1 = 4 + 1 = 5$
- Plotting the function 
```functionplot
---
title: function
xLabel: x
yLabel: x
bounds: [-10,10,-10,10]
disableZoom: false
grid: true
---
f(x) = x^2
```

## Increasing Functions 

- A function can be increasing or decreasing either entirely or in parts.
- A function can be increasing between a given interval or vice versa.

```functionplot
---
title: increasing decreasing
xLabel: x
yLabel: x
bounds: [-5,5,-5,5]
disableZoom: True
grid: true
---
f(x) = x ^ 3 - 4x
```

## Maxima and Minima 

- A function $f(x)$ has an absolute maximum at $x = c$ if 
	- the y-value $f(c)$ is called the **absolute maximum value** of $f$
	- the point $(c, f(c))$ is called an absolute maximum point.

- A function $f(x)$ has an absolute minimum at $x = C$ if
```functionplot
---
title: Maxima
xLabel: x
yLabel: y
bounds: [-5,5,-5,5]
disableZoom: false
grid: true
---
f(x) = sin(x)
```
