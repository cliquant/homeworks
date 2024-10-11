print("P1-1 Niks A.\n")

try:
    skaitlis = input("Lūdzu, ievadiet skaitli: ")
    skaitlis = int(skaitlis)

    if skaitlis % 2 == 0:
        print("Skaitlis ir pāra.")
    else:
        print("Skaitlis ir nepāra.")
except ValueError:
    print("Kļūda: Lūdzu, ievadiet derīgu skaitli.")
