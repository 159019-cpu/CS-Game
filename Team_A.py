# =====================================================
# 🏕️ WILDERNESS SURVIVAL — TEAM A CORE
# Base Camp + Game Loop
# =====================================================

import json
import sys

# =====================================================
# PLAYER CREATION
# =====================================================

def create_player(name: str) -> dict:
    return {
        "name": name,
        "day": 1,
        "alive": True,

        # Vital Stats
        "health": 100,
        "hunger": 100,
        "thirst": 100,
        "warmth": 100,

        # Environment
        "weather": "Clear",

        # Base
        "shelter_level": 0,
        "fire_level": 0,

        # Inventory
        "inventory": {},

        # Logs
        "events_log": []
    }


# =====================================================
# EVENT LOGGER
# =====================================================

def add_event(player: dict, message: str):
    entry = f"Day {player['day']}: {message}"
    player["events_log"].append(entry)


# =====================================================
# STATUS DISPLAY
# =====================================================

def display_status(player: dict):
    print("\n" + "=" * 50)
    print(f"🏕️  DAY {player['day']}  |  Survivor: {player['name']}")
    print("=" * 50)

    def stat(label, value):
        if value <= 25:
            return f"{label:<10}: {value} ⚠️"
        return f"{label:<10}: {value}"

    print(stat("Health", player["health"]))
    print(stat("Hunger", player["hunger"]))
    print(stat("Thirst", player["thirst"]))
    print(stat("Warmth", player["warmth"]))

    print("-" * 50)
    print(f"🌤️ Weather: {player['weather']}")
    print(f"🏠 Shelter level: {player['shelter_level']}")
    print(f"🔥 Fire level: {player['fire_level']}")

    print("\n🎒 Inventory:")
    if player["inventory"]:
        for item, qty in player["inventory"].items():
            print(f"  - {item}: {qty}")
    else:
        print("  (empty)")

    if player["events_log"]:
        print("\n📜 Recent events:")
        for event in player["events_log"][-3:]:
            print(f"  • {event}")

    print("=" * 50)


# =====================================================
# MAIN MENU
# =====================================================

def main_menu(player: dict) -> str:
    print("\nChoose an action:")
    print("1) Go gathering")
    print("2) Craft / Build")
    print("3) Rest")
    print("4) Check inventory")
    print("5) Save game")
    print("6) Quit")

    return input("> ").strip()


# =====================================================
# DAILY DRAIN
# =====================================================

def apply_daily_drain(player: dict, warmth_modifier: int = 0):
    player["hunger"] -= 10
    player["thirst"] -= 15

    base_warmth_loss = 10
    warmth_loss = max(0, base_warmth_loss - warmth_modifier)
    player["warmth"] -= warmth_loss

    add_event(player, "The day ends. Hunger, thirst and warmth decreased.")


# =====================================================
# SURVIVAL CHECK
# =====================================================

def check_alive(player: dict) -> bool:
    for stat in ("health", "hunger", "thirst", "warmth"):
        if player[stat] <= 0:
            player["alive"] = False
            print("\n☠️  GAME OVER")
            print(f"You survived {player['day']} days.")
            return False
    return True


# =====================================================
# SAVE / LOAD
# =====================================================

def save_game(player: dict, filename: str):
    with open(filename, "w") as f:
        json.dump(player, f, indent=2)
    print("💾 Game saved.")

def load_game(filename: str) -> dict:
    with open(filename, "r") as f:
        player = json.load(f)
    print("📂 Game loaded.")
    return player


# =====================================================
# MAIN GAME LOOP
# =====================================================

def game_loop(player: dict):
    while player["alive"]:
        display_status(player)
        choice = main_menu(player)

        if choice == "1":
            # -------- Team B Hook --------
            print("\n🔍 You go gathering...")
            add_event(player, "Went gathering.")
            # Team B will modify inventory & weather

        elif choice == "2":
            # -------- Team C Hook --------
            print("\n🔨 You work on crafting/building...")
            add_event(player, "Crafted or built structures.")
            # Team C will update shelter/fire

        elif choice == "3":
            player["health"] = min(100, player["health"] + 5)
            add_event(player, "Rested and recovered some health.")

        elif choice == "4":
            display_status(player)
            continue  # no day passes

        elif choice == "5":
            save_game(player, "savegame.json")
            continue

        elif choice == "6":
            print("\n👋 You quit the game.")
            sys.exit(0)

        else:
            print("❌ Invalid choice.")
            continue

        # ---- End of Day ----
        apply_daily_drain(player)

        if not check_alive(player):
            break

        player["day"] += 1


# =====================================================
# ENTRY POINT
# =====================================================

def main():
    print("\n🏕️  WILDERNESS SURVIVAL\n")

    choice = input("Load saved game? (y/n): ").strip().lower()

    if choice == "y":
        try:
            player = load_game("savegame.json")
        except FileNotFoundError:
            print("❌ No save found. Starting new game.")
            name = input("Enter your name: ")
            player = create_player(name)
    else:
        name = input("Enter your name: ")
        player = create_player(name)

    game_loop(player)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted.")
