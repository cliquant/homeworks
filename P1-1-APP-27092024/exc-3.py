print("P1-1 Niks A.")

def htm():
    try:
        n = float(input("Ievadiet stundu skaitu: "))
        minutes = n * 60
        return minutes
    except ValueError:
        print("Kļūda: Lūdzu ievadiet derīgu skaitli.")
        return None

minutes = htm()

if minutes is not None:
    print(f"{minutes} minūtes ir {minutes / 60} stundās.")
