print("P1-1 Niks A.")

try:
    num1 = float(input("Ievadiet pirmo skaitli: "))
    num2 = float(input("Ievadiet otro skaitli: "))
    num3 = float(input("Ievadiet trešo skaitli: "))

    average = (num1 + num2 + num3) / 3
    print(f"Vidējā aritmētiskā vērtība ir: {average}")
except ValueError:
    print("Kļūda: Lūdzu ievadiet derīgus skaitļus.")
