bestelling = ""
totaal_bedrag = 0.0
doorgaan = True

while doorgaan:
    print("\nWelkom bij McDonald's, wat wil je bestellen?")
    print("1. Eten")
    print("2. Drinken")
    print("3. Menu")
    print("4. Betalen en afsluiten")

    keuze = input("Maak uw keuze (1-4): ")

    if keuze == "1":
        print("\nEten opties:")
        print("a. Hamburger (€3.00)")
        print("b. Cheeseburger (€3.50)")
        print("c. Chicken Nuggets (€4.00)")
        keuze_eten = input("Kies een optie (a-c): ")
        if keuze_eten == "a":
            bestelling += "Hamburger, "
            totaal_bedrag += 3.00
        elif keuze_eten == "b":
            bestelling += "Cheeseburger, "
            totaal_bedrag += 3.50
        elif keuze_eten == "c":
            bestelling += "Chicken Nuggets, "
            totaal_bedrag += 4.00
        else:
            print("Ongeldige keuze voor eten.")

    elif keuze == "2":
        print("\nDrinken opties:")
        print("a. Cola (€2.00)")
        print("b. Fanta (€2.00)")
        print("c. Water (€1.50)")
        keuze_drank = input("Kies een optie (a-c): ")
        if keuze_drank == "a":
            bestelling += "Cola, "
            totaal_bedrag += 2.00
        elif keuze_drank == "b":
            bestelling += "Fanta, "
            totaal_bedrag += 2.00
        elif keuze_drank == "c":
            bestelling += "Water, "
            totaal_bedrag += 1.50
        else:
            print("Ongeldige keuze voor drinken.")

    elif keuze == "3":
        print("\nMenu opties:")
        print("a. Big Mac Menu (€7.50)")
        print("b. McChicken Menu (€7.00)")
        print("c. Vegan Menu (€6.50)")
        keuze_menu = input("Kies een optie (a-c): ")
        if keuze_menu == "a":
            bestelling += "Big Mac Menu, "
            totaal_bedrag += 7.50
        elif keuze_menu == "b":
            bestelling += "McChicken Menu, "
            totaal_bedrag += 7.00
        elif keuze_menu == "c":
            bestelling += "Vegan Menu, "
            totaal_bedrag += 6.50
        else:
            print("Ongeldige keuze voor menu.")

    elif keuze == "4":
        doorgaan = False
    else:
        print("Ongeldige invoer. Probeer opnieuw.")

# Bestelling afronden
print("\n--- Uw Bestelling ---")
if bestelling != "":
    print("Items: " + bestelling.strip(", "))
else:
    print("U heeft niets besteld.")
print(f"Totaal te betalen: €{totaal_bedrag:.2f}")
print("Bedankt voor uw bestelling!")