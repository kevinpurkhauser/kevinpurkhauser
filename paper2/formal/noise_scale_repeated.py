"""Repeated observations of one source with unknown Gaussian scale s (marginalised).
Joint likelihood of n readings given h: f_n(y|h) = int prod_i phi_s(y_i - h) pi(ds) <= (2 pi)^(-n/2) E_pi[s^-n],
with equality at y_1 = ... = y_n = h. So f_n is bounded iff E_pi[s^-n] < oo.
Prior pi(s) proportional to exp(-1/s) on (0,1). Substituting t = 1/s:
  int_0^1 s^-n exp(-1/s) ds = int_1^oo t^(n-2) exp(-t) dt = upper incomplete Gamma(n-1, 1), finite for all n.
"""
import sympy as sp
from mpmath import mp, quad, exp, inf
t = sp.symbols('t', positive=True)
mp.dps = 30
Z = sp.integrate(sp.exp(-t)*t**-2, (t, 1, sp.oo))
for n in range(1, 8):
    m = sp.integrate(t**(n-2)*sp.exp(-t), (t, 1, sp.oo))
    num = quad(lambda s: s**(-n)*exp(-1/s), [0, 1])   # direct numeric check, original variable
    assert abs(sp.N(m, 25) - num) < 1e-15
    print(f"n={n}: E[s^-n] = {sp.N(m/Z, 10)} (finite)")
mass = quad(lambda s: exp(-1/s), [0, 0.01]) / quad(lambda s: exp(-1/s), [0, 1])
print("prior mass of (0, 0.01) =", mass, "> 0")
s = sp.symbols('s', positive=True)
print("contrast, density 2s: E[s^-1] =", sp.integrate(2*s/s, (s, 0, 1)), "; E[s^-2] =", sp.integrate(2*s/s**2, (s, 0, 1)))
