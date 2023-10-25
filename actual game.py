import random
import math

# define all vars
player_maxhealth = 10
player_health = 10
player_damage = 2
slimehealth = int(random.randint(5, 7))
slimedamage = int(random.randint(2, 3))

print("Welcome to my game.")

# import stats
def stats(player_health, player_damage):
    view_stats = input("Would you like to view your stats (y/n)?: ")
    if view_stats == 'y':
        print("Your health is: " , str(player_health))
        print("Your damage is: " , str(player_damage))
    elif view_stats == 'n':
        pass
# import slime
def slime_attack(slimehealth, player_health, player_damage, slimedamage):
    print("You encounter a slime!")
    print("The slime's dmg is: " + str(slimedamage))
    while slimehealth >= 0:
        print("The slime's hp is: " + str(slimehealth))
        slime_input = input("Would you like to attack the slime? (y/n): ")

        if slime_input[0].lower() == 'y':
            print("You attacked the slime for " + str(player_damage))
            slimehealth -= player_damage  # Update the slime's health
            print("The slime's health is now: " + str(slimehealth))
            print("The slime attacked you for:" + str(slimedamage))
            player_health -= slimedamage
        elif slime_input[0].lower() == 'n':
            print("The slime attacked you for:" + str(slimedamage))
        else:
            print("Invalid input, detecting you would attack.")

    if slimehealth <= 0:
        print("You win!")
        print("You have been healed to" + str(player_maxhealth) + "Health!")
        player_health = player_maxhealth
        # rerolling the slime stats
        slimehealth = int(random.randint(5, 7))
        slimedamage = int(random.randint(2, 3))

    else:
        print("You lose!")

# actual game
stats(player_health, player_damage)
slime_attack(slimehealth, player_health, player_damage, slimedamage)









