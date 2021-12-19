import time
import random

def printD (string):
     print (string)
     time.sleep(1.5)

class move:
     name = " "
     damage = 0
     def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class pokemon:
    name = " "
    lvl = 0
    maxhp = 0
    currenthp = 0
    xp = 0
    move = None
    evolutions = []
    futuremoves = []
    def __init__(self, name, lvl, maxhp, currenthp, xp, move, evolutions, futuremoves):
        self.name = name
        self.lvl = lvl
        self.maxhp = maxhp
        self.currenthp = currenthp
        self.xp = xp
        self.move = move
        self.evolutions = evolutions
        self.futuremoves = futuremoves
    def gainxp(self, xpgain):
        self.xp = self.xp + xpgain
        if self.xp > 100:
            self.xp = self.xp - 100
            self.lvl = self.lvl + 1
            self.maxhp = self.maxhp + 10
            print ("" + self.name + " has leveled up to level " + str(self.lvl))
        if self.lvl > 5 and self.lvl < 11:
             self.name = self.evolutions[0]
             self.move = self.futuremoves[0]
             print ("" + self.name + " has evolved!")
        if self.lvl > 10:
             self.name = self.evolutions[1]
             self.move = self.futuremoves[1]
             print ("" + self.name + " has evolved!")

inventory = [0,0,0]
berryNames = ["Small Berry", "Medium Berry", "Large Berry"]
berryheal = [15,25,35]

badges = []

def battle (starter, enemy):
     enemy.currenthp = enemy.maxhp
     if starter.currenthp <= 0:
          print ("Your pokemon has fainted! Please visit the Pokemon Center")
          return False
     print ("You are in a battle against " + enemy.name)
     while starter.currenthp > 0 and enemy.currenthp > 0:
          action = input("What do you want to do? \n\t(1)Bag \n\t(2)Fight \n")
          actionDone = False
          if action == "1":
               berrychoice = input("What kind of berry do you want to use? \n\t(1)Small Berry \n\t(2)Medium Berry \n\t(3)Large Berry \n\t(4)Go back instead \n")
               if berrychoice != "4": 
                    if inventory[int(berrychoice)-1] < 1:
                         print ("You don't have enough")
                    else:
                         inventory[int(berrychoice)-1]-=1
                         starter.currenthp += berryheal[int(berrychoice) -1]
                         actionDone = True
               #If statment Check if it doesnt go over hp, set currenthp = maxhp
                         if starter.currenthp + berryheal[int(berrychoice) -1] > starter.maxhp:
                              starter.currenthp = starter.maxhp
          else:
               #while action 
               print ("Moves: \n(1) " + starter.move.name)
               choice = input("What is " + starter.name + " going to use? \n")
               #while loop for ==1
               actionDone = True
               print (starter.name + " used " + starter.move.name + " and did " + str(starter.move.damage) + " damage!")
               enemy.currenthp = enemy.currenthp - starter.move.damage
          if actionDone == True:
               if enemy.currenthp > 0:
                    print (enemy.name + " used " + enemy.move.name + " and did " + str(enemy.move.damage) + " damage!")
                    starter.currenthp = starter.currenthp - enemy.move.damage
          if enemy.currenthp <=0:
               print (enemy.name + " has fainted!")
               starter.gainxp(34)
               print (starter.name + " has gained 34 XP")
          else:
               print (enemy.name + " has " + str(enemy.currenthp) + " HP left!")
                 
          if starter.currenthp <=0:
               print (starter.name + " has fainted!")
          else:
               print (starter.name + " has " + str(starter.currenthp) + " HP left!")
     if starter.currenthp <= 0:
          return False
     else:
          return True 
          

#ADD NEW MOVES WHEN LEVEL UP
#ADD EVOLUTION


printD ("Hi there! It's so nice to meet you!")
printD ("Welcome to the world of Pokemon!")
printD ("My name is Professor Anaconda and I will be helping you start your adventure!")
printD ("But before that, what is your name?")

name = input("Enter your name: ")

time.sleep(1)
printD ("Hi " + name +"! Come visit me at my laboratory when you get the chance.")
printD ("There's still one more thing you need to do to before you begin!")
printD (".")
printD (".")
printD (".")
printD ("You wake up to a ray of sunlight shining in your eyes.")
printD ("But everything is unfamiliar...")
printD ("Oh right, you just moved to Twinleaf Town...")


printD ("Let's see what Mom is doing")

choice = input("What do you want to do? (Please enter a number) \n \t(1)Go back to bed \n \t(2)Go on your PC \n \t(3)Go downstairs \n")

while choice != "3":
     if choice == "1":
          print ("It's too early for that")
     if choice == "2":
          print ("There's no internet right now")
     choice = input("What do you want to do? (Please enter a number) \n \t(1)Go back to bed \n \t(2)Go on your PC \n \t(3)Go downstairs \n")


printD ("You go downstairs to see Mom making breakfast")
printD ("Hi honey, I think Professor Anaconda was looking for you. Do you want to grab something to eat before you go?")
printD ("No, it's okay. I'll eat later. See you, Mom. I'll head over there right now")

printD ("You start your walk to Professor's lab, but you notice something strange.")
printD ("There's strange creatures around you...")
printD ("The pigeons look slightly different")
printD ("The bugs are WAY bigger")
printD ("And is that... a fish on land??")
printD ("You finally make it to the lab and Professor Anaconda greets you.")
printD ("Hi " + name + "! You finally made it here! \nLet's get you started!")
printD ("He takes out a suitcase with three shiny spheres...half of it red, the other half white, and a button in the center")
printD ("In Pokeball (1) is Chimchar! A chimp Pokemon with fire-type moves!")
printD ("In Pokeball (2) is Turtwig! A turtle Pokemon with grass-type moves!")
printD ("In Pokeball (3) is Piplup! A penguin Pokemon with water-type moves!")

choice = input("Take your pick! \n\t(1)Chimchar \n\t(2)Turtwig \n\t(3)Piplup \n")
  
if choice == "1":
     print ("Great choice! Don't monkey around too much!")
     ember = move("Ember!", 20)
     flamewheel = move("Flame Wheel!", 30)
     flamethrower = move("Flamethrower!", 40)     
     starter = pokemon("Chimchar", 1, 50, 50, 0, ember, ["Monferno","Infernape"], [flamewheel, flamethrower])
if choice == "2":
     print ("Great choice! Make sure Turtwig keeps up!")
     razerleaf = move("Razer Leaf!", 20)
     leechseed = move("Leech Seed!", 30)
     leafstorm = move("Leaf Storm!", 40)
     starter = pokemon("Turtwig", 1, 50, 50, 0, razerleaf,["Grotle","Torterra"], [leechseed,leafstorm])
if choice == "3":
     print ("Great choice! Piplup won't be flying away, that's for sure!")
     watergun = move("Water Gun!", 20)
     whirlpool = move("Whirlpool!", 30)
     hydropump = move("Hydro Pump!",40)
     starter = pokemon("Piplup", 1, 50, 50, 0, watergun,["Prinplup","Empoleon"], [whirlpool,hydropump])

time.sleep(1.5)
printD ("Now that you have your first Pokemon, you can begin your adventure!")
printD ("Explore all of the Sinnoh Region and train " + starter.name + " to become the strongest")
printD ("Here's a Badge Box as well! Use this to keep track of each Gym Leader you defeat!")
printD ("Off you go!")

printD ("You are excited of what's coming. Your new companion, " + starter.name + " is going to be with you the entire adventure!")
printD ("I love " + starter.name + "...")

printD ("Let's get our first badge in Oreburgh City!")
printD ("You make your way to the edge of Twinleaf Town and take a look at the map")
printD (".")
printD (".")
printD (".")
printD ("That's going to be a long walk...")
printD ("But you're anxious to begin, and you take your first step into the tall grass.")
printD (".")
printD (".")

turn1 = 1

peck = move("Peck", 10)
bite = move("Bite", 15)

starly = pokemon("Starly", 2, 30, 30, 0, peck,[],[])
bidoof = pokemon("Bidoof", 3, 50, 50, 0, bite,[],[])

while turn1 < 5:
     chance = random.randint(1,7)
     if chance < 4:
               printD ("You encounter a wild Pokemon!")
               printD ("Prepare for battle!")
               wildbattle = random.randint(0,1)
               wild = [starly,bidoof]
               result = battle(starter,wild[wildbattle])
               if result == False:
                    print ("You lost, start at the beginning again.")
                    print ("Your pokemon has been healed to full HP.")
                    starter.currenthp = starter.maxhp
                    turn1 = 0
               turn1 = turn1 + 1
     if chance > 3 and chance < 6:
               printD ("Another Trainer wants to battle!")
               printD ("Prepare for battle!")
               wildbattle = random.randint(0,1)
               wild = [starly,bidoof]
               result = battle(starter,wild[wildbattle])
               if result == False:
                    print ("You lost, start at the beginning again.")
                    print ("Your pokemon has been healed to full HP.")
                    starter.currenthp = starter.maxhp
                    turn1 = 0       
               turn1 = turn1 + 1
     if chance > 5:
               printD ("You see something on the floor...")
               berry = random.randint(0,2)
               printD ("It's a " + berryNames[berry] + ". What a lucky find!")
               inventory[berry]+=1
               turn1 = turn1 + 1
     print ("----------------------------------------------------------------------------------------------------")
printD ("You finally made it!")

printD ("Ah yes, the b-beau...")
printD ("ti...")
printD ("ful...")
printD ("city of Oreburgh")
printD ("What is this rocky place?! It's like we're in a mine!")
printD (".")
printD (".")
printD (".")
printD ("An Old Man with a brown sweater approaches you slowly.")
printD ("Hi traveler! What brings you to Oreburgh City?")
printD ("Are you here for a chance to excavate some brilliant diamonds and pearls?")
printD ("Actually, I'm here to fight the Gym Leader to get my first badge!")
printD ("Another young'n starting off their adventure I see...")

printD ("Roark, our town's Gym Leader, is waiting at Oreburgh Gym. I wish you the best of luck.")

choice = input("What do you want to do? \n\t(1)Go battle the Gym Leader! \n\t(2)Visit the Pokemon Center. \n\t(3)Go train some more! \n\t(4)Check your bag. \n")
beatgym = False
while (choice == "1" or choice == "2" or choice == "3" or choice == "4"):
     if choice == "1":
          rocksmash = move("Rock Smash!", 24)
          gym1 = pokemon("Geodude", 4, 80, 80, 0, rocksmash,[],[])
          result = battle(starter,gym1)
          if result == True:
               beatgym = True
          else:
               print ("You lost the Gym battle :( \nHeal your Pokemon and train up!")
     if choice == "2":
          printD ("Let's make sure " + starter.name + " is recovered before we battle again.")
          starter.currenthp = starter.maxhp
          printD ("" + starter.name + "'s HP has been fully restored!")
     if choice == "3":
          #wildbattle
          wildbattle = random.randint(0,1)
          wild = [starly,bidoof]
          result = battle(starter,wild[wildbattle])
          if result == False:
               print ("You lost, start at the beginning again.") 
          berryfind = random.randint(1,2)
          if berryfind == 1:
               berry = random.randint(0,2)
               printD ("It's a " + berryNames[berry] + ". What a lucky find!")
               inventory[berry]+=1
     if choice == "4":
          print (inventory)
     if beatgym == True:
          break
     time.sleep(1)
     choice = input("What do you want to do? \n\t(1)Go battle the Gym Leader! \n\t(2)Visit the Pokemon Center. \n\t(3)Go train some more! \n\t(4)Check your bag. \n")
printD ("Let's get that badge!")
#RoarkBattle

printD ("Suddenly, you hear ringing from your pocket...")
printD ("CONGRATULATIONS " + name +"!")
printD ("You recognize the voice as Professor Anaconda")
printD ("You have defeated Roark, the first Gym Leader!")
printD ("Just look at that new shiny badge!")

badges.append ("Coal Badge")

choice = input("Check your new badge! \n\t(1)Bag \n\t(2)Go train \n")
while choice != "1":
     if choice == "2":
          print ("Check your bag!")
     choice = input("Check your new badge! \n\t(1)Bag \n\t(2)Go train \n")

bag = input ("What do you want to do? \n\t(1)Berry \n\t(2)Badges \n")
while choice != "2":
     if choice == "1":
          print ("It's not the time for that right now!")
     choice = input("Check your new badge! \nWhat do you want to do? \n\t(1)Berry \n\t(2)Badges \n")
 
printD ("You look at your badge case in excitement...")
printD (".")
printD (".")
printD (".")
printD ("The Coal Badge!")
printD ("Make your way to Eterna City, where your next battle awaits you!")
printD ("Goodbye Trainer!")
printD (".")
printD (".")
printD (".")
printD ("Wow! What a battle! That's our first badge, the Coal Badge!")
printD ("I can't wait any longer, let's get going")
printD ("You look for a map to see which way to go...")
printD ("Another **** walk...")
printD ("Why is every city so far from another???")
printD ("Where's the transportation???")
printD ("You grudginly take a step into the tall grass again...")
printD (".")
printD (".")

turn2 = 1

while turn2 < 5:
     chance = random.randint(1,7)
     if chance < 4:
               printD ("You encounter a wild Pokemon!")
               printD ("Prepare for battle!")
               #put battle here
               wildbattle = random.randint(0,1)
               wild = [starly,bidoof]
               result = battle(starter,wild[wildbattle])
               if result == False:
                    print ("You lost, start at the beginning again.")
                    print ("Your pokemon has been healed to full HP.")
                    starter.currenthp = starter.maxhp
                    turn2 = 0 
               turn2 = turn2 + 1
     if chance > 3 and chance < 6:
               printD ("Another Trainer wants to battle!")
               printD ("Prepare for battle!")
               #put battle here
               wildbattle = random.randint(0,1)
               wild = [starly,bidoof]
               result = battle(starter,wild[wildbattle])
               if result == False:
                    print ("You lost, start at the beginning again.")
                    print ("Your pokemon has been healed to full HP.")
                    starter.currenthp = starter.maxhp
                    turn2 = 0 
               turn2 = turn2 + 1
     if chance > 5:
               printD ("You see something on the floor...")
               berry = random.randint(0,2)
               printD ("It's a " + berryNames[berry] + ". What a lucky find!")
               inventory[berry]+=1
               turn2 = turn2 + 2
     print ("----------------------------------------------------------------------------------------------------")
printD ("You finally made it!")

printD ("Finally, some green around here.")
printD ("Suddenly, you hear a faint but recognizable sound...")
printD ("The steadfast footsteps approaching you slowly...")
printD (".")
printD (".")
printD (".")
printD ("You turn around to see the Old Man again... but in a green sweater")
printD ("Hiya youngster! What brings you to the luscious city of Eterna?")
printD ("To smell the flowers and pick some berries maybe?")
printD ("How did you get here already, Old Man?!")
printD ("What do you mean? I've always lived here?")
printD ("No, you were literally just at Oreburgh City")
printD ("and in a brown sweater")
printD ("Oh!! You must be talking about my twin brother!")
printD ("He loves brown...")
printD ("But I love green... as he points to his sweater")
printD ("I'm here to challenge Eterna's Gym Leader, do you know where the Gym is?")
printD ("Ah yes, a greenhorn at the edge of their seat ready to battle.")
printD ("Gardenia, is that way. Goodluck!")
printD ("You look straight ahead at the imposing Gym...")
printD ("That second badge is mine.")
     
choice = input("What do you want to do? \n\t(1)Go battle the Gym Leader! \n\t(2)Visit the Pokemon Center. \n\t(3)Go train some more! \n\t(4)Check your bag. \n")
beatgym = False
while (choice == "1" or choice == "2" or choice == "3" or choice == "4"):
     if choice == "1":
          gigadrain = move("Giga Drain!", 34)
          gym2 = pokemon("Roserade", 7, 100, 100, 0, gigadrain,[],[])
          result = battle(starter,gym2)
          if result == True:
               beatgym = True
          else:
               print ("You lost the Gym battle :( \nHeal your Pokemon and train up!")
     if choice == "2":
          printD ("Let's make sure " + starter.name + " is recovered before we battle again.")
          starter.currenthp = starter.maxhp
          printD ("" + starter.name + "'s HP has been fully restored!")
     if choice == "3":
          #wildbattle
          print ("Pokemon Battle Here")
          wildbattle = random.randint(0,1)
          wild = [starly,bidoof]
          result = battle(starter,wild[wildbattle])
          if result == False:
               print ("You lost, start at the beginning again.")
          berryfind = random.randint(1,2)
          if berryfind == 1:
               berry = random.randint(0,2)
               printD ("It's a " + berryNames[berry] + ". What a lucky find!")
               inventory[berry]+=1
     if choice == "4":
          bag = input ("What do you want to do? \n\t(1)Berry \n\t(2)Badges \n")
          if bag == "1":
               print (badges)
          if bag == "2":
               print (inventory)
     if beatgym == True:
          break
     time.sleep(1)
     choice = input("What do you want to do? \n\t(1)Go battle the Gym Leader! \n\t(2)Visit the Pokemon Center. \n\t(3)Go train some more! \n\t(4)Check your bag. \n")
printD ("Let's get that badge!")
#GardeniaBattle

printD ("You hear ringing again from your pocket...")
printD ("Professor Anaconda again.")
printD ("CONGRATULATIONS " + name +"!")
printD ("You have defeated Gardenia, the second Gym Leader!")
printD ("Look at your new badge!")

badges.append ("Forest Badge")

choice = input("Check your new badge! \n\t(1)Bag \n\t(2)Go train \n")
while choice != "1":
     if choice == "2":
          print ("Check your bag!")
     choice = input("Check your new badge! \n\t(1)Bag \n\t(2)Go train \n")
bag = input ("What do you want to do? \n\t(1)Berry \n\t(2)Badges \n")
while choice != "2":
     if choice == "1":
          print ("It's not the time for that right now!")
     choice = input("Check your new badge! \nWhat do you want to do? \n\t(1)Berry \n\t(2)Badges \n")

printD ("Your next badge awaits you at Veilstone City!")
printD ("Goodbye Trainer!")
printD (".")
printD ("Wow, my second badge... and look at " + starter.name + " too...")
printD (starter.name + "'s so strong now")
printD ("and I have two badges now, the Coal Badge and the Forest Badge!")
printD ("Becoming a Pokemon Master isn't so far away huh....")
printD (".")
printD (".")
printD (".")
printD ("But Veilstrone City is far away......")
printD ("Here we go again")

turn3 = 1

while turn3 < 3:
     chance = random.randint(1,7)
     if chance < 4:
               printD ("You encounter a wild Pokemon!")
               printD ("Prepare for battle!")
               #put battle here
               wildbattle = random.randint(0,1)
               wild = [starly,bidoof]
               result = battle(starter,wild[wildbattle])
               if result == False:
                    print ("You lost, start at the beginning again.")
                    print ("Your pokemon has been healed to full HP.")
                    starter.currenthp = starter.maxhp
                    turn3 = 0 
               turn3 = turn3 + 1
     if chance > 3 and chance < 6:
               printD ("Another Trainer wants to battle!")
               printD ("Prepare for battle!")
               #put battle here
               wildbattle = random.randint(0,1)
               wild = [starly,bidoof]
               result = battle(starter,wild[wildbattle])
               if result == False:
                    print ("You lost, start at the beginning again.")
                    print ("Your pokemon has been healed to full HP.")
                    starter.currenthp = starter.maxhp
                    turn3 = 0
               turn3 = turn3 + 1
     if chance > 5:
               printD ("You see something on the floor...")
               berry = random.randint(0,2)
               printD ("It's a " + berryNames[berry] + ". What a lucky find!")
               inventory[berry]+=1
               turn3 = turn3 + 1
     print ("----------------------------------------------------------------------------------------------------")
printD ("You finally made it...?")

printD ("Oh wow, that was actually quick")
printD ("You hear those inevitable footsteps again...")
printD (".")
printD (".")
printD ("Hello youth! Come visit our Casinos, Game Buildings, Department Stores!")
printD ("Hi... again... do you and your twin like traveling or something?")
printD ("I'm not following what you're saying...?")
printD ("Actually, it seems like you two have been following me")
printD ("OHHH, you must be talking about my brothers!")
printD ("Can't you see, I look nothing like them!")
printD ("You glance up and down the Old Man, everything identical...")
printD (".")
printD (".")
printD (".")
printD ("...except that damned sweater.")
printD ("Orange.")
printD ("I'm here to get that last badge for this case")
printD ("And get all this walking over with.")
printD ("A small grin forms on the Old Man's face...")
printD ("Maylene, our city's Gym leader, is actually up there.")
printD ("He points up...")
printD (".")
printD (".")
printD ("...above that mountain behind all the buildings.")
printD ("You're kidding me. I knew that trip was too short to be true.")
printD ("Have fun kiddo! I've got to wash my sweaters!")
printD ("I mean sweater... I only have one sweater. Right.")
printD ("and the Old man dissappears around the corner.")
printD (".")
printD ("You let out a big sigh and start the trek.")

turn4 = 1

while turn4 < 3:
     chance = random.randint(1,7)
     if chance < 4:
               printD ("You encounter a wild Pokemon!")
               printD ("Prepare for battle!")
               #put battle here
               wildbattle = random.randint(0,1)
               wild = [starly,bidoof]
               result = battle(starter,wild[wildbattle])
               if result == False:
                    print ("You lost, start at the beginning again.")
                    print ("Your pokemon has been healed to full HP.")
                    starter.currenthp = starter.maxhp
                    turn1 = 0
               turn4 = turn4 + 1
     if chance > 3 and chance < 6:
               printD ("Another Trainer wants to battle!")
               printD ("Prepare for battle!")
               #put battle here
               wildbattle = random.randint(0,1)
               wild = [starly,bidoof]
               result = battle(starter,wild[wildbattle])
               if result == False:
                    print ("You lost, start at the beginning again.")
                    print ("Your pokemon has been healed to full HP.")
                    starter.currenthp = starter.maxhp
                    turn1 = 0    
               turn4 = turn4 + 1
     if chance > 5:
               printD ("You see something on the floor...")
               berry = random.randint(0,2)
               printD ("It's a " + berryNames[berry] + ". What a lucky find!")
               inventory[berry]+=1
               turn4 = turn4 + 1
     print ("----------------------------------------------------------------------------------------------------")
printD ("You made it... RIGHT???")
printD (".")
printD (".")
printD ("You see Veilstone Gym... right up ahead.")
printD ("It's time... or is it?")

choice = input("What do you want to do? \n\t(1)Go battle the Gym Leader! \n\t(2)Visit the Pokemon Center. \n\t(3)Go train some more! \n\t(4)Check your bag. \n")
beatgym = False
while (choice == "1" or choice == "2" or choice == "3" or choice == "4"):
     if choice == "1":
          phantomforce = move("Phantom Force!", 39)
          gym3 = pokemon("Roserade", 11, 120, 120, 0, phantomforce,[],[])
          battle(starter,gym3)
          if result == True:
               beatgym = True
          else:
               print ("You lost the Gym battle :( \nHeal your Pokemon and train up!")
     if choice == "2":
          printD ("Let's make sure " + starter.name + " is recovered before we battle again.")
          starter.currenthp = starter.maxhp
          printD ("" + starter.name + "'s HP has been fully restored!")
     if choice == "3":
          #wildbattle
          print ("Pokemon Battle here")
          wildbattle = random.randint(0,1)
          wild = [starly,bidoof]
          result = battle(starter,wild[wildbattle])
          berryfind = random.randint(1,2)
          if result == False:
               print ("You lost, start at the beginning again.") 
          berryfind = random.randint(1,2)
          if berryfind == 1:
               berry = random.randint(0,2)
               printD ("It's a " + berryNames[berry] + ". What a lucky find!")
               inventory[berry]+=1
     if choice == "4":
          bag = input ("What do you want to do? \n\t(1)Berry \n\t(2)Badges \n")
          if bag == "1":
               print (badges)
          if bag == "2":
               print (inventory)
     if beatgym == True:
          break
     time.sleep(1)
     choice = input("What do you want to do? \n\t(1)Go battle the Gym Leader! \n\t(2)Visit the Pokemon Center. \n\t(3)Go train some more! \n\t(4)Check your bag. \n")
printD ("Let's get that badge!")
#MayleneBattle

printD ("That accursed ringing again.")
printD ("CONGRATULATIONS " + name + "!")
printD ("You have defeated Maylene, the third Gym Leader!")
printD ("jUsT lOoK aT tHaT sHiNy bAdGe! \n\tYou mocking whisper")

badges.append ("Cobble Badge")

choice = input("Check your new badge! \n\t(1)Bag \n\t(2)Do something else, that isn't checking your badge \n")
while choice != "1":
     if choice == "2":
          print ("Seriously, check your bag.")
     choice = input("Check your new badge! \n\t(1)Bag \n\t(2)Do something else, that isn't checking your badge \n")

bag = input ("What do you want to do? \n\t(1)Berry \n\t(2)Badges \n")
while choice != "2":
     if choice == "1":
          print ("It's really not the time for that right now...")
     choice = input("Check your new badge! \nWhat do you want to do? \n\t(1)Berry \n\t(2)Badges \n")

printD ("You look at your Badge Box in satisfaction.")
printD ("All three slots were filled.")
printD (".")
printD ("The call was still on.")
printD ("Come visit me at my lab again! To turn in that Badge Box!")
printD ("Are you serious... all the way back.")
printD (".")
printD (".")
printD ("A long.")
printD (".")
printD ("long.")
printD (".")
printD ("looooong. walk later.")
printD (".")
printD (".")
printD ("You bust open that door and find Professor Anaconda.")
printD ("Hey " + name + ", you finally made it back!")
printD ("Hand me that box you have.")
printD ("You take out your Badge Box and slowly hand it to the Professor")
printD ("You hesitantly place it in his hand, but also glad you finally completed it.")
printD ("You let out a sigh of relief.")
printD (".")
printD ("It's finally over, that was fun.")
printD ("You take a last glance at " + starter.name + ".")
printD ("It's been fun hasn't it.")
printD (".")
printD ("The Professor, confused, says 'What are you talking about?'")
printD ("You look behind him and see a stack of cases.")
printD (".")
printD (".")
printD ("Your adventure is only beginning...!")
printD (".")
printD (".")
printD (".")
printD ("Stay tuned, for Part 2!")







     
