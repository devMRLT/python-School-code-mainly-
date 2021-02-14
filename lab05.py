#Global Variables  
partyNames = ['Krogg', 'Glinda', 'Geoffrey']
#cannot use the orginal data because the int cannot be subsriptable
partyHP = [180, 120, 150] 
partyAttack = [20, 5, 15] 
partyDefense = [20, 20, 15] 
bossAttack = 25 
bossDefense = 25
bossHP = 500
#declare round variable
round1 = 1

#function Defs 
  
     #check if the party is dead
def isPartydead(partyHP, partyNames, playerAttack):
    if(partyHP[0] <= 0):
        print(partyNames[0], "cannot attack because he is dead!")
        partyAttack[0] = 0
        return partyAttack[0]
    else:
        print(partyNames[0], "has", partyHP[0], "HP left.\n")
        
    if(partyHP[1] <= 0):
        print(partyNames[1], "cannot attack because he is dead!")
        partyAttack[1] = 0
        return partyAttack[1]
    else:
        print( partyNames[1], "has", partyHP[1], "HP left.\n")
        
    if(partyHP[2] <= 0):
        print(partyNames[2], "cannot attack because he is dead!")
        partyAttack[2] = 0
        return partyAttack[2]
    else:
        print(partyNames[2], "has", partyHP[2], "HP left.\n")
        
        #check which party members are actually dead
def isDead(partyHP):
    val = 0
    for x in partyHP:
        if val <= 0:
            return False
        else:
            return True
        
#Inital Statement
print("This is a great battle between", partyNames[0],",", partyNames[1],",", partyNames[2], "and the Boss.")
    # The boss's defence (-) attack from krogg
damage1 = (bossDefense - partyAttack[0])
    # The boss's Defence (-) attack from Geoffrey
damage3 = (bossDefense - partyAttack[2]) 

    #damage calc against the defense
bossdoesDamage1 = (-1 * (partyDefense[0] - bossAttack))
bossdoesDamage2 = (-1 * (partyDefense[1] - bossAttack))
bossdoesDamage3 = (-1 * (partyDefense[2] - bossAttack))

     # initalize the code
while(bossHP > 0 or partyHP[0] > 0 or partyHP[1] > 0 or partyHP[2] > 0):
    round1 = round1 + 1
    
    #round count (done)
    print("Round #", round1)  
    
    #boss damage taken off (Done)
    bossHP = bossHP - (-1 * (damage1 - damage3))
    
    #damage taken off by the health party members
    partyHP[0] = partyHP[0] - bossdoesDamage1
    
    partyHP[1] = partyHP[1] - bossdoesDamage2
    
    partyHP[2] = partyHP[2] - bossdoesDamage3
    
     
    #Heals (Done)
    partyHP[0] = (partyHP[0] + partyAttack[1])
    partyHP[1] = (partyHP[1] + partyAttack[1])
    partyHP[2] = (partyHP[2] + partyAttack[1])
    
    #functions called (working)
    isPartydead(partyHP, partyNames, partyAttack)
    isDead(partyHP)
    
    if bossHP <= 0:
        print("Boss attacked by",  partyNames[0],",", partyNames[1],",", partyNames[2], "and has zero hp left!")
        print ("party has been victorious")
        break
        #end loop at this step if true
    elif  bossHP <= 0 and partyHP[0] <= 0 and partyHP[1] <= 0 and partyHP[2] <= 0:
        print("It was a tie, everyone is dead")
        break
        #end loop at this step if true 
    elif bossHP >= 0 and partyHP[0] >= 0 or partyHP[1] >= 0 or partyHP[2] >= 0:
        print("Boss was attacked by", partyNames[0],",", partyNames[1],",", partyNames[2], "and has", bossHP, "hp left.\n")
        print ("The boss has been victorious!")