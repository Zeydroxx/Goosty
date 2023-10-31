from random import randint

banner = """
   ________                           
  /  _____/   ____    ____    _______/  |_  ___.__.
 /   \  ___  /  _ \  /  _ \  /  ___/\   __\<   |  |
 \    \_\  \(  <_> )(  <_> ) \___ \  |  |   \___  |
  \______  / \____/  \____/ /____  > |__|   / ____|
         \/                      \/         \/     
                                by Zeydroxx
"""

print(banner)

def play():
    mode = input("Select Your Mode to Play : \n - (H)ard (1000 numbers in 10) \n - (N)ormal (500 in 10) \n - (E)asy (100 in 10) \n - (Q)uit --->")
    dico = {"H": 1000, "N": 500, "E": 100}
    if mode in ["H", "N", "E", "h", "n", "e", "Q", "q"]:
        if mode == "Q" or mode == "q":
            print("Le Jeu Est Quitté. Fait par Zeydroxx")
        else:
            max = dico.get(mode)
            number = generate(max)
            print(f"Le Nombre est compris entre 0 et {max}")
            tours = 0
            while tours < 10:
                try:
                    choice = int(input("What is Your Number --> "))
                except ValueError:
                    print("Mettez un nombre valide s'il vous plaît.")
                    continue  # Revenir au début de la boucle
                if choice > number:
                    print("Le nombre est Plus Petit")
                elif choice < number:
                    print("Le Nombre est plus Grand")
                elif choice == number:
                    bravo = f"Bravo tu as gagné le jeu en {tours} tours. Si tu veux rejouer, relance le programme."
                    print(bravo)
                    input("Appuie sur n'importe quelle touche pour quitter.")
                    break  # Sortir de la boucle while
                tours = tours + 1
            else:
                print(f"Vous avez dépassé les 10 tentatives. Le nombre était {number}. Vous avez perdu.")
                input("Appuie sur Entrer pour quitter.")
    else:
        print("*** Incorrect Value ***")
        play()

def generate(max):
    return randint(0, max)

if __name__ == "__main__":
    play()
