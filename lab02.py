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
kroggAttack = 18.5
kroggDefense = 12.5
kroggHP = 200
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
darkdragonDefense = 17.5
darkdragonHP = 500
darkdragonXP = 1000
darkdragonWeapons = ['Flame Breath']

dark_dragon = [darkdragonName, darkdragonClass, darkdragonLevel, darkdragonAttack, 
               darkdragonDefense, darkdragonHP, darkdragonXP, darkdragonWeapons]

    # list of stats to be called for game
party = [glinda, krogg, geoffrey]

    # variables to be changed i = character j = attack
i = 0
j = 3
damage = (party[i][j] - dark_dragon[4])
     # Conditions for if damage is less than 0 and output
print("Dark Dragon (Boss) has", dark_dragon[4],"defense", "and", dark_dragon[5], "hp." )
if damage < 0:
	print("No damage was dealt to", dark_dragon[0], "when", party[i][0], "attacked him!")
else:
    print("The final hp after being attacked by", party[i][0], "is ", dark_dragon[5] - damage)



