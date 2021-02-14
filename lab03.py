glindaName = 'Glinda'
glindaClass = 'Spellcaster'
glindaLevel = 1
glindaAttack = 4.5
glindaDefense = 25.0
glindaHP = 120
glindaXP = 0
glindaWeapons = ['Staff', 'Unarmed']
glinda = [glindaName, glindaClass, glindaLevel, glindaAttack, glindaDefense, glindaHP, glindaXP, glindaWeapons]

# kroggs stats
kroggName = 'Krogg'
kroggClass = 'Warrior'
kroggLevel = 1
kroggAttack = 38.5
kroggDefense = 20
kroggHP = 20
kroggXP = 0
kroggWeapons = ['Axe', 'Dagger', 'Unarmed']
krogg = [kroggName, kroggClass, kroggLevel, kroggAttack, 
kroggDefense, kroggHP, kroggXP, kroggWeapons]

    # geoffrey stats
geoffreyName = 'geoffrey'
geoffreyClass = 'Paladin'
geoffreyLevel = 1
geoffreyAttack = 15.0
geoffreyDefense = 12.5
geoffreyHP = 180
geoffreyXP = 0
geoffreyWeapons = ['Bow', 'Sword']
geoffrey = [geoffreyName, geoffreyClass, geoffreyLevel, geoffreyAttack,
geoffreyDefense, geoffreyHP, geoffreyXP, geoffreyWeapons]
    # darkdragon stats
darkdragonName = 'Dark Dragon'
darkdragonClass = 'Boss'
darkdragonLevel = 10
darkdragonAttack = 25
darkdragonDefense = 40
darkdragonHP = 250
darkdragonXP = 1000
darkdragonWeapons = ['Flame Breath']

dark_dragon = [darkdragonName, darkdragonClass, darkdragonLevel, darkdragonAttack, 
               darkdragonDefense, darkdragonHP, darkdragonXP, darkdragonWeapons]

    # list of stats to be called for game
party = [glinda, krogg, geoffrey]
    # variables to be changed i = character j = attack
i = 1
j = 3
    # The damage variables + round code
damage1 = ( - (krogg[4] - dark_dragon[3]))
damage2 = (dark_dragon[4] - krogg[3])
round1 = 1

print("This is a great battle between", party[i][0], "and ", dark_dragon[0])
     # loop for attack
while dark_dragon[5] > 0 and party[i][5] > 0:
    #initalzes the branching
  if damage1 < 0 and damage2 < 0:
   print("But no damage was given it was a tie") 
   break
  else:
    print("Round #",round1)
    #damage equalling zero
    if damage1 < 0:
        damage1 = 0
    dark_dragon[5] = dark_dragon[5] - damage1
    if dark_dragon[5] < 0:
        print("Dark Dragon was attacked by", party[i][0], "and has zero hp left.")
    else:
        print("Dark Dragon was attacked by", party[i][0], "and has", dark_dragon[5], "hp left.")
        #check for damage equalling zero
        if damage2 < 0:
             damage2 = 0
        party[i][5] = party[i][5] - damage2
    if party[i][5] < 0:
        print(party[i][0], "was attacked by Dark Dragon and now has zero hp left.")
    else:
        print(party[i][0], "was attacked by Dark Dragon and now has", party[i][5], "hp left.")
    round1 = round1 + 1
    if dark_dragon[5] <= 0:
        print ("Krogg has been victorious")
        break
    elif party[i][5] <= 0:
        print (" Dark Dragon has been victorous")
        break
    elif party[i][5] == 0 and dark_dragon[5] == 0:
        print("It was a tie")