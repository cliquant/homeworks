import math

print("P1-1 Niks A.")

try:
    a = float(input("Ievadi trijstūra malu a: "))
    b = float(input("Ievadi trijstūra malu b: "))
    c = float(input("Ievadi trijstūra malu c: "))

    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"Trijstūra laukums ir: {round(S, 3)}")
    else:
        print("Šāds trijstūris neeksistē.")
except ValueError:
    print("Lūdzu ievadi derīgus skaitļus.")
except Exception as e:
    print(f"Neizdevās aprēķināt: {e}")
