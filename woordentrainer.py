import random
import os

# Engelse woorden met Nederlandse vertaling
woorden = {
    "computer": "computer",
    "keyboard": "toetsenbord",
    "screen": "scherm",
    "software": "software",
    "file": "bestand",
    "program": "programma",
    "network": "netwerk",
    "database": "database",
    "password": "wachtwoord",
    "website": "website"
}

SCORE_BESTAND = "score.txt"


def score_laden():
    """Laad de vorige score uit het bestand."""
    if os.path.exists(SCORE_BESTAND):
        with open(SCORE_BESTAND, "r") as bestand:
            inhoud = bestand.read().strip()
            if inhoud == "":
                return 0
            return int(inhoud)
    return 0


def score_opslaan(score):
    """Sla de huidige score op."""
    with open(SCORE_BESTAND, "w") as bestand:
        bestand.write(str(score))


def woordentrainer():
    score = score_laden()

    print("================================")
    print("       ENGELS-WOORDENTRAINER")
    print("================================")
    print(f"Je huidige score is: {score}")
    print("Typ 'stop' om te stoppen.\n")

    woordenlijst = list(woorden.items())
    random.shuffle(woordenlijst)

    for engels, nederlands in woordenlijst:
        print(f"Wat is de Nederlandse vertaling van: {engels}?")

        antwoord = input("> ").lower().strip()

        if antwoord == "stop":
            break

        if antwoord == nederlands:
            print("Goed gedaan! ✓")
            score += 1
        else:
            print(f"Fout! Het juiste antwoord is: {nederlands}")

        print(f"Score: {score}")
        print()

    score_opslaan(score)

    print("==============================")
    print("De oefening is afgelopen.")
    print(f"Je eindscore is: {score}")
    print("Je score is opgeslagen!")
    print("==============================")


woordentrainer()