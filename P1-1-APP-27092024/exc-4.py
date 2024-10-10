print("P1-1 Niks A.")


def average():
    try:
        num1 = float(input("Ievadiet pirmo skaitli: "))
        num2 = float(input("Ievadiet otro skaitli: "))
        num3 = float(input("Ievadiet trešo skaitli: "))

        average = (num1 + num2 + num3) / 3
        return average
    except ValueError:
        print("Kļūda: Lūdzu ievadiet derīgus skaitļus.")
        return None


end = average()

if end is not None:
    print(f"Vidējā aritmētiskā vērtība ir: {end}")
