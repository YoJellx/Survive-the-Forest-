import sys, time, random


health = 100
wood = 0
scrap = 0
day = 1
BaseRange = 0
FishingRod = 0
AdvancedRecipe = 0
MasterRecipe = 0
DivineRecipe = 0
rifle = 0
ammo = 0
BaseProtect = 0
ArmorProtection = 0
flashlight = 1
SwampGem = 0
Campfire = 0
spear = 0
kid = 0


if health <= 0:
    print("You died...")

time.sleep(1.5)
print("Survive in the forest until help arrives...")
time.sleep(1.5)
print("DAY", day)
time.sleep(2)
print("Objective: Gather Wood")
print("Press Enter to Chop Wood")

for i in range (10):
    userInput = input()


wood = wood + 15
print("You gained 15 wood.")
print("You have", wood,"wood")
time.sleep(2.5)

print("Objective: Build a Campfire")

userInput1 = input("Press F to craft."). lower()

if(userInput1 == "f"):
    print("What would you like to craft?")
    print("1. Basic FirePlace")
    print("2. Advanced Fireplace")

    userInput = input()

    if(userInput == "1"):
        if (wood-10>=0):   
            time.sleep(1)
            BaseRange = BaseRange + 5
            print("You crafted a Basic Fireplace. Your base range is now", BaseRange)
            Campfire = 1
        else:
            print("Get required material.")

    if(userInput == "2"):
        if (wood-25>=0):
            BaseRange = BaseRange + 15
            print("You crafted an Advanced Fireplace. Your base range is now", BaseRange)
            Campfire = 1
        else:
            print("Get required material.")

    print("Objective: Explore and gather material")
    time.sleep(0.5)

    userInput = input("Where do you want to go? WASD"). lower()

    if(userInput == "a"):
        print("You come across a river. It is a perfect place to catch fish.")
        time.sleep(3)
        print("You have no fishing rod. Find a recipe map to craft a fishing rod.")
        time.sleep(3)
        print("You cross the river.")
        time.sleep(3)
        print("You find an old fishing shop. You walk inside, and find a advanced workbench recipe.")
        AdvancedRecipe = 1
        time.sleep(3.5)
        print("You also find an old fishing rod.")
        FishingRod = 1
        time.sleep(2)
        print("You also find some scrap.")
        scrap = scrap + 5
        time.sleep(1)
        print("You have", scrap,"scrap.")
        time.sleep(2)
       
     
    if(userInput == "w"):
        print("You keep walking, and find an old camp.")
        time.sleep(2)
        print("You found some scrap.")
        scrap = scrap + 10
        time.sleep(2)
        print("You have", scrap,"scrap.")
        time.sleep(2)
        print("You also found a rifle.")
        rifle = 1
        time.sleep(2)
        print("You also found 12 rifle ammo.")
        ammo = 12
    
    if(userInput == "s"):
        print("You found a tribe village.")
        time.sleep(2)

        userInput = input("1. Loot/Rob them. 2. Trade with them.")

        if(userInput == "1"):
            print("You attempt to rob them. They use their blowpipes to damage you.")
            health = health - 75
            time.sleep(2)
            print("You have", health, "health.")
            time.sleep(2)
            print("You manage to get 10 scraps.")
            scrap = scrap + 10
            time.sleep(2)
            print("You have", scrap,"scrap.")
            time.sleep(2)

        if(userInput == "2"):
            print("What do you want to trade?")

            userInput = input("1. Old Flashlight 2. Wood")
            
            if(userInput == "1"):
                print("You offer to trade your old flashlight.")
                flashlight = 0
                time.sleep(2)
                print("They seem fascintated and give you leather armor in return.")
                time.sleep(2)
                print("You gained protection.")
                ArmorProtection = 10
                time.sleep(1)
                print("Your armor protection is", ArmorProtection)
   
    if(userInput == "d"):
        print("You find a watchtower.")
        time.sleep(2)
        print("You head up and find 5 scrap")
        scrap = scrap + 5
        time.sleep(1)
        print("You have",scrap,"scrap")
        time.sleep(2)
        print("You found a Silver Chest.")

        userInput = input("1. Open the chest 2. Don't")

        if(userInput == "1"):
            print("You open the chest.")
            time.sleep(2)
            print("You recieve Iron Armor.")
            ArmorProtection = 25
            time.sleep(2)
            print("Your armor protection is", ArmorProtection)

        if(userInput == "2"):
            print("You leave the chest.")
        
        time.sleep(2)
        print("You also find an old flashlight, but you already have one.")

    print("!Night is soon!")

    userInput = input("Head back? 1. Yes 2. No")
        
    if(userInput == "1"):
        time.sleep(1)
        print("You head back. Night falls")
        time.sleep(2)
        if Campfire == 1:
            print("Your campfire keeps you warm.")
        else:
            print("A wolf pack attacks you. You lose 75 health.")
            health = health -75
            time.sleep(2)


        
    if(userInput == "2"):
        if rifle == 1:
            print("You keep walking.")
            time.sleep(2)
            print("Night falls.")
            time.sleep(2)
            print("A pack of wolf attack you.")
            time.sleep(2)
            print("You use your rifle to attack them.")
            time.sleep(2)
            print("You successfully kill them and head back to camp.")
            ammo == ammo - 2
        else:
            print("You have no way of attacking, so you have to run.")
            time.sleep(2)
            print("You run back to camp, but lose 50 hp.")
            health = health - 50
            time.sleep(1.5)
            print("You have", health, "health.")
            if health <= 0:
                print("You died...")
                sys.exit()


day = day + 1
time.sleep(2)
print("DAY", day)
time.sleep(2)
print("You heal 25 health.")
health = health + 25
time.sleep(1)
print("You have", health,"health.")
def Craft_Turn():
    global scrap
    print("Would you like to craft?")

    userInput = input("1. Yes 2. No")

    if(userInput == "1"):
        if AdvancedRecipe == 1:
            print("What would you like to craft?")
            print("1. Metal Wall")
            print("2. Spike Trap")

            userInput = input()

            if(userInput == "1"):
                if scrap >= 5:
                    print("You crafted a metal wall, and it protected your base.")
                    BaseProtect = BaseProtect + 10
                    scrap = scrap - 5
                    time.sleep(2)
                    print("You now have", scrap, "scrap")
                else:
                    print("Gather more supplies.")
        
            if(userInput == "2"):
                if scrap > 2.5:
                    print("You crafted a Spike Trap.")
        else:
            print("You do not have the advanced recipe.")
    else:
        print("You exited the crafting menu.")

        
Craft_Turn()

print("What would you like to do?")

userInput = input("1. Go explore 2. Save the kid 3. Go fishing")

if(userInput == "1"):
    print("You go explore.")
    time.sleep(2)
    print("You find an old log cabin.")
    time.sleep(2)
    print("You recieve 4 chairs, which is the equivalent of 20 wood.")
    wood = wood + 20
    time.sleep(2)
    print("You explore the cabin some more, and find a ruby chest.")
    time.sleep(2)

    userInput = input("1. Open it 2. Don't")

    if(userInput == "1"):
        print("You open the chest, and get Red DragonScar Armor.")
        ArmorProtection = 100
        time.sleep(2)
        print("Your armor protection is", ArmorProtection)
        time.sleep(2)
        print("You also find a gem of the swamp.")
        time.sleep(2)
        print("You wonder what that's for.")
        SwampGem = 1
        time.sleep(2)

if(userInput == "2"):
    print("You go to save the first kid. His cave is guarded by 5 wolfs.")
    time.sleep(2)
    
    userInput = input("1. Try to sneak around them 2. Fight them ")

    if(userInput == "1"):
        print("You try to sneak around them. You go from the back and the top of the cave.")
        time.sleep(2)
        print("They luckily dont spot you.")
        time.sleep(2)
        print("You head into the cave, and find the kid, crying.")
        firstkid = 1
        time.sleep(2)
        print("You find a chest. Open it?")
        time.sleep(2)
        
        userInput = input("1. Open it 2. Don't")

        if(userInput == "1"):
            print("You recieve a spear.")
            spear = 1
            time.sleep(2)
            print("You head back to camp.")
            time.sleep(2)
            print("FIRST KID SAVED SUCCESFULLY")

    if(userInput == "2"):
        if rifle == 1:
            print("You shoot the wolves. You kill all of them, but you lose 25 health.")
            kid = 1
            time.sleep(2)
            print("FIRST KID SAVED SUCCESFULLY")
        else:
            print("You attack the wolves, but you have no weapon.")
            health = health - 99.999
            time.sleep(2)
            print("They damage you, and you have", health,"health left.")

print("A helicopter hovers above you.")
time.sleep(2)
print("It lands, and rescues you.")
time.sleep(2)

if kid == 1:
    print("YOU GOT THE HAPPY ENDING")

else:
    print("You got the normal ending.")

print("Credits:")
time.sleep(2)
print("99 nights in the Forest")
time.sleep(2)
print("Jellx")
time.sleep(2)
print("")
time.sleep(1)
print("")
time.sleep(1)
print("")
time.sleep(1)
print("")
time.sleep(2)
print("Thanks for surviving...")