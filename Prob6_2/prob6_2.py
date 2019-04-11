import Obiect
import os
import time

p = Obiect.Sistem_Demonstratii()

while True:
        print("Scrie 'init' pentru a initializa sistemului de demonstratii")
        print("Scrie 'det' pentru a determina consistenta sistemului de demonstratii")
        print("Scrie 'rationament' pentru a vedea daca o afirmatie este adevarata")
        print("Scrie 'adaugare' pentru a adauga o noua teorema")
        print("Scrie 'stergere' pentru a sterge o teorema")
        print("Scrie 'afisare' pentru a afisa enunturile teoremelor adaugate dar si graful")
        print("Scrie orice altceva pentru a iesii")

        action = input(': ')
        if "init" in action:
            print("Numaratoarea incepe de la 0")
            p.initializare_sistem()
        elif "det" in action:
            p.det()
        elif "rationament" in action:
            start = str(input('Introduceti teorema(nodul de plecare): '))
            end = str(input('Introduceti concluzia(nodul de sosire): '))
            path = p.prove(start, end)
            print("Rationamentele posibile sunt: ",end="")
            print(path)
            path = p.smallest_prove(start, end)
            print("Si rationamentul cel mai scurt este")
            print(path)
        elif "adaugare" in action:
            p.adaugare()
        elif "stergere" in action:
            p.sterge()
        elif "afisare" in action:
            p.afisare()
        else:
            break
        print()
        input('Press enter to continue...')
        os.system('cls')
