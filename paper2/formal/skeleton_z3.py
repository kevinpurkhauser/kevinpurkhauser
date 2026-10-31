"""Validity check of the core argument's logical skeleton (Z3).
Each conclusion is valid iff premises AND NOT(conclusion) is unsat.
"""
from z3 import *

Agent = DeclareSort('Agent')
Prior = DeclareSort('Prior')
a, b = Consts('a b', Agent)
p = Const('p', Prior)
Req   = Function('Req', Agent, BoolSort())    # bound by conditionalization norm
Can   = Function('Can', Agent, BoolSort())    # can conditionalize from own representation
Same  = Function('Same', Agent, Agent, BoolSort())  # same credence function
Holds = Function('Holds', Agent, BoolSort())  # holds a prior and receives continuous evidence
InN   = Function('InN', Agent, BoolSort())    # representation in channel class N
World = Function('World', Agent, Prior)       # agent's prior over the world variables
a1, a2 = Consts('a1 a2', Agent)

def check(name, premises, conclusion):
    s = Solver()
    s.add(*premises)
    s.add(Not(conclusion))
    r = s.check()
    print(f"{name}: {'VALID' if r == unsat else 'NOT VALID ('+str(r)+')'}")
    return r == unsat

# Argument 1: representation-dependence
P1 = ForAll([a], Implies(Req(a), Can(a)))                      # (CERT) restricted ought-implies-can
P2 = ForAll([a], Implies(And(Holds(a), Can(a)), Req(a)))       # orthodoxy: able holders are bound
P3 = And(Same(a1, a2), Holds(a1), Holds(a2), Can(a1), Not(Can(a2)))  # Proposition 1 witness pair
C1 = Not(ForAll([a, b], Implies(Same(a, b), Req(a) == Req(b))))
ok1 = check("Argument 1 (representation-dependence)", [P1, P2, P3], C1)

# Argument 2: every world-prior is compatible with certifiable updating
P4 = ForAll([a], Implies(InN(a), Can(a)))                      # noise corollary + Lemma 3
P5 = ForAll([p], Exists([a], And(InN(a), Holds(a), World(a) == p)))  # any world prior can be given a channel presentation
C2 = ForAll([p], Exists([a], And(Holds(a), Req(a), World(a) == p)))
ok2 = check("Argument 2 (no constraint on world-priors)", [P2, P4, P5], C2)

# Sanity: dropping CERT (P1) breaks Argument 1
ok3 = not check("Argument 1 without P1 (expected NOT VALID)", [P2, P3], C1)
# Sanity: dropping P4 breaks Argument 2
ok4 = not check("Argument 2 without P4 (expected NOT VALID)", [P2, P5], C2)
assert ok1 and ok2 and ok3 and ok4
print("all skeleton checks behave as expected")
