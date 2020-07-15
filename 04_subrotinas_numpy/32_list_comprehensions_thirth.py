vps = [100, 200, 300, 400, 500,
       1050, 2300, 3200, 4400, 5100,
       10000, 22000, 37000, 49000, 63000]

# VF = VP * (1 + i) ** n
i = 0.016
n = 60

# Na forma trasicional
vfs = []
for vp in vps:
    if vp >= 2300 and vp <= 3700:
        vfs.append(vp * (1 + i) ** n)
print(vfs)

# Na forma de List Comprehensions
# Quebra de linha \
vfs_lc = \
    [vp * (1 + i) ** n for vp in vps if vp >= 2300 and vp <= 3700]
print(vfs_lc)
