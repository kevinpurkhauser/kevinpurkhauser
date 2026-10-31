"""Proposition 2 (all members tractable, no uniform updater): exact check of the posterior on E_n.
R_M = (1-w) delta_0 x Leb + w delta_1 x Unif(E_n), w = 2^-n, E_n = {y in [0,1]: binary digits n..2n are 0},
Leb(E_n) = 2^-(n+1). For y in E_n: P(I=1|y) = w*2^(n+1) / ((1-w) + w*2^(n+1)) = 2/(3 - 2^-n) >= 2/3.
For y not in E_n: P(I=1|y) = 0.
"""
from fractions import Fraction as F
import itertools, random
for n in range(1, 40):
    w = F(1, 2**n); f1 = F(2**(n+1)); f0 = F(1)
    post = w*f1/((1-w)*f0 + w*f1)
    assert post == F(2, 1)/(3 - F(1, 2**n)) and post >= F(2, 3)
# measure of E_n by brute force on digit strings for small n
for n in range(1, 9):
    L = 2*n + 1
    cnt = sum(1 for bits in itertools.product((0,1), repeat=L) if all(b == 0 for b in bits[n-1:2*n]))
    # digits indexed 1..L; digits n..2n are positions n-1..2n-1 (0-based)
    assert F(cnt, 2**L) == F(1, 2**(n+1)), (n, cnt)
# independence from a prefix sigma of length < n
for n in range(3, 9):
    for m in range(0, n):
        L = 2*n + 1
        for sigma in [(0,)*m, (1,)*m]:
            cnt = sum(1 for bits in itertools.product((0,1), repeat=L-m) if all(b == 0 for b in (sigma+bits)[n-1:2*n]))
            assert F(cnt, 2**(L-m)) == F(1, 2**(n+1))
# error bound used in the proof: d(m, delta0) < 1/8 and d(true, delta0) >= 2/3 gives d(m, true) > 1/16
assert F(2,3) - F(1,8) > F(1,16)
print("Proposition 2 numerics: posterior >= 2/3 on E_n, Leb(E_n) = 2^-(n+1), independence from short prefixes: OK")
