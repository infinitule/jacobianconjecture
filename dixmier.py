#!/usr/bin/env python3
"""
The explicit Dixmier counterexample induced by the Jacobian-Conjecture
counterexample F.

The counterexample F is due to Levent Alpoge (@__alpoge__, https://alpo.ge),
announced 2026-07-20, found with Claude Fable 5. This script derives the standard
Weyl-algebra consequence; credit for the map itself belongs to Alpoge.

The Dixmier Conjecture (1968) asserts that every algebra endomorphism of the
Weyl algebra A_n is an automorphism.  Here we write down an *explicit*
endomorphism phi of A_3 that is injective but NOT surjective, i.e. an
endomorphism that is not an automorphism -- a counterexample to DC_3.

Weyl algebra A_3 = C<x1,x2,x3, d1,d2,d3>,  [d_i, x_j] = delta_ij, others 0.
We use the faithful polynomial representation: x_i acts by multiplication,
d_i acts as the partial derivative on C[x1,x2,x3].

Construction (van den Essen, *Polynomial Automorphisms and the Jacobian
Conjecture*; Tsuchimoto; Bavula).  For F with det J_F in C^*,

    phi(x_i) = f_i ,        phi(d_i) = sum_k (J_F^{-1})_{k,i} d_k .

Because det J_F = -2 is a nonzero CONSTANT, J_F^{-1} has polynomial entries, so
each phi(d_i) is a genuine element of A_3 (a polynomial-coefficient vector
field).  Run:  python3 dixmier.py
"""
import sympy as sp

x, y, z = sp.symbols('x y z')
V = [x, y, z]

# The Jacobian-Conjecture counterexample F (see verify.py / README).
f = [(1 + x*y)**3*z + y**2*(1 + x*y)*(4 + 3*x*y),
     y + 3*x*(1 + x*y)**2*z + 3*x*y**2*(4 + 3*x*y),
     2*x - 3*x**2*y - x**3*z]

J = sp.Matrix(f).jacobian(V)
assert sp.expand(J.det()) == -2                 # constant, nonzero
Jinv = J.inv()                                  # polynomial entries since det is constant
assert all(sp.expand(e).is_polynomial(*V) for e in Jinv)

# phi(d_i) as a differential operator D_i on C[x,y,z]:  D_i = sum_k Jinv[k,i] d_k
def D(i, g):
    return sp.expand(sum(Jinv[k, i]*sp.diff(g, V[k]) for k in range(3)))

# ---- The explicit endomorphism -------------------------------------------
print("phi is the algebra endomorphism of A_3 defined by")
print("  phi(x_i) = f_i,   phi(d_i) = c_{1i} d_1 + c_{2i} d_2 + c_{3i} d_3\n")
for i in range(3):
    print(f"phi(x_{i+1}) = f_{i+1} =")
    print("   ", sp.expand(f[i]))
for i in range(3):
    print(f"\nphi(d_{i+1}) = ")
    for k in range(3):
        print(f"    ({sp.expand(Jinv[k, i])}) * d_{k+1}")

# ---- Verify phi is a well-defined homomorphism (all A_3 relations) --------
rel_x  = all(sp.expand(f[i]*f[j] - f[j]*f[i]) == 0 for i in range(3) for j in range(3))
rel_dx = sp.Matrix(3, 3, lambda i, j: D(i, f[j])) == sp.eye(3)
rel_dd = all(
    sp.expand(sum(Jinv[k, i]*sp.diff(Jinv[l, j], V[k])
                - Jinv[k, j]*sp.diff(Jinv[l, i], V[k]) for k in range(3))) == 0
    for i in range(3) for j in range(3) for l in range(3))

print("\n--- relations of A_3 under phi ---")
print("  [phi(x_i), phi(x_j)] = 0        :", rel_x)
print("  [phi(d_i), phi(x_j)] = delta_ij :", rel_dx)
print("  [phi(d_i), phi(d_j)] = 0        :", rel_dd)
assert rel_x and rel_dx and rel_dd
print("=> phi : A_3 -> A_3 is a well-defined algebra endomorphism.\n")

# ---- Why phi is not an automorphism --------------------------------------
# 1) A_3 is a SIMPLE ring (char 0), so the nonzero homomorphism phi is injective.
# 2) Theorem (van den Essen 4.x; equiv. the elementary DC_n => JC_n direction):
#    phi_F is an automorphism of A_n  <=>  F is an automorphism of C^n.
#    F is NOT an automorphism -- verify.py exhibits three distinct points with a
#    common image, so F is 3:1, not injective.  Hence phi is NOT surjective.
print("phi is injective (A_3 is simple) but NOT surjective, because F is 3:1 and")
print("phi_F is an automorphism of A_3 iff F is an automorphism of C^3 (it is not).")
print("=> phi is an endomorphism of A_3 that is not an automorphism:")
print("   a counterexample to the Dixmier Conjecture (n = 3).")
