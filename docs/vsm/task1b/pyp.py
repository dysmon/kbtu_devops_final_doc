from pulp import *

pos = [200, 120, 150]
a = [4, 2, 3]
b = [3, 1, 2]
costa = 30
costb = 20

prob = LpProblem("Profit maximization problem", LpMaximize)
cnta = LpVariable("a", 0, None, LpInteger)
cntb = LpVariable("b", 0, None, LpInteger)

prob += costa * cnta + costb * cntb, "Total cost"
for i in range(len(pos)):
    prob += (cnta * a[i] + cntb * b[i] <= pos[i]), f"Contstraint #{i}"

prob.writeLP("sol.lp")
prob.solve()

print(f"Status: {LpStatus[prob.status]}")

for v in prob.variables():
    print(v.name, "=", v.varValue)


