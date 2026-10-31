"""Exact-arithmetic checks for the mixture construction (finite analogue).

Finite analogue of Lemma 2: B is any joint distribution on X x Y, nu any
distribution on X. P = (1-w) * (delta_0 x nu x B_Y) + w * (delta_1 x B) on
I x X x Y. Check, for every y with B_Y(y) > 0:
  (a) P_Y = B_Y;
  (b) P(I=i, X=x | Y=y) = (1-w) nu(x) [i=0] + w B(x|y) [i=1];
  (c) B(x|y) = P(I=1, X=x | Y=y) / w   (recovery).
Random instances, exact rationals.
"""
from fractions import Fraction as F
import random, itertools

def rand_dist(n, rng):
    v = [rng.randint(1, 9) for _ in range(n)]
    s = sum(v)
    return [F(a, s) for a in v]

def check(seed):
    rng = random.Random(seed)
    nx, ny = rng.randint(2, 4), rng.randint(2, 4)
    flat = rand_dist(nx * ny, rng)
    B = {(x, y): flat[x * ny + y] for x in range(nx) for y in range(ny)}
    nu = rand_dist(nx, rng)
    w = F(1, 2 ** rng.randint(1, 6))
    BY = {y: sum(B[(x, y)] for x in range(nx)) for y in range(ny)}
    P = {}
    for x, y in itertools.product(range(nx), range(ny)):
        P[(0, x, y)] = (1 - w) * nu[x] * BY[y]
        P[(1, x, y)] = w * B[(x, y)]
    assert sum(P.values()) == 1
    PY = {y: sum(P[(i, x, y)] for i in (0, 1) for x in range(nx)) for y in range(ny)}
    assert PY == BY, "(a) fails"
    for y in range(ny):
        for x in range(nx):
            c0 = P[(0, x, y)] / PY[y]
            c1 = P[(1, x, y)] / PY[y]
            assert c0 == (1 - w) * nu[x], "(b) i=0 fails"
            assert c1 == w * B[(x, y)] / BY[y], "(b) i=1 fails"
            assert c1 / w == B[(x, y)] / BY[y], "(c) fails"
    return True

assert all(check(s) for s in range(2000))
print("mixture identities: 2000 random exact instances OK")

# Lemma 1: w_M is computable uniformly in M. Toy machines: halt at step n, or never.
def w_true(n):
    return F(0) if n is None else F(1, 2 ** n)

def w_approx(n, k):
    # run M for k steps; output 2^-n if halted at step n <= k, else 0
    return F(1, 2 ** n) if (n is not None and n <= k) else F(0)

for n in [None] + list(range(1, 40)):
    for k in range(0, 45):
        assert abs(w_true(n) - w_approx(n, k)) <= F(1, 2 ** k), (n, k)
print("w_M approximation error <= 2^-k for all toy machines and k < 45: OK")
