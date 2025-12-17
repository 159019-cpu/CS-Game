#This is the base
import random
DAY = 1
health = 100
warmth = 100
hunger = 100
print ("you have 4 options")
print ("click 1 for rest")
print("click 2 for gathering")

choice = input("choose")

if choice == 1:
    health = health - random.randint(10,15)
def create_player(name):
    """Returns a fresh player dictionary - Team A should implement this"""
    return {
        "name": name,
        "day": 1,
        "alive": True,
        
        # Stats (0-100 scale)
        "health": 100,
        "warmth": 100,
        "hunger": 100,
        "thirst": 100,
        
        # Inventory
        "inventory": {
            "wood": 0,
            "food": 0,
            "water": 0,
            "cloth": 0,
            "stone": 0
        },
        
        # Shelter & Equipment
        "shelter_level": 0,      # 0=none, 1=basic, 2=upgraded, 3=fortified
        "fire_burning": False,
        "tools": [],             # e.g., ["axe", "spear", "water_filter"]
        
        # Environment
        "temperature": -5,       # Celsius
        "weather": "clear",      # "clear", "snowing", "blizzard", "fog"
        
        # Meta
        "events_log": []         # List of strings describing what happened
    }
