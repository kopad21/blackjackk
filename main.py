import random

gameloop = True

hodnoty = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

barvy = ["♥", "♦", "♠", "♠"]

zetony = 250

celkem_hrac = 0

celkem_dealer = 0

# vytvoreni balicku
balicek = [{"barva": barva, "hodnota": hodnota} for barva in barvy for hodnota in hodnoty]

# zamichani balicku
random.shuffle(balicek)

# zadani prezdivky
nickname = input("Zvolte prezdivku: ")
while gameloop:
    # vklad sazky
    sazka = input("Mate " + str(zetony) + " zetonu" + "\nZadejte pocet zetonu pro sazku: ")
    while True:
        if not sazka.isdigit():
            print("Zadana hodnota neni cislo")
            sazka = input("Zadejte pocet zetonu pro sazku: ")
        elif int(sazka) > zetony:
            print("Nemuzete vsadit vic nez mate zetonu, mate " + str(zetony) + " zetonu")
            sazka = input("Zadejte pocet zetonu pro sazku:")
        elif int(sazka) <= 0:
            print("Musite zadat sazku vetsi nez 0")
            sazka = input("Zadejte pocet zetonu pro sazku: ")
        else:
            break

    karty_hrace_nove = [balicek.pop(0)["hodnota"]]
    karty_hrace = [balicek.pop(0), balicek.pop(1)]
    for karty in karty_hrace:
        if karty["hodnota"] in ["J", "Q", "K"]:
            celkem_hrac += 10
        elif karty["hodnota"] == "A":
            celkem_hrac += 11
        else:
            celkem_hrac += int(karty["hodnota"])
    karty_dealera = [balicek.pop(0), balicek.pop(0)]
    print("Karty hrace: " + str(karty_hrace) + "Celkem: " + str(celkem_hrac))
    print("Karty dealera: " + str(karty_dealera[0]) + ", X " + "Celkem: " + karty_dealera[0]["hodnota"])
    vyber_akce = input("Chceš hrát dál (hit) nebo stát (stand): ")
    if vyber_akce == "hit":
        karty_hrace += [balicek.pop(0)]
        celkem_hrac += karty_hrace["hodnota"]
        print(karty_hrace)
    elif vyber_akce == "stand":
        pass
    else:
        pass
