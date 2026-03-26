import random
import re

#       PLAYER!
player = {
    "hp": 100,
    "max_hp": 100,
    "energy": 5,
    "max_energy": 7,
    "status": {"poison": 0, "stun": 0}
}

#       CARDS!
cards = [
    {"name": "Strike", "damage": 10, "cost": 2},
    {"name": "Quick Slash", "damage": 12, "cost": 2},
    {"name": "Venom Slash", "damage": 18, "cost": 3, "poison": 3},
    {"name": "Thousand Myriad Blades", "damage": 35, "cost": 4}
]

#       ENEMIES!
enemies = [
    {"name": "Bandit Scout", "hp": 45, "damage": 8, "elite": False},
    {"name": "Controlled Wolf", "hp": 35, "damage": 9, "elite": False},
    {"name": "Elite Enforcer", "hp": 90, "damage": 14, "elite": True}
]

#       FUNCTIONS!

def wait():
    input("\n(Press Enter to continue...)")

def intro():
    print("You, a hero, are camping in a peaceful Village...")
    wait()
    print("Your instincts activate... something feels wrong.")
    wait()
    print("Bandits rush in with controlled monsters...\n")
    wait()

def show_energy():
    print("Energy:", "⚡️" * player["energy"], f"({player['energy']}/7)")

def draw_cards():
    return random.sample(cards, 3)

def inspect_enemy(enemy):
    print("\nEnemy:", enemy["name"])
    print("HP:", enemy["hp"])
    print("Damage:", enemy["damage"])

def inspect_card(hand, index):
    if 0 <= index < len(hand):
        card = hand[index]
        print(f"\n{card['name']}:")
        print("Damage:", card["damage"])
        print("Cost:", card["cost"])

#       STATUS EFFECTS
def apply_status(entity, name):
    if entity["status"]["poison"] > 0:
        entity["hp"] -= 3
        entity["status"]["poison"] -= 1
        print(name, "takes 3 poison damage!")

    if entity["status"]["stun"] > 0:
        entity["status"]["stun"] -= 1
        print(name, "is stunned!")
        return True

    return False

def player_turn(enemy):
    hand = draw_cards()

    print("\nYour cards:")
    for i, card in enumerate(hand):
        print(f"{i+1}. {card['name']} (Cost {card['cost']})")

    while True:
        command = input("\nCommand: ").lower()

        match = re.match(r"(use|u)\s*(\d+)", command)
        if match:
            choice = int(match.group(2)) - 1

            if 0 <= choice < len(hand):
                card = hand[choice]

                if player["energy"] >= card["cost"]:
                    player["energy"] -= card["cost"]
                    enemy["hp"] -= card["damage"]

                    print(f"You used {card['name']} for {card['damage']} damage!!!")

                    if "poison" in card:
                        enemy["status"]["poison"] += card["poison"]
                        print("Enemy is poisoned!")

                    return
                else:
                    print("Not enough energy!")
            else:
                print("Invalid Card Number!!")

        elif re.match(r"inspect enemy", command):
            inspect_enemy(enemy)

        elif re.match(r"inspect (\d+)", command):
            idx = int(re.match(r"inspect (\d+)", command).group(1)) - 1
            inspect_card(hand, idx)

        elif re.match(r"skip", command):
            print("You skipped your turn.")
            return

        else:
            print("Invalid command.")

def enemy_turn(enemy):
    roll = random.randint(1, 100)

    if enemy["elite"] and roll <= 30:
        dmg = enemy["damage"] + 6
        print(enemy["name"], "uses Heavy Slam!")
    elif roll <= 25:
        dmg = enemy["damage"] + 3
        print(enemy["name"], "uses Quick Strike!")
    else:
        dmg = enemy["damage"]

    player["hp"] -= dmg
    print(enemy["name"], "deals", dmg, "damage!")

def new_turn():
    player["energy"] = min(player["energy"] + 2, player["max_energy"])

def loot():
    print("\nSearching loot...")
    if random.randint(1, 100) <= 30:
        new_card = random.choice(cards)
        print("You found a new skill:", new_card["name"])
    else:
        print("Nothing useful found.")

def battle():
    enemy_template = random.choice(enemies)

    # clone enemy so stats reset
    enemy = {
        "name": enemy_template["name"],
        "hp": enemy_template["hp"],
        "damage": enemy_template["damage"],
        "elite": enemy_template["elite"],
        "status": {"poison": 0, "stun": 0}
    }

    print("\nA", enemy["name"], "appears!")

    if enemy["elite"]:
        print("⚠️ ELITE ENEMY ⚠️")

    turn = 1

    while player["hp"] > 0 and enemy["hp"] > 0:

        print("\n--- Turn", turn, "---")
        print("Player HP:", player["hp"])
        print("Enemy HP:", enemy["hp"])

        show_energy()

        # PLAYER STATUS
        if not apply_status(player, "Player"):
            player_turn(enemy)

        # ✅ CHECK ENEMY DEATH (NOW INSIDE LOOP)
        if enemy["hp"] <= 0:
            print("Enemy defeated!")

            # rewards
            player["energy"] = min(player["energy"] + 4, player["max_energy"])
            player["hp"] = min(player["hp"] + 20, player["max_hp"])

            print("You gained 4 energy ⚡ and 20 HP ❤️!")
            loot()
            return

        # ENEMY STATUS
        if not apply_status(enemy, enemy["name"]):
            enemy_turn(enemy)

        # PLAYER DEATH CHECK
        if player["hp"] <= 0:
            print("You were defeated...")
            return

        new_turn()
        turn += 1

def game():
    intro()

    fights = 3

    for i in range(fights):
        print(f"\n--- Encounter {i+1} ---")
        battle()

        if player["hp"] <= 0:
            print("Game Over.")
            return

        wait()

    print("\nYou defended the village...")
    wait() 
    print("But something deeper and sinister controls the monsters...")
    wait()
    print("It is up to you HERO, to find out the root of this chaos!")
    wait()
    print("THANKS FOR PLAYING! IK ITS SHORT BUT ITS ALOT HAHA")
    
# --- START ---

game()



