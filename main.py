import random

gameloop = True

hodnoty = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

barvy = ["♥", "♦", "♠", "♠"]

zetony = 250


# vytvoreni balicku
balicek = [{"barva": barva, "hodnota": hodnota} for barva in barvy for hodnota in hodnoty]

# zamichani balicku
random.shuffle(balicek)


def scitani_karet(karty):
    celkem = 0
    for karta in karty:
        if karta["hodnota"] in ["J", "Q", "K"]:
            celkem += 10
        elif karta["hodnota"] == "A":
            celkem += 11
        else:
            celkem += int(karta["hodnota"])
    return celkem


# zadani prezdivky
nickname = input("Zvolte prezdivku: ")
while gameloop and zetony > 0:
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
            zetony = zetony - int(sazka)
            break

    karty_hrace = [balicek.pop(0), balicek.pop(1)]
    karty_dealera = [balicek.pop(0), balicek.pop(0)]
    print("Karty hrace: " + str(karty_hrace) + " Celkem: " + str(scitani_karet(karty_hrace)))
    print("Karty dealera: " + str(karty_dealera[0]) + ", X " + "Celkem: " + karty_dealera[0]["hodnota"])
    print(scitani_karet(karty_dealera))
    if scitani_karet(karty_hrace) == 21:
        if scitani_karet(karty_dealera) == 21:
            zetony = zetony + int(sazka)
            print("Mas blackjack, ale dealer taky")
        else:
            zetony = zetony + int(sazka) * 2.5
            print("Mas blackjack, vyhral jsi")
    else:
        while True:
            vyber_akce = input("Chceš hrát dál (hit) nebo stát (stand): ")
            if vyber_akce == "hit":
                karty_hrace += [balicek.pop()]
                print("Karty: " + str(karty_hrace) + " Celkem hodnota: " + str(scitani_karet(karty_hrace)))
                if scitani_karet(karty_hrace) > 21:
                    print("Bohuzel, prohral jsi")
                    zetony = zetony - int(sazka)
                    break
            elif vyber_akce == "stand":
                if scitani_karet(karty_dealera) < 17:
                    karty_dealera += [balicek.pop()]
                    soucet_dealera = scitani_karet(karty_dealera)
                    print(soucet_dealera)
                    if scitani_karet(karty_dealera) > 21:
                        print("Vyhral jsi, dealer měl: " + str(karty_dealera) + " Celkem hodnota: " + str(scitani_karet(karty_dealera)))
                        zetony = zetony + int(sazka) * 2
                        break
                    elif soucet_dealera == scitani_karet(karty_hrace):
                        print("Mas stejnou hodnotu jako dealer, zetony se ti vraci")
                        zetony = zetony + int(sazka)
                    elif soucet_dealera > scitani_karet(karty_hrace):
                        print("Bohuzel, prohral jsi, dealer měl: " + str(karty_dealera) + " Celkem hodnota: " + str(scitani_karet(karty_dealera)))
                        zetony = zetony - int(sazka)
                        break
                    else:
                        print("Vyhral jsi, dealer měl: " + str(karty_dealera) + " Celkem hodnota: " + str(scitani_karet(karty_dealera)))
                        zetony = zetony + int(sazka) * 2
                        break
                else:
                    if scitani_karet(karty_dealera) > 21:
                        print("Vyhral jsi, dealer měl: " + str(karty_dealera) + " Celkem hodnota: " + str(
                            scitani_karet(karty_dealera)))
                        zetony = zetony + int(sazka)
                        break
                    elif scitani_karet(karty_dealera) == scitani_karet(karty_hrace):
                        print("Mas stejnou hodnotu jako dealer, zetony se ti vraci")
                        zetony = zetony + int(sazka)
                    elif scitani_karet(karty_dealera) > scitani_karet(karty_hrace):
                        print("Bohuzel, prohral jsi, dealer měl: " + str(karty_dealera) + " Celkem hodnota: " + str(scitani_karet(karty_dealera)))
                        zetony = zetony - int(sazka)
                        break
                    else:
                        print("Vyhral jsi, dealer měl: " + str(karty_dealera) + " Celkem hodnota: " + str(scitani_karet(karty_dealera)))
                        zetony = zetony + int(sazka) * 2
                        break
            else:
                break
