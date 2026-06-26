mi_variable = "hola mundo"
mi_segunda_variable = "Hola mundo"
mi_bool = mi_variable == mi_segunda_variable

print(f"""
mi_variable = "{mi_variable}" {type(mi_variable)}
mi_segunda_variable = "{mi_segunda_variable}" {type(mi_segunda_variable)}
mi_bool = {mi_variable} == {mi_segunda_variable} {mi_bool} {type(mi_bool)}""")

mi_variable = 10
mi_segunda_variable = 6 + 4
mi_bool = mi_variable == mi_segunda_variable

print(f"""
mi_variable = {mi_variable} {type(mi_variable)}
mi_segunda_variable = {mi_segunda_variable} {type(mi_segunda_variable)}
mi_bool = {mi_variable} == {mi_segunda_variable} {mi_bool} {type(mi_bool)}""")

mi_variable = 10
mi_segunda_variable = "10"
mi_bool = mi_variable == mi_segunda_variable

print(f"""
mi_variable = {mi_variable} {type(mi_variable)}
mi_segunda_variable = {mi_segunda_variable} {type(mi_segunda_variable)}
mi_bool = {mi_variable} == {mi_segunda_variable} {mi_bool} {type(mi_bool)}""")

# A pesar de ser distintos tipos siguen siendo números y este caso el mismo número
mi_variable = 10
mi_segunda_variable = 10.0
mi_bool = mi_variable == mi_segunda_variable

print(f"""
mi_variable = {mi_variable} {type(mi_variable)}
mi_segunda_variable = {mi_segunda_variable} {type(mi_segunda_variable)}
mi_bool = {mi_variable} == {mi_segunda_variable} {mi_bool} {type(mi_bool)}""")

# ── != diferente a ────────────────────────────────────────────────────────────
mi_bool = 5 != 6
print(f"\n5 != 6  →  {mi_bool} {type(mi_bool)}")

mi_bool = 5 != 5
print(f"5 != 5  →  {mi_bool} {type(mi_bool)}")

# ── > mayor que ───────────────────────────────────────────────────────────────
mi_bool = 10 > 6
print(f"\n10 > 6  →  {mi_bool} {type(mi_bool)}")

mi_bool = 6 > 10
print(f"6 > 10  →  {mi_bool} {type(mi_bool)}")

# ── < menor que ───────────────────────────────────────────────────────────────
mi_bool = 5 < 6
print(f"\n5 < 6   →  {mi_bool} {type(mi_bool)}")

mi_bool = 6 < 5
print(f"6 < 5   →  {mi_bool} {type(mi_bool)}")

# ── >= mayor o igual que ──────────────────────────────────────────────────────
mi_bool = 5 >= 6
print(f"\n5 >= 6  →  {mi_bool} {type(mi_bool)}")

mi_bool = 6 >= 6
print(f"6 >= 6  →  {mi_bool} {type(mi_bool)}")

# ── <= menor o igual que ──────────────────────────────────────────────────────
mi_bool = 5 <= 6
print(f"\n5 <= 6  →  {mi_bool} {type(mi_bool)}")

mi_bool = 6 <= 5
print(f"6 <= 5  →  {mi_bool} {type(mi_bool)}")

# ── con expresiones ───────────────────────────────────────────────────────────
mi_bool = 10 == 2 * 5
print(f"\n10 == 2*5  →  {mi_bool} {type(mi_bool)}")