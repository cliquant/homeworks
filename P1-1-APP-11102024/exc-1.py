import math

print("P1-1 Niks A.\n")

try:
    x = float(input("Lūdzu, ievadiet x vērtību: "))

    if x > 0:
        y = math.sqrt(3 * x * 2)**3 - (24 * x) / (3 * math.sqrt(x)) - (2 / math.sqrt(x))
    else:
        y = (2 * x) - (3 - x) / 4

    print(f"Kad x = {x}, y = {y:.2f}")
except ValueError:
    print("Lūdzu, ievadiet derīgu skaitli.")
