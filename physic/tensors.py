from sympy import *
init_printing(use_latex=True)

# g(mn)
# G[l](mn)

# x0 = r, x1 = a, x2 = b


class Metric:
    def __init__(self, metric):
        self.g = metric

    def __str__(self):
        return str(self.g)

    def __getitem__(self, key):
        return self.g.row(key)


class SphericMetric:
    def __init__(self):
        r, t, p = symbols('r a b')
        self.coord = [r, t, p]
        self.metric = Metric(Matrix([[1, 0, 0],
                                     [0, r**2, 0],
                                     [0, 0, r**2 * (sin(t))**2]]))
        self.inverse = Metric((self.metric.g)**-1)


class CartesianMetric:
    def __init__(self):
        self.metric = Metric(Matrix([[1, 0, 0],
                                     [0, 1, 0],
                                     [0, 0, 1]]))
        self.inverse = self.metric


class Christoffel:
    # C^l_mn = 0.5 g^la(d(m)g_na + d(n)g_am - d(a)g_mn)
    def __init__(self, metrictype):
        dim = metrictype.metric.g.shape[0]
        self.symb = []
        for l in range(dim):
            mlist = []
            for m in range(dim):
                nlist = []
                for n in range(dim):
                    chrlmn = 0
                    for a in range(dim):
                        chrlmn += 0.5 * metrictype.inverse[l][a] * (
                            metrictype.metric[n][a].diff(
                                metrictype.coord[m]) + metrictype.metric[a][m].diff(
                                metrictype.coord[n]) - metrictype.metric[m][n].diff(
                                metrictype.coord[a]))
                    nlist.append(chrlmn)
                mlist.append(nlist)
            self.symb.append(mlist)


m = SphericMetric()

chrs = Christoffel(m)
print(chrs.symb)
