"""Proposition 2 with continuous (tent) densities. Exact rational checks.
E_n = union of 2^(n-1) dyadic intervals of length 2^-2n (digits n..2n zero). On each, a tent of mass 2^-(n-1).
Tent height at centre = 2*mass/length = 2^(n+2); on the central half, height >= 2^(n+1).
Prior: I ~ (1-w, w), w = 2^-n; Z | I=0 ~ Leb[0,1]; Z | I=1 ~ tent density f_n.
On the central halves: P(I=1 | z) = w f / ((1-w) + w f) >= 2/(3 - 2^-n) >= 2/3.
Central halves have total Lebesgue measure 2^(n-1) * 2^-2n / 2 = 2^-(n+2) > 0, and inside any cylinder [sigma]
with |sigma| <= n-1 they have measure 2^-|sigma| * 2^-(n+2).
"""
from fractions import Fraction as F
for n in range(2, 40):
    w = F(1, 2**n); L = F(1, 2**(2*n)); mass = F(1, 2**(n-1))
    h = 2*mass/L
    assert h == 2**(n+2)
    fmin = h/2
    post = w*fmin/((1-w) + w*fmin)
    assert post >= F(2, 3)
    assert 2**(n-1) * mass == 1                       # tents integrate to 1
    assert 2**(n-1) * L / 2 == F(1, 2**(n+2))         # central-half measure
print("tent version of Proposition 2: posterior >= 2/3 on a set of measure 2^-(n+2); constants OK")
