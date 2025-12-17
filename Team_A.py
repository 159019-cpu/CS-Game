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
