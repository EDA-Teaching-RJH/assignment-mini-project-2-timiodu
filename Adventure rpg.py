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
    {"name": "Bandit Scout", "hp": 90, "damage": 14, "elite": True}
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


