import math
from fractions import Fraction
from z3 import Ints, Solver


with open('input.txt') as fp:
    hails = []
    for line in fp.readlines():
        p, v = line.split(' @ ')
        p = [int(s) for s in p.split(',')]
        v = [int(s) for s in v.split(',')]
        hails.append((p, v))

    def normalize(p):
        p = [abs(x) for x in p]
        g = math.gcd(*p)
        return tuple([x // g for x in p])

    def intersect2d(hail1, hail2):
        (x1, y1, _), (x2, y2, _) = hail1
        x2, y2 = x1 + x2, y1 + y2
        (x3, y3, _), (x4, y4, _) = hail2
        x4, y4 = x3 + x4, y3 + y4

        dx1, dy1, dx2, dy2 = x1 - x2, y1 - y2, x3 - x4, y3 - y4
        den = dx1 * dy2 - dy1 * dx2
        if den == 0:
            if normalize((x1 - x3, y1 - y3)) == normalize((hail1[1][:2])):
                print(hail1, hail2)
                assert False
            return

        D1, D2 = x1*y2 - y1*x2, x3*y4 - y3*x4
        p = Fraction(D1 * dx2 - dx1 * D2, den), Fraction(D1 * dy2 - dy1 * D2, den)

        if (p[0] - x1) / hail1[1][0] < 0 or (p[0] - x3) / hail2[1][0] < 0:
            return

        return p


    lo, hi = 200000000000000, 400000000000000
    if len(hails) == 5:
        lo, hi = 7, 27  # Sample

    cnt = 0
    for i in range(len(hails)):
        for j in range(i + 1, len(hails)):
            p = intersect2d(hails[i], hails[j])
            if p is None:
                continue
            if lo <= p[0] <= hi and lo <= p[1] <= hi:
                cnt += 1
    print(cnt)

    (x1, y1, z1), (vx1, vy1, vz1) = hails[0]
    (x2, y2, z2), (vx2, vy2, vz2) = hails[1]
    (x3, y3, z3), (vx3, vy3, vz3) = hails[2]
    pxt, pyt, pzt, vxt, vyt, vzt, t1, t2, t3 = Ints('pxt pyt pzt vxt vyt vzt t1 t2 t3')

    solver = Solver()
    solver.add(
      pxt + vxt * t1 == x1 + vx1 * t1,
      pyt + vyt * t1 == y1 + vy1 * t1,
      pzt + vzt * t1 == z1 + vz1 * t1,

      pxt + vxt * t2 == x2 + vx2 * t2,
      pyt + vyt * t2 == y2 + vy2 * t2,
      pzt + vzt * t2 == z2 + vz2 * t2,

      pxt + vxt * t3 == x3 + vx3 * t3,
      pyt + vyt * t3 == y3 + vy3 * t3,
      pzt + vzt * t3 == z3 + vz3 * t3,
    )
    solver.check()
    model = solver.model()
    print(model[pxt].as_long() + model[pyt].as_long() + model[pzt].as_long())
