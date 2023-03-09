import random
import csv

# nastavovani zakladnich hodnot

gameloop = False

hodnoty = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

barvy = ["♥", "♦", "♠", "♠"]

zetony = 0


# vytvoreni balicku
balicek = [{"barva": barva, "hodnota": hodnota} for barva in barvy for hodnota in hodnoty]

# zamichani balicku
random.shuffle(balicek)


# funkce na scitani karet
def scitani_karet(karty):
    celkem = 0
    esa = 0
    for karta in karty:
        # pokud je to J, Q nebo K tak se pricte 10
        if karta["hodnota"] in ["J", "Q", "K"]:
            celkem += 10
        # pokud je to eso pricte se 11
        elif karta["hodnota"] == "A":
            celkem += 11
            esa += 1
        # pricte se hodnota co ma karta na sobe
        else:
            celkem += int(karta["hodnota"])
    # pokud ma clovek pres 21 a ma eso tak se odecte 10 = eso ma hodnotu 1
    while celkem > 21 and esa > 0:
        celkem -= 10
        esa -= 1

    return celkem


# vytvoreni menu

while True:
    menu = input("1. Hrat" + "\n2. Zebricek" + "\n3. Pravidla" + "\n4. O hre" + "\n5. Ukoncit\n")

    # pokud napise 1 zepta se ho na jmeno a pousti do hry
    if menu == "1":
        while True:
            nickname = input("Zvolte prezdivku: ")
            if nickname.isalnum():
                break
            else:
                print("Prezdivka muze obsahovat pouze cisla a pismena")
        gameloop = True
        zetony = 250
        break
    # pokud napise 2 zobrazuje leaderboard
    if menu == "2":
        print("IN PROGRESS")
    # pokud napise 3 da link na pravidla blackjacka
    if menu == "3":
        print("https://cs.wikipedia.org/wiki/Blackjack#Pravidla")
    # pokud napise 4 da link o hre blackjack
    if menu == "4":
        print("https://cs.wikipedia.org/wiki/Blackjack")
    # pokud napise 5 ukoncuje hru
    if menu == "5":
        gameloop = False
        break
    else:
        pass


while gameloop and zetony > 0:

    # zapisuje kazde kolo do souboru prezdivku a zetony
    f = open("leaderboard.csv", "a", newline="")
    tup1 = (nickname, zetony)
    writer = csv.writer(f)
    writer.writerow(tup1)

    while True:
        pokracovani = input("Chcete hrat dal? Y/N")
        if pokracovani.lower() == "n":
            quit()
        elif pokracovani.lower() == "y":
            sazka = input("Mate " + str(zetony) + " zetonu" + "\nZadejte pocet zetonu pro sazku: ")
            break
        else:
            pass

    # kontrola jestli je sazka cislo, vetsi nez 1 a neni to vic nez ma k dispozici
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

    # rozdani karet a vypsani kdo ma co za hodnoty, jedna karta dealera je zakryta

    karty_hrace = [balicek.pop(0), balicek.pop(1)]
    karty_dealera = [balicek.pop(0), balicek.pop(0)]
    print("Karty hrace: " + str(karty_hrace) + " Celkem: " + str(scitani_karet(karty_hrace)))
    if karty_dealera[0]["hodnota"] == "J" or karty_dealera[0]["hodnota"] == "Q" or karty_dealera[0]["hodnota"] == "K":
        hodnota_dealer = "10"
    else:
        hodnota_dealer = karty_dealera[0]["hodnota"]
    print("Karty dealera: " + str(karty_dealera[0]) + ", X " + "Celkem: " + hodnota_dealer)
    if scitani_karet(karty_hrace) == 21:
        if scitani_karet(karty_dealera) == 21:
            zetony = zetony + int(sazka)
            print("Mas blackjack, ale dealer taky, remiza")
        else:
            zetony = zetony + int(sazka) * 1.5
            print("Mas blackjack, vyhral jsi")
    elif scitani_karet(karty_dealera) == 21 and scitani_karet(karty_hrace) < 21:
        print("Dealer ma blackjack, prohral jsi")
    else:
        doubledown = ""
        if scitani_karet(karty_hrace) == 10 or scitani_karet(karty_hrace) == 11:
            doubledown = input("Chcete double down? Y/N")
            odpoved = ""
            while not odpoved == "ok":
                if doubledown.lower() == "y":
                    odpoved = "ok"
                    karty_hrace += [balicek.pop()]
                    print(str(karty_hrace) + " Celkem: " + str(scitani_karet(karty_hrace)))
                elif doubledown.lower() == "n":
                    odpoved = "ok"
                else:
                    doubledown = input("Odpovez Y nebo N")
        while True:
            if doubledown.lower() == "y":
                doubledown_sazka = int(sazka) * 2
                if scitani_karet(karty_dealera) < 17:
                    while scitani_karet(karty_dealera) < 17:
                        karty_dealera += [balicek.pop()]
                else:
                    pass
                if scitani_karet(karty_dealera) > scitani_karet(karty_hrace):
                    print("Bohuzel, prohral jsi, dealer měl: " + str(karty_dealera) + " Celkem hodnota: " + str(scitani_karet(karty_dealera)))
                    zetony = zetony - int(sazka)
                    break
                elif scitani_karet(karty_dealera) == scitani_karet(karty_hrace):
                    print("Remiza, dealer měl: " + str(karty_dealera) + " Celkem hodnota: " + str(scitani_karet(karty_dealera)))
                    zetony = zetony + int(sazka)
                    break
                elif scitani_karet(karty_dealera) > 21:
                    print("Vyhral jsi, dealer měl: " + str(karty_dealera) + " Celkem hodnota: " + str(scitani_karet(karty_dealera)))
                    zetony = zetony + int(doubledown_sazka) * 2
                    break
                else:
                    print("Vyhral jsi, dealer měl: " + str(karty_dealera) + " Celkem hodnota: " + str(scitani_karet(karty_dealera)))
                    zetony = zetony + int(doubledown_sazka) * 2
                    break
            else:
                vyber_akce = input("Chceš hrát dál (hit) nebo stát (stand): ")
            if vyber_akce.lower() == "hit":
                karty_hrace += [balicek.pop()]
                print("Karty: " + str(karty_hrace) + " Celkem hodnota: " + str(scitani_karet(karty_hrace)))
                if scitani_karet(karty_hrace) > 21:
                    print("Bohuzel, prohral jsi")
                    break
            elif vyber_akce.lower() == "stand":
                if scitani_karet(karty_dealera) < 17:
                    while scitani_karet(karty_dealera) < 17:
                        karty_dealera += [balicek.pop()]
                    soucet_dealera = scitani_karet(karty_dealera)
                    if scitani_karet(karty_dealera) > 21:
                        print("Vyhral jsi, dealer měl: " + str(karty_dealera) + " Celkem hodnota: " + str(scitani_karet(karty_dealera)))
                        zetony = zetony + int(sazka) * 2
                        break
                    elif soucet_dealera == scitani_karet(karty_hrace):
                        print("Mas stejnou hodnotu jako dealer, zetony se ti vraci")
                        zetony = zetony + int(sazka)
                        break
                    elif soucet_dealera > scitani_karet(karty_hrace):
                        print("Bohuzel, prohral jsi, dealer měl: " + str(karty_dealera) + " Celkem hodnota: " + str(scitani_karet(karty_dealera)))
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
                        break
                    elif scitani_karet(karty_dealera) > scitani_karet(karty_hrace):
                        print("Bohuzel, prohral jsi, dealer měl: " + str(karty_dealera) + " Celkem hodnota: " + str(scitani_karet(karty_dealera)))
                        break
                    else:
                        print("Vyhral jsi, dealer měl: " + str(karty_dealera) + " Celkem hodnota: " + str(scitani_karet(karty_dealera)))
                        zetony = zetony + int(sazka) * 2
                        break
            else:
                pass
