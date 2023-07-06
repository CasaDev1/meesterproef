import random
from lingowords import words
from termcolor import colored

def get_random_woord(words):
    return random.choice(words)

def get_1e_letter(geselecteerde_woord):
    eerste_letter = geselecteerde_woord[0]
    return eerste_letter


while True:
    print('Welkom bij Lingo!')
    print("Type een woord met 5 letters en druk op Enter!\n")

    woord = get_random_woord(words)
    eerste_letter = get_1e_letter(woord)
    print(eerste_letter)

    opnieuw_spelen = ""


    for poging in range(1,6):
        while True:
            raad = input(f"Poging {poging}: ").lower()
            if len(raad) == 5:
                break
            else:
                print("Het woord moet precies 5 letters lang zijn!")

        correcte_woord = list('-' * 5)
        nieuw_woord = list(woord)
        raad_woord = list(raad)

        for w in range(5):
            if raad_woord[w] == nieuw_woord[w]:
                correcte_woord[w] = colored(raad_woord[w], 'green')

                nieuw_woord[w] = ' '
                raad_woord[w] = ' '

        for w in range(5):
            if raad_woord[w] in nieuw_woord and raad_woord[w] != ' ':
                p = nieuw_woord.index(raad_woord[w])
                correcte_woord[w] = colored(raad_woord[w], 'yellow')
                nieuw_woord[p] = ' '
        
        
        print(''.join(correcte_woord))

        if raad_woord == woord:
            print(colored(f"Gefeliciteerd! Je hebt het woord geraden in poging {poging} !", 'red'))
            break

        if poging == 5:
            print(colored(f"Helaas, je hebt het woord niet geraden. Het woord was '{woord}'.", 'red'))

    opnieuw_spelen = input("Wil je opnieuw spelen? Typ 'q' om af te sluiten of druk op Enter om opnieuw te spelen!.\n")
    if opnieuw_spelen.lower() == 'q':
        break