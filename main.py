# ❄️ WINTER SURVIVAL SIMULATOR ❄️
# Main Game File - This ties all team modules together
# 
# INSTRUCTIONS:
# 1. Each team creates their own Python file:
#    - team_a.py (Base Camp + Game Loop)
#    - team_b.py (Resource Gathering + Weather)
#    - team_c.py (Crafting + Shelter)
# 
# 2. Import your team's functions at the top of this file
# 
# 3. Fill in the game loop below using everyone's functions
#
# ============================================================

# STEP 1: Import team modules (uncomment when ready)
# from team_a import create_player, display_status, main_menu, apply_daily_drain, check_alive, save_game, load_game, add_event
# from team_b import gather_menu, gather_wood, gather_food, gather_water, scavenge, advance_weather, describe_weather
# from team_c import crafting_menu, craft_item, upgrade_shelter, manage_fire, get_warmth_bonus

# ============================================================
# PLAYER DICTIONARY TEMPLATE (Team A: put this in your create_player function)
# ============================================================

def create_player_template(name):
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

# ============================================================
# MAIN GAME LOOP
# ============================================================

def main():
    """Main game loop - connects all team modules together"""
    
    print("=" * 50)
    print("❄️  WINTER SURVIVAL SIMULATOR  ❄️")
    print("=" * 50)
    print()
    
    # Ask if loading a save or starting new
    print("1. New Game")
    print("2. Load Game")
    choice = input("Choose (1/2): ").strip()
    
    if choice == "2":
        # TODO: Use Team A's load_game() function
        filename = input("Enter save filename: ").strip()
        # player = load_game(filename)
        print("⚠️ Load function not yet connected!")
        player = create_player_template("Survivor")  # Fallback
    else:
        name = input("Enter your name, survivor: ").strip()
        if not name:
            name = "Survivor"
        # TODO: Use Team A's create_player() function
        # player = create_player(name)
        player = create_player_template(name)  # Using template for now
    
    print()
    print(f"Good luck, {player['name']}. Try to survive as long as you can...")
    print()
    
    # ========== GAME LOOP ==========
    while player["alive"]:
        
        # STEP 1: Advance weather (Team B)
        # TODO: advance_weather(player)
        print(f"[Day {player['day']}] Weather: {player['weather']}, Temp: {player['temperature']}°C")
        
        # STEP 2: Display status (Team A)
        # TODO: display_status(player)
        print(f"Health: {player['health']} | Warmth: {player['warmth']} | Hunger: {player['hunger']} | Thirst: {player['thirst']}")
        print(f"Inventory: {player['inventory']}")
        print(f"Tools: {player['tools']} | Shelter Level: {player['shelter_level']} | Fire: {'🔥' if player['fire_burning'] else '❌'}")
        print()
        
        # STEP 3: Get player action (Team A)
        # TODO: Use Team A's main_menu() function
        print("What would you like to do?")
        print("1. Go gathering")
        print("2. Craft / Build")
        print("3. Rest")
        print("4. Check inventory")
        print("5. Save game")
        print("6. Quit")
        
        action = input("Choose (1-6): ").strip()
        print()
        
        # STEP 4: Execute action
        if action == "1":
            # TODO: Use Team B's gather_menu() and gathering functions
            print("🌲 [Gathering not yet connected - Team B]")
            # Example flow:
            # gather_choice = gather_menu(player)
            # if gather_choice == "wood":
            #     gather_wood(player)
            # elif gather_choice == "food":
            #     gather_food(player)
            # etc.
            
        elif action == "2":
            # TODO: Use Team C's crafting_menu() and crafting functions
            print("🛠️ [Crafting not yet connected - Team C]")
            # Example flow:
            # craft_choice = crafting_menu(player)
            # if craft_choice == "fire":
            #     manage_fire(player)
            # elif craft_choice == "shelter":
            #     upgrade_shelter(player)
            # else:
            #     craft_item(player, craft_choice)
            
        elif action == "3":
            # Rest - small health recovery
            player["health"] = min(100, player["health"] + 10)
            print("😴 You rest and recover some health. (+10 health)")
            
        elif action == "4":
            # Just show inventory (doesn't use up the day)
            print("📦 Inventory:", player["inventory"])
            print("🔧 Tools:", player["tools"] if player["tools"] else "None")
            continue  # Don't advance the day
            
        elif action == "5":
            # TODO: Use Team A's save_game() function
            filename = input("Enter save filename: ").strip()
            # save_game(player, filename)
            print(f"💾 [Save function not yet connected - Team A]")
            continue  # Don't advance the day
            
        elif action == "6":
            print("Thanks for playing! You survived", player["day"], "days.")
            break
            
        else:
            print("Invalid choice. Try again.")
            continue  # Don't advance the day
        
        # STEP 5: Apply daily drain (Team A)
        # TODO: Use Team A's apply_daily_drain() with Team C's warmth formula
        # warmth_bonus = get_warmth_bonus(player)
        # apply_daily_drain(player, warmth_bonus)
        
        # Temporary basic drain:
        player["hunger"] -= 10
        player["thirst"] -= 15
        player["warmth"] -= 10
        
        # STEP 6: Fire expires at end of day
        player["fire_burning"] = False
        
        # STEP 7: Check if player survived (Team A)
        # TODO: Use Team A's check_alive() function
        if player["health"] <= 0 or player["warmth"] <= 0 or player["hunger"] <= 0 or player["thirst"] <= 0:
            player["alive"] = False
            print()
            print("=" * 50)
            print(f"💀 You did not survive. You lasted {player['day']} days.")
            print("=" * 50)
            break
        
        # STEP 8: Advance to next day
        player["day"] += 1
        print()
        print("-" * 50)
        print()
    
    print()
    print("🎮 Game Over. Thanks for playing!")

# ============================================================
# RUN THE GAME
# ============================================================

if __name__ == "__main__":
    main()
