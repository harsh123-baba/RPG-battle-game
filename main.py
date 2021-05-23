import random
from classes.game import Person
from classes.game import bcolors
from classes.magic import Spell
from classes.inventory import Item




#create black magic
fire = Spell("Fire", 15, 100, "black")
thunder = Spell("Thunder", 22, 120, "black")
blizzer = Spell("Blizzer", 24, 140 , "black")
mathor = Spell("Mathor", 26, 160, "black")
quake = Spell("Quake", 28, 180, "black")

#create white magic
cure = Spell("cure", 32, 120, "white")
cura = Spell("Cura", 32, 140, "white")


#create items
potion = Item("Potion", "potion", "Heal for 50 HP" , 50)
hipotion = Item("Hipotion", "potion", "Heal for 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heal for 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restore HP/MP of one party member", 9999)
hielixer = Item("Hielixer", "elixer", "Fully restroes HP/MP of party's member", 9999)
grenade = Item("Grenade", "attack", "Deals 500 points of Damage", 500)



player_magic = [fire, thunder, blizzer, mathor, cure, cura]
player_item = [ {"item": potion, "quantity":5},
                {"item":hipotion, "quantity": 5},
                {"item":superpotion, "quantity": 5},
                {"item":elixer, "quantity": 5},
                {"item":hielixer, "quantity": 5},
                {"item":grenade, "quantity": 2}
]

#instantiate magic

player1 = Person("vicky", 460, 65, 200, 34, player_magic, player_item)
player2 = Person("keshav", 460, 65, 200, 34, player_magic, player_item)
player3 = Person("Mi", 460, 65, 200, 34, player_magic, player_item)
players = [player1, player2, player3]

enemy1 = Person("shobit", 1600, 65, 90, 25, [], [])
enemy2 = Person("Ayush ", 1200, 65, 90, 25, [], [])
enemies = [enemy1, enemy2]


running = True
i =0
print(bcolors.FAIL +bcolors.BOLD +"An Enemy Attacks:"+bcolors.ENDC) 
while(running):
    
    print("==================================+=================================================")
    print("\n\n")
    print("Name                  HP                                   MP            ")
    

    for player in players:
        
        player.get_stats()
        
    print("\n\n")
    for enemy in enemies:
        enemy.get_enemy_stats()
    
    for player in players:

        player.choose_action()
        choice = input("    Choose your action ")
        index = int(choice)
        index = index -1
        
        if(index ==0):
            
            dmg = player.genrate_damage()
            enemy = int(player.choose_target(enemies))
            enemies[enemy].take_dmg(dmg)
            print(bcolors.OKGREEN+bcolors.BOLD+player.name+" attacked enemy "+ enemies[enemy].name+ " for :", dmg, "\n"+ bcolors.ENDC)
            if enemies[enemy].get_hp() ==0:
                print(enemies[enemy].name + " has died ")
                del enemies[enemy]
        elif index == 1:
                player.choose_magic()
                magic_choice = int(input("Choose Magic : "))
                print("\n")
                magic_choice = magic_choice-1


    #yeh linessmjh nh aayi yeh 2
                spell = player.magic[magic_choice]
                magic_damage = spell.genrate_damage()

                current_mp = player.get_mp()
                if(spell.cost > current_mp):
                    print(bcolors.FAIL + "Not Enough MP " +bcolors.ENDC)
                    continue

                player.reduce_mp(spell.cost)

                if(spell.type == "white"):
                    player.heal(magic_damage)
                    print(bcolors.OKGREEN+spell.name+" Heals for "+str(magic_damage)+bcolors.ENDC)


                elif(spell.type == "black"):
                    enemy = player.choose_target(enemies)
                    enemies[enemy].take_dmg(magic_damage)
                    print(bcolors.OKBLUE+"\n"+spell.name + " deals", str(magic_damage), "points of damage to "+ enemies[enemy].name+bcolors.ENDC)
                    if enemies[enemy].get_hp() ==0:
                        print(enemies[enemy].name + " has died ")
                        del enemies[enemy]

        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item : "))
            item_choice -= 1

            if(item_choice==-1):
                continue

            item = player.item[item_choice]["item"]
            player.item[item_choice]["quantity"]-=1
            if(player.item[item_choice]["quantity"]==0):
                print(bcolors.FAIL + "None left "+bcolors.ENDC)
                continue

            
            if(item.Type== "potion"):
                player.heal(item.prop)
                print(bcolors.OKGREEN + item.name +" Heals for"+str(item.prop))

            elif(item.Type =="elixer"):
                
                if item.name =="Hielixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp

                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + item.name + " Fully boosted your HP/MP ")

            elif(item.Type == "attack"):
                enemy = player.choose_target(enemies)
                enemies[enemy].take_dmg(item.prop)
            
                print(item.name +" Deals ",str(item.prop), " points of damage to "+enemies[enemy].name)
                if enemies[enemy].get_hp() ==0:
                    print(enemies[enemy].name + " has died ")
                    del enemies[enemy]



    #enemy_choice = 1

    for enemy in enemies:
        target = random.randrange(0, 3)
        enemy_dmg = enemy.genrate_damage()
        players[target].take_dmg(enemy_dmg)
        print(bcolors.FAIL+ enemies[0].name +" attacks for ", enemy_dmg, bcolors.ENDC)



    defeted_enemies = 0
    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeted_enemies+=1
    if defeted_enemies ==2:
        print(bcolors.OKGREEN + bcolors.BOLD + "   You won"+bcolors.ENDC)
        running = False

    defeted_player = 0
    for player in players:
        if player.get_hp() == 0:
            defeted_player +=1

    if defeted_player ==3:
        print(bcolors.FAIL + bcolors.BOLD + "    Enemy defeted you"+bcolors.ENDC)
        running = False
    


    #running = False



