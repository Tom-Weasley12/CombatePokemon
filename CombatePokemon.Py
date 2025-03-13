from random import randint
import os

BARRA_DE_VIDA = 20
VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

while vida_pikachu > 0 and vida_squirtle > 0:
    # Se desenvuelven los turnos del combate

    # Turno de Pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        # Bola Voltio
        print("Pikachu ataca con Bola Voltio")
        vida_squirtle -= 10
    else:
        # Honda Trueno
        print("Pikachu ataca con Honda Trueno")
        vida_squirtle -= 11

    if vida_squirtle < 0:
        vida_squirtle = 0

    if vida_pikachu < 0:
        vida_pikachu = 0

    barras_de_vida_pikachu = int(vida_pikachu * BARRA_DE_VIDA / VIDA_INICIAL_PIKACHU)
    print("La vida de Pikachu es [{}{}] ({}/{})".format(
        "*" * barras_de_vida_pikachu, " " * (BARRA_DE_VIDA - barras_de_vida_pikachu),
        vida_pikachu, VIDA_INICIAL_PIKACHU))

    barras_de_vida_squirtle = int(vida_squirtle * BARRA_DE_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("La vida de Squirtle es [{}{}] ({}/{})".format(
        "*" * barras_de_vida_squirtle, " " * (BARRA_DE_VIDA - barras_de_vida_squirtle),
        vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    input("Enter para continuar...\n\n")
    os.system("clear")

    # Turno de Squirtle
    print("Turno de Squirtle")

    ataque_squirtle = None
    while ataque_squirtle not in ["P", "B", "A", "N", ¨V¨]:
        ataque_squirtle = input("¿Qué ataque deseas realizar? [P - Pistola Agua | B - Burbuja | A - Placaje | N - Nada | V - Pocion]: ")

    if ataque_squirtle == "P":
        print("Squirtle ataca con Pistola Agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "V":
        print("Squirtle usa pocion, obtiene 10 puntos de vida")
        vida_squirtle += 10
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja")
        vida_pikachu -= 9
    elif ataque_squirtle == "A":
        print("Squirtle ataca con Placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "N":
        print("Squirtle no hace nada...")

    if vida_squirtle < 0:
        vida_squirtle = 0

    if vida_pikachu < 0:
        vida_pikachu = 0

    barras_de_vida_pikachu = int(vida_pikachu * BARRA_DE_VIDA / VIDA_INICIAL_PIKACHU)
    print("La vida de Pikachu es [{}{}] ({}/{})".format(
        "*" * barras_de_vida_pikachu, " " * (BARRA_DE_VIDA - barras_de_vida_pikachu),
        vida_pikachu, VIDA_INICIAL_PIKACHU))

    barras_de_vida_squirtle = int(vida_squirtle * BARRA_DE_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("La vida de Squirtle es [{}{}] ({}/{})".format(
        "*" * barras_de_vida_squirtle, " " * (BARRA_DE_VIDA - barras_de_vida_squirtle),
        vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    input("Enter para continuar...\n\n")
    os.system("clear")

if vida_pikachu > vida_squirtle:
    print("Pikachu ha ganado")
else:
    print("Squirtle ha ganado")
 
