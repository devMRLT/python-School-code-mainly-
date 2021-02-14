#Global Variables  
partyNames = ['Krogg', 'Glinda', 'Geoffrey']
#cannot use the orginal data because the int cannot be subsriptable
partyHP = [180, 120, 150] 
partyAttack = [20, 5, 15] 
partyDefense = [20, 20, 15] 
partyDead = [False, False, False]
bossAttack = 25 
bossDefense = 15 
bossHP = 500
#declare round variable
round1 = 1

#function Defs
    
def bossDamage(partyAttack,bossDefense, bossHP):
    # The boss's defence (-) attack from krogg
    damage1 = (bossDefense - partyAttack[0])
    # The boss's Defence (-) attack from Geoffrey
    damage3 = (bossDefense - partyAttack[2]) 
    #Takes off the damage form the health
    bossHP - damage1 - damage3
    return bossHP
    
def partyDamage(partyDefense, bossAttack, partyHP):
    #damage calc against the defense
    bossdoesDamage1 = (partyDefense[0] - bossAttack)
    bossdoesDamage2 = (partyDefense[1] - bossAttack)
    bossdoesDamage3 = (partyDefense[2] - bossAttack)
    #damage taken off by the health
    partyHP[0] = partyHP[0] + bossdoesDamage1
    return partyHP[0]
    partyHP[1] = partyHP[1] + bossdoesDamage2
    return partyHP[1]
    partyHP[2] = partyHP[2] + bossdoesDamage3
    return partyHP[2]
    #heals all the party if still alive
def partyHeal(partyHP, partyAttack):
    partyHP[0] = (partyHP[0] + partyAttack[1])
    return partyHP[0]
    partyHP[1] = ((partyHP[1] + partyAttack[1]))
    return partyHP[1]
    partyHP[2] = ((partyHP[2] + partyAttack[1]))
    return partyHP[2]
    #check if the party is dead
def isPartydead(partyHP, partyNames, playerAttack):
    if(partyHP[0] <= 0):
        print(partyNames[0], "is dead and has zero hp")
        partyDead[0] = True
        return  partyDead[0]
        partyAttack[0] = 0
        return partyAttack[0]
    else:
        print(partyNames[0], "has", partyHP[0], "HP left.\n")
    if(partyHP[1] <= 0):
        print(partyNames[1], "is dead and has zero hp")
        partyDead[1] = True
        return  partyDead[1]
        partyAttack[1] = 0
        return partyAttack[1]
    else:
        print( partyNames[1], "has", partyHP[1], "HP left.\n")
    if(partyHP[2] <= 0):
        print(partyNames[2], "is dead and has zero hp")
        partyDead[2] = True
        return  partyDead[2]
        partyAttack[2] = 0
        return partyAttack[2]
    else:
        print(partyNames[2], "has", partyHP[2], "HP left.\n")
        #check which party members are actually dead
def isDead(partyDead, partyAttack):
    if(partyDead[0] == True):
        partyAttack[0] = 0
        return partyAttack[0]
    if(partyDead[1] == True):
        partyAttack[1] = 0
        return partyAttack[1]
    if(partyDead[2] == True):
        partyAttack[2] = 0
        return partyAttack[2]
#Inital Statement
print("This is a great battle between", partyNames[0],",", partyNames[1],",", partyNames[2], "and the Boss.")

     # initalize the code
while(bossHP > 0 or partyDead[0] == True or partyDead[1] == True or partyDead[2] == True):
    round1 = round1 + 1
    print("Round #", round1)
      #functions called
    partyHP = partyDamage(partyDefense, bossAttack, partyHP)
    partyHP = partyHeal(partyHP, partyAttack)
    bossHP = bossDamage(partyAttack,bossDefense, bossHP)
    partyDead = isPartydead(partyHP, partyNames, partyAttack)
    partyAttack = isDead(partyDead, partyAttack)
    if bossHP <= 0:
        print("Boss attacked by",  partyNames[0],",", partyNames[1],",", partyNames[2], "and has zero hp left.")
        print ("party has been victorious")
        break
        #end loop at this step if true
    elif  bossHP <= 0 and partyDead[0] == False and partyDead[1] == False and partyDead[2] == False:
        print("It was a tie, everyone is dead")
        break
        #end loop at this step if true 
    elif bossHP <= 0 and partyDead[0] == True and partyDead[1] == True and partyDead[2] == True:
        print("Boss was attacked by", partyNames[0],",", partyNames[1],",", partyNames[2], "and has", bossHP, "hp left.\n")
        

   
