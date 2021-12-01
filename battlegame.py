wizard = "Wizard"
wizard_hp = 70 
wizard_damage = 150

elf = "Elf"
elf_hp = 100
elf_damage = 100

human = "Human"
human_hp = 150
human_damage = 20

orc = "Orc"
orc_hp = 200
orc_dmg = 75

dragon = "Dragon"
dragon_hp = 300
dragon_damage = 50

while True:
    print("1. Wizard")
    print("2. Elf")
    print("3. Human")
    print("4. Orc")
    print("5. Exit the game")
    option = input("Choose your character:").lower()
    if option == "1" or option == "wizard":
        character = wizard 
        my_hp = wizard_hp
        my_damage = wizard_damage
        print("You have chosen Wizard!")
        print("Health: 70", "Damage: 150")
        break
    if option == "2" or option =="elf":
        character = elf 
        my_hp = elf_hp
        my_damage = elf_damage
        print("You have chosen elf!")
        print("Health: 100", "Damage: 100")
        break
    if option == "3" or option == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        print("You have chosen Human!")
        print("Health: 150", "Damage: 20")
        break
    if option == "4" or option == "orc":
        character = orc
        my_hp = orc_hp
        my_damage = orc_dmg
        print("You have chosen Orc!")
        print("Health: 200, Damage: 75")
        break
    if option == "5" or option == "exit":
        quit()
    else: print("Unknown character")
while True:

    dragon_hp = dragon_hp - my_damage
    print("The", str(character), "damaged the Dragon for", str(my_damage) + "!")
    if dragon_hp >= 0:
        print("The Dragon's hitpoints are now:", str(dragon_hp) + "!")
    if dragon_hp <= 0:
        print("The Dragon has been felled!")
        break
    my_hp = my_hp - dragon_damage
    print("The", str(character), "took", str(dragon_damage), "damage from the Dragon!")
    if my_hp >= 0:
        print("The", str(character) + "'s", "hitpoints are now:", str(my_hp) + "!")
    if my_hp <= 0:
        print("You have fallen in battle :(")
        break

