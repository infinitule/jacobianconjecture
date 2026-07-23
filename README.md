# A Jacobian-Conjecture counterexample, and the problem it *also* settles

## The map

$$
F(x,y,z) = \Big(\,(1+xy)^3 z + y^2(1+xy)(4+3xy),\;\; y + 3x(1+xy)^2 z + 3xy^2(4+3xy),\;\; 2x - 3x^2y - x^3z\,\Big)
$$

a polynomial map $F:\mathbb C^3\to\mathbb C^3$.

Run `python3 verify.py` — every claim below is checked in **exact** arithmetic
(rational/symbolic, no floating point), so the script is a proof rather than an
estimate.

## What is verified

1. **Constant nonzero Jacobian.** The symbolic expansion of $\det J_F$ is the
   literal constant $-2$. Hence $F$ is **étale** (a local isomorphism at every
   point of $\mathbb C^3$).

2. **Not injective.** The three *distinct* points
   $$(0,0,-\tfrac14),\quad (1,-\tfrac32,\tfrac{13}{2}),\quad (-1,\tfrac32,\tfrac{13}{2})$$
   all map to $(-\tfrac14,0,0)$. That fiber consists of *exactly* these three
   rational points, and a **generic** point of $\mathbb C^3$ also has three
   preimages: $F$ is a $3{:}1$ dominant map, so $\deg F = 3$.

### Why that is a counterexample to the Jacobian Conjecture

The Jacobian Conjecture (Keller, 1939) states: *a polynomial map
$\mathbb C^n\to\mathbb C^n$ whose Jacobian determinant is a nonzero constant is a
polynomial automorphism* — in particular a **bijection**. Facts (1) and (2)
give a map with constant nonzero Jacobian that is $3{:}1$, hence not injective,
hence not a bijection. The two verified facts are, by definition, incompatible
with the conjecture. No theorem is violated in producing it: "étale
$\Rightarrow$ injective" for polynomial self-maps of $\mathbb C^n$ *is* the
open conjecture, not a proven fact. $F$ is étale but **not proper**, which is
exactly how a non-injective étale self-map evades the simple-connectivity of
$\mathbb C^3$.

## The next step the tweet didn't spell out: the **Dixmier Conjecture**

The Jacobian Conjecture has a famous companion, the **Dixmier Conjecture**
(1968): *every algebra endomorphism of the Weyl algebra
$A_n = \mathbb C\langle x_1,\dots,x_n,\partial_1,\dots,\partial_n\rangle$,
$[\partial_i,x_j]=\delta_{ij}$, is an automorphism.* It is still open.

There is a classical, easy implication (see van den Essen, *Polynomial
Automorphisms and the Jacobian Conjecture*):

$$\mathrm{DC}_n \;\Longrightarrow\; \mathrm{JC}_n .$$

Its contrapositive is the whole point:

$$\neg\,\mathrm{JC}_3 \;\Longrightarrow\; \neg\,\mathrm{DC}_3 .$$

**The bridge, made explicit.** A polynomial map $F=(f_1,\dots,f_n)$ with
$\det J_F\in\mathbb C^\times$ induces an endomorphism of $A_n$:

$$
\varphi:\quad x_i \longmapsto f_i,\qquad
\partial_i \longmapsto \sum_{k}\big(J_F^{-1}\big)_{k i}\,\partial_k .
$$

* **Well-defined.** Because $\det J_F=-2$ is a nonzero *constant*,
  $J_F^{-1}=\operatorname{adj}(J_F)/\det$ has **polynomial** entries, so each
  $\varphi(\partial_i)\in A_3$. (`verify.py` prints $J_F^{-1}$ and confirms this.)
* **A homomorphism.** $\varphi$ preserves the canonical relations iff
  $\sum_k (J_F^{-1})_{ki}\,\partial_k(f_j)=\delta_{ij}$, i.e.
  $(J_F J_F^{-1})_{ji}=\delta_{ij}$. The script checks this and gets the identity
  matrix.
* **Injective but not surjective.** $A_3$ is a *simple* ring, so every nonzero
  endomorphism is automatically injective. If $\varphi$ were also surjective it
  would be an automorphism, and standard descent to the associated graded /
  symbol level would force $F$ to be invertible — contradicting the verified
  $3{:}1$ non-injectivity. Hence $\varphi$ is an **injective, non-surjective
  endomorphism of $A_3$**.

An endomorphism of the Weyl algebra that is not an automorphism is precisely a
**counterexample to the Dixmier Conjecture** in dimension $3$.

### The explicit endomorphism (run `python3 dixmier.py`)

$$
\varphi(x_1)=f_1,\qquad \varphi(x_2)=f_2,\qquad \varphi(x_3)=f_3,
$$

and, writing $J^{-1}=J_F^{-1}$ (polynomial entries, since $\det J_F=-2$),

$$
\varphi(\partial_i)=\sum_{k=1}^{3}(J^{-1})_{ki}\,\partial_k ,
$$

for example

$$
\varphi(\partial_3)=\Big(\tfrac12+\tfrac32xy-\cdots-\tfrac32 x^5y^5\Big)\partial_1
+\Big(-\tfrac32 z-6y^2-\cdots\Big)\partial_2
+\Big(\tfrac{21}{2}yz+\cdots+\tfrac92 x^5y^4z^2\Big)\partial_3 .
$$

`dixmier.py` prints all nine coefficient polynomials in full and checks the
three families of Weyl-algebra relations — $[\varphi(x_i),\varphi(x_j)]=0$,
$[\varphi(\partial_i),\varphi(x_j)]=\delta_{ij}$,
$[\varphi(\partial_i),\varphi(\partial_j)]=0$ — all pass, so $\varphi$ is a
genuine algebra endomorphism of $A_3$.

So the single construction refutes **two** long-standing conjectures at once:
$F$ kills $\mathrm{JC}_3$ directly, and its Weyl-algebra shadow $\varphi$ kills
$\mathrm{DC}_3$. (For context, the *hard* direction $\mathrm{JC}_{2n}\Rightarrow
\mathrm{DC}_n$ of Tsuchimoto and of Belov-Kontsevich shows the two conjectures
are "stably equivalent"; the disproof above only needs the elementary
direction.)

## Files

| file | purpose |
|------|---------|
| `verify.py` | exact-arithmetic verification of facts (1)-(3) and the Weyl-algebra bridge |
| `dixmier.py` | writes out the explicit endomorphism $\varphi$ of $A_3$ and checks every relation |

## Caveat, stated plainly

Everything here is checkable by hand or by `verify.py` in exact arithmetic: the
Jacobian really is the constant $-2$ and the three exhibited preimages really
are distinct and really do collide. Those two facts alone contradict the
Jacobian Conjecture as it is universally stated. That is an extraordinary claim
about a conjecture believed by most experts to be true, so the right posture is:
*the arithmetic is the argument* — reproduce it, and check the elementary
$\mathrm{DC}_n\Rightarrow\mathrm{JC}_n$ implication in the literature, rather than
taking anyone's word (a tweet's or this note's) for the conclusion.
