from src.life_table import LifeTable

# Example mortality rates (qx) for 5 years
qx = [0.01, 0.012, 0.013, 0.015, 0.018]

lt = LifeTable(qx, radix=100000)

print("qx:", lt.qx)
print("px:", lt.px)
print("lx:", lt.lx)
print("dx:", lt.dx)
