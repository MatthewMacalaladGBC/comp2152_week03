import random

# Dice setup using list() and range()
diceOptions = list(range(1, 7))

# Weapons array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

print("Available Weapons:", ', '.join(weapons))

# Input combat strength
combatStrength = int(input("Enter your combat strength (1-6): "))
if combatStrength < 1 or combatStrength > 6:
    print("Invalid input! Combat strength should be between 1 and 6.")
    combatStrength = 1 # Default value for invalid combatStrength input

# Input monster's combat strength
mCombatStrength = int(input("Enter monster's combat strength (1-6): "))
if mCombatStrength < 1 or mCombatStrength > 6:
    print("Invalid input! Monster;s combat strength should be between 1 and 6.")
    mCombatStrength = 1 # Default value for invalid mCombatStrength input

# Simulate Battle rounds
for j in range(1, 21, 2):
    # Dice rolls for hero and monster
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    # Weapon name for hero and monster
    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    # Calculate total strengths
    heroTotal = combatStrength + heroRoll
    monsterTotal = mCombatStrength + monsterRoll

    # Print round details
    print(f"\n Round {j}: Hero rolled {heroRoll}, Monster rolled {monsterRoll}.")
    print(f"Hero selected: {heroWeapon}, Monster selected {monsterWeapon}.")
    print(f"Hero total strength: {heroTotal}, Monster total strength: {monsterTotal}.")
