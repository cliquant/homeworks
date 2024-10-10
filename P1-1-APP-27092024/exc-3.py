print("P1-1 Niks A.")

try:
    n = float(input("Ievadiet stundu skaitu: "))
    m = n * 60
    print(f"{m} minūtes ir {m / 60} stundās.")
except ValueError:
    print("Kļūda: Lūdzu ievadiet derīgu skaitli.")
