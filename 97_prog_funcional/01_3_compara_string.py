# Don’t Update, Create — String

# Not Functional - STRING
name = "Geison"
name = "{0} Flores".format(name)
print(name)

# Functional
firstname = "Geison"
lastname = "Flores"
name = "{0} {1}".format(firstname, lastname)
print(name)

# Not Functional - LIST
years = [2001, 2002]
years.append(2003)
years += [2004, 2005]
print(years) # [2001, 2002, 2003, 2004, 2005]

# Functional
years = [2001, 2002]
all_years = years + [2003] + [2004, 2005]
print(all_years)

# Not Functional - DICT
ages = {"John": 30}
ages["Mary"] = 28
print(ages) # {‘John’: 30, ‘Mary’: 28}

"""
Concatenar dicionários em Python não é tão fácil quanto strings, tuplas ou listas.
Havia um método mais fácil no Python 2.7, mas ele não funciona mais no Python 3.
ages = {"John": 30}
all_ages = dict(ages.items() + {"Mary": 28}.items())
A partir do 3.5 (PEP 448) foi proposto isto
z = {**a, **b}
"""
# Functional
#all_ages = {} #declaring a empty dictionary first
ages = {"John": 30}
all_ages = dict(ages, **{"Mary": 28})
#for x in (ages,{"Mary": 28}): all_ages.update(x)
print(all_ages) # {‘John’: 30, ‘Mary’: 28}


