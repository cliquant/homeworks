import math
print("P1-1 Niks A.")

try:
    try:
        D = float(input("Ievadiet ārējo diametru (D): "))
        d = float(input("Ievadiet iekšējo diametru (d): "))

        R = D / 2
        r = d / 2

        S = math.pi * (R**2 - r**2)

        print(f"Gredzena laukums ir: {S:.2f}")
    except ValueError:
        print("Lūdzu ievadi valid float skaitli lai aprēķinātu.")
except Exception as e:
    print(f"Neizdevās aprēķināt: {r}")
