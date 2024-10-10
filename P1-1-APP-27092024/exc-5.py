print("P1-1 Niks A.")

def convert(days):
    return days * 24 * 60 * 60

try:
    user = input("Ievadi skaitli, lai aprēķinātu: ")
    r = None
    try:
        r = int(user)
        end = convert(r)
        print(f"{user} diena/s ir: {end}s")
    except ValueError:
        print("Lūdzu ievadi valid skaitli lai aprēķinātu.")

except Exception as e:
    print(f"Neizdevās aprēķināt: {r}")
