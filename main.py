from sympy import *

az, bz, cz = 26, 30, 22

aco = 3

l2 = 19.5 * 19.5
s, se = 30, 15

r = s / sqrt(3) - aco - se / (2 * sqrt(3))

x0, y0, z0 = symbols(['x0', 'y0', 'z0'])
system = [
    Eq(pow(az - z0, 2), l2 - pow(x0, 2) - pow((y0 - r), 2)),
    Eq(pow(bz - z0, 2), l2 - pow((x0 - r*(sqrt(3)/2)), 2) - pow((y0 + r/2), 2)),
    Eq(pow(cz - z0, 2), l2 - pow((x0 + r*(sqrt(3)/2)), 2) - pow((y0 + r/2), 2))
]
soln = solve(system, [x0, y0, z0])

x0, y0, z0 = soln[1][0], soln[1][1], soln[1][2]

print(f'x0:\t{x0}\ny0:\t{y0}\nz0:\t{z0}')