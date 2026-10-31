"""Reply to the advocate's 'noise floor' objection.
Gaussian noise with unknown scale s, prior pi on s in (0,1). The mixture density
of the noise is f(e) = int phi_s(e) pi(s) ds, maximised at e = 0, where
f(0) = (2 pi)^(-1/2) E_pi[1/s]. So the mixture density is bounded iff E_pi[1/s] < oo.
"""
import sympy as sp
s, e = sp.symbols('s e', positive=True)
phi = sp.exp(-e**2/(2*s**2))/(s*sp.sqrt(2*sp.pi))
for name, pi in [("uniform on (0,1)", sp.Integer(1)), ("density 2s on (0,1)", 2*s), ("density 3s^2", 3*s**2)]:
    assert sp.integrate(pi, (s, 0, 1)) == 1
    Einv = sp.integrate(pi/s, (s, 0, 1))
    f0 = sp.integrate(phi.subs(e, 0)*pi, (s, 0, 1))
    print(f"{name}: E[1/s] = {Einv}, f(0) = {sp.simplify(f0)}, every interval (0,d) has prior mass {sp.simplify(sp.integrate(pi,(s,0,sp.Symbol('d',positive=True))))}")
# check phi_s(e) <= phi_s(0) for all e, so sup_e f(e) = f(0)
assert sp.simplify(phi.subs(e,0) - phi) != 0
print("max of each Gaussian at e=0; hence sup f = f(0). Bounded iff E[1/s] finite.")
