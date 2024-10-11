print("P1-1 Niks A.\n")

try:
    skaitlis = input("Lūdzu, ievadiet skaitli: ")
    skaitlis = int(skaitlis)

    dienas = {
        1: "Pirmdiena",
        2: "Otrdiena",
        3: "Trešdiena",
        4: "Ceturdiena",
        5: "Piektdiena",
        6: "Sestdiena",
        7: "Svētdiena"
    }

    if skaitlis > 1 and skaitlis < 7:
        if skaitlis in dienas:
            print(dienas[skaitlis])
        else:
            print("Kļūda!")
    else:
        print("Kļūda!")
except ValueError:
    print("Kļūda: Lūdzu, ievadiet derīgu skaitli.")
