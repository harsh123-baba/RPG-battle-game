from math import fabs
import random
from .magic import Spell
from .inventory import Item
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self,name, hp, mp, atk , df, magic, item):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk-10
        self.atkh = atk +10
        self.df = df
        self.item = item
        self.magic = magic
        self.actions  = ["Attack", "Magic", "Items"]
        self.name = name

    def genrate_damage(self):
        return random.randrange(self.atkl, self.atkh)


    def take_dmg(self, dmg):
        self.hp -= dmg
        if(self.hp<0):
            self.hp =0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp
    
    def get_max_mp(self):
        return self.maxmp
    
    def reduce_mp(self, cost):
        self.mp -= cost
    
    def choose_action(self):
        i =1
        print("\n"+bcolors.BOLD +self.name +" : "+bcolors.ENDC)
        print(bcolors.OKBLUE +bcolors.BOLD+ "Actions"+bcolors.ENDC)
        for item in self.actions:
            print("    "+str(i)+":", item)
            i+=1

    def choose_magic(self):
        i =1
        
        print(bcolors.OKGREEN +bcolors.BOLD+ "Magic"+bcolors.ENDC)
        for spell in self.magic:
            print("    "+str(i)+":", spell.name,"[cost : "+str(spell.cost)+"]")
            i +=1

    def choose_item(self):
        i = 1
        print(bcolors.OKGREEN + bcolors.BOLD+"Items"+bcolors.ENDC)
        for item in self.item:
            print("    "+str(i)+":", item["item"].name, " : ", item["item"].description, "(X",str(item["quantity"])+")")
            i+=1

    def choose_target(self, enemies):
        i = 1
        print("    "+bcolors.FAIL+"Targets : "+bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp()!=0:
                print("    "+str(i)+". "+enemy.name)
                i+=1

        choice = int(input("    Choose Target : "))-1
        return choice

    def heal(self, dmg):
        self.hp +=dmg
        if(self.hp>self.maxhp):
            self.hp = self.maxhp 


    def get_enemy_stats(self):
        hp_bars = ""
        hp_ticks = (self.hp/self.maxhp)*100/2
        while(hp_ticks>0):
            hp_bars+="█"
            hp_ticks-=1

        while(len(hp_bars)<50):
            hp_bars +=" "


        hp_string = str(self.hp)+"/"+str(self.maxhp)
        current_hp = ""
        if(len(hp_string)<9):
            decresed = 9-len(hp_string)
            while(decresed>0):
                current_hp += " "
                decresed -=1
            current_hp+=hp_string

        else:
            current_hp = hp_string

        
        print("                              ___________________________________________________")
        print(f"{self.name:10}" +"           "+current_hp+"|"+bcolors.FAIL+ hp_bars+bcolors.ENDC+"|" +bcolors.ENDC)

    




    def get_stats(self):
        hp_bars=""
        bar_ticks = (self.hp/self.maxhp)*100/4
         
        mp_bars = ""
        mp_ticks = (self.mp/self.maxmp)*100/10

        while(bar_ticks>0):
            hp_bars+="█"
            bar_ticks-=1

        while(len(hp_bars)<25):
            hp_bars+=" "

        
        
        while(mp_ticks>0):
            mp_bars+= "█"
            mp_ticks-=1

        while(len(mp_bars)<10):
            mp_bars += " "

        hp_string = str(self.hp)+"/"+str(self.maxhp)

        # current_hp = ""
        # if(len(hp_string)<7):
        #     decresed = 7-len(hp_string)

        #     while(decresed>0):
        #         hp_string += " "
        #         decresed-=1

        #     current_hp += hp_string

        # else:
        #     current_hp = hp_string

        mp_string = str(self.mp)+"/"+str(self.maxmp)
        # current_mp = ""
        # if(len(mp_string)<5):
        #     decresed = 5-len(mp_string)
        #     while(decresed>0):
        #         mp_string += " "
        #         decresed-=1
            
        #     current_mp = mp_string
        # else:
        #     current_mp = mp_string


        print("                             __________________________           ___________")
        print(f"{self.name:10}" +"           "+f"{hp_string:7}"+"|"+bcolors.OKGREEN+ hp_bars+bcolors.ENDC+"|" 
        + "     "+f"{mp_string:5}"+"|"+bcolors.OKBLUE+mp_bars+bcolors.ENDC+"|")

    
    
