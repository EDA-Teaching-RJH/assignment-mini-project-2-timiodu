import random
import re

#       PLAYER!
player = {
    "hp": 100,
    "max_hp": 100,
    "energy": 5,
    "max_energy": 7
}
#       CARDS!
cards = [
    {"name": "Strike", "damage": 10, "cost": 2},
    {"name": "Quick Slash", "damage": 12, "cost": 2},
    {"name": "Venom Slash", "damage": 18, "cost": 3},
    {"name": "Thousand Myriad Blades", "damage": 35, "cost": 4}
]
#       ENEMIES!
enemies = [
    {"name": "Bandit Scout", "hp": 45, "damage": 8, "elite": False },
    {"name": "Controlled Wolf", "hp": 35, "damage": 9, "elite": False},
    {"name": "Elite ", "hp": 90, "damage": 14, "elite": True}
]
#       FOR THE FUNCTIONS!
def intro():
    print("You, a hero, is camping in a peaceful Village...")
    print("Your heightened instincts start to activate out of nowhere, you feel uneasy.")
    print("Bandits rush towards the village, with somewhat obidient and controlled monsters???\n")
def show_energy():
    print("Energy:", "⚡️" * player["energy"], f"({player['energy']}/7)")
def draw_cards():
    return random.sample(cards,3)
def inspect_enemy(enemy):
    print("\nEnemy:", enemy["name"])
    print("HP", enemy["hp"])
    print("Damage", enemy["damage"])
def inspect_card(hand, index):
    if 0 <= index < len(hand):
        card = hand[index]
        print(f"\n{card['name']}:")
        print("Damage:", card["damage"])
        print("Cost:", card["cost"])
def player_turn(enemy):
    hand = draw_cards()
    print("\nYour cards:")
    for i, card in enumerate(hand):
        print(f"{i+1}. {card['name']} (Cost {card['cost']})")
    while True:
        command = input("\nCommand: ").lower()

#               FOR THE USES OF CARDS ONE AFTER ANOTHER!!
        match = re.match(r"(use|u)\s*(\d+)", command)
        if match:
            choice = int(match.group(2)) -1
            if 0 <= choice < len(hand):
                card = hand[choice]

                if player["energy"] >= card["cost"]:
                    player["energy"] -= card["cost"]
                    enemy["hp"] -= card["damage"]
                    print(f"You used {card['name']} for {card['damage']} damage!!!")
                    return
                else: print("Not enough energy!")
            else: 
                print("Invalid Card Number!!")
#               If u wanna inspect ur enemy!
        elif re.match(r"inspect enemy", command):
            inspect_enemy(hand, idx)
#               Inspect ur cards!
        elif re.match(r"inspect (\d+)", command):
            idx = int(re.match(r"inspect (\d+)", command).group(1)) - 1
            inspect_card(hand, idx)

        # skip turn
        elif re.match(r"skip", command):
            print("You skipped your turn.")
            return

        else:
            print("Invalid command.")


