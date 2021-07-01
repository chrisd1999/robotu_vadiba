from sympy import *

f = 44.5
e = 17.5
fr, er = f/2*sqrt(3), e/2*sqrt(3)
rf = 27
re = 47.5

x0 = 16.3076
y0 = 2.3849
z0 = -42.8923

yj1, zj1 = symbols(['yj1', 'zj1'])
system = [
    Eq(pow(yj1+fr, 2) + pow(zj1, 2), pow(rf, 2)),
    Eq(pow((yj1 - y0 + er), 2) + pow((zj1 - z0), 2), (pow(re, 2) - pow(x0, 2)))
]

soln = solve(system, [yj1, zj1])

print(soln)