import chempy as cp
from pprint import pprint


def intersperse(val, sequence):
    first = True
    for item in sequence:
        if not first:
            yield val
        yield item
        first = False


def string_reaction(reac_list, reactants, prod_list, products):
    lhalf = [
        f"({reactants[r]}){r}" if not isinstance(reactants[r], int) or isinstance(reactants[r], float)
        else f"{reactants[r]}{r}" if reactants[r] != 1 else f"{r}" for r in reac_list]
    lhalf = list(intersperse('+', lhalf))

    rhalf = [
        f"({products[p]}){p}" if not isinstance(products[p], int) or isinstance(products[p], float)
        else f"{products[p]}{p}" if products[p] != 1 else f"{p}" for p in prod_list]
    rhalf = list(intersperse('+', rhalf))

    to_print = lhalf + ['->'] + rhalf

    t = " ".join(to_print)
    return t


def react_ratio(r, p):
    lhalf = [f"({_})" for _ in r.values()]
    lhalf = list(intersperse(':', lhalf))
    rhalf = [f"({_})" for _ in p.values()]
    rhalf = list(intersperse(':', rhalf))
    to_print = lhalf + [':'] + rhalf

    t = " ".join(to_print)
    return t


reac_list = ['P2S3', 'HNO3', 'H2O']
prod_list = ['H3PO4', 'S', 'NO']

a = [formula for formula in reac_list]
b = [formula for formula in prod_list]
reac, prod = cp.balance_stoichiometry(a, b)
reactants, products = dict(reac), dict(prod)

print(string_reaction(reac_list, reactants, prod_list, products))
print(react_ratio(reactants, products))

# n1_mol = r_mass / r_mmass
# n2_mol_real = p_mass / p_mmass
# n2_mol_imag = n1_mol * products['H2O'] / reactants['KMnO4']
# resa = n2_mol_real / n2_mol_imag
# print(resa*100, "%")
