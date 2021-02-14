"""
v3.007
@author: Nathaniel Armogan
"""
#--------------------------------------Class Section------------------------#
class Character():
    def __init__(self, name, hp, attack, defense):
        self.name = ''
        self.hp = 0
        self.attack = 0
        self.defense = 0
        self.maxhp = 0
    def __str__(self):#display the current health points for the character
        return (self.name, ' has ', self.hp, 'HP.')
    #check if the individual is dead
    def isDead(self):
        if self.hp <= 0:
            return True
        else:
            return False
     #attack code      
    def attack(self, othercharacter):
        othercharacter.hp = othercharacter.hp + (othercharacter.defense  - self.attack)
    #give health back to the party from glinda
    def heal(self, party):
       party.hp = party.hp + self.attack
#-------------------Functions-----------------------------------------------#
def isPartydead(party):#issue is with this function!!!!
#check each part member
    for partyMember in party:
        if partyMember.hp >= 0:
            return False
        elif partyMember.hp <= 0:
            return True
            

#----------------Main------------------------------------------------------#  
#party Members
krogg = Character('Krogg',180, 20, 20)
glinda = Character('Glinda', 120, 5, 20)
geoffrey = Character('Geoffrey',150, 15, 15)
party = [krogg, glinda, geoffrey]

#boss
boss = Character('Boss', 500, 25, 15)
#initate the inital round number
rnum = 1
#Start Battle
while((not boss.isDead()) and (not isPartydead(party))):
    print("Round", rnum)
    #krogg attacks 
    krogg.attack(boss)
    #----------------
    #geoffrey attacks
    geoffrey.attack(boss)
    #--------------------
    #glinda heals
    glinda.heal(party)
    #--------------------
    #boss attacks
    for partyMember in party:
        print(partyMember)
    print(boss)
    print('')
    
    #count the round number up
    rnum += 1
if isPartydead(party):
    print('Your whole party is dead. You lose.')
elif boss.isDead():
    print("The boss is dead. You are victorious!")
        