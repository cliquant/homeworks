print("P1-1 Niks A.")

try:
    user = input("Ievadi skaitli, lai aprēķinātu: ")
    r = None
    try:
        r = float(user)
        pi = 3.14
        c = 2 * pi * r
        print(f"Atbilde: {c}")
    except ValueError:
        print("Lūdzu ievadi valid skaitli lai aprēķinātu.")

except Exception as e:
    print(f"Neizdevās aprēķināt: {r}")
