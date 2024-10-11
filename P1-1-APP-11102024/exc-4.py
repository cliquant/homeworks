print("P1-1 Niks A.\n")

try:
    summa = input("Lūdzu, ievadiet pirkuma summu (EUR): ")
    summa = float(summa)

    atlaide = 0.0

    if summa >= 500:
        atlaide = 0.25
    elif summa >= 200:
        atlaide = 0.15

    maksajama_summa = summa * (1 - atlaide)
    print("Jums jāmaksā: {:.2f} EUR".format(maksajama_summa))

except ValueError:
    print("Kļūda: Lūdzu, ievadiet derīgu skaitli.")
