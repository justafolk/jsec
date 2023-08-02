
## Cheat sheet

| **Identifier** | **Description**  |
| -------------- | ---------------- |
| $p \wedge q$   | It's Conjunction |
| $p \vee q$     | It's Disjunction | 



```tikz

\usepackage{tikz}
\usepackage{circuitikz}

\begin{document}

\begin{circuitikz}[american, voltage shift=0.5]
\draw (0,2) node[and port] (myand1) {}
(0,0) node[and port] (myand2) {}
(2,1) node[xnor port] (myxnor) {}
(myand1.out) -- (myxnor.in 1)
(myand2.out) -- (myxnor.in 2);
\end{circuitikz}

\end{document}
```
