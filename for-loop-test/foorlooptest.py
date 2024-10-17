print("Välkommen till det bästa programmet i världen där du nämner saker du ÄLSKAR!!")

running = True

favorite_items = []

while running:
    choice = input("Vad vill du göra? \n[1] Skriv ut\n[2] Lägg till FAVORIT sak!!\n[3] Avlsuta \n")
    if choice == "1":
        for item in favorite_items:
            print(item)
    elif choice == "2":
        choice = input("Skriv in namnet på en ny FAVORITSAK: ")

        favorite_items.append(choice)
    elif choice == "3":
        running = False
        print("Tack för att du använda DETTA FANTASTISKA PROGRAM!!!")
        