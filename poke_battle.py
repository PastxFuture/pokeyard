# Python Class Pokemon Battle

from typing import _SpecialForm


class Pokemon:
    
    # This gets called each time an instance is created
    def __init__(self, name, hp, damage, pokemon_type):
        self.name = name    # sets the name og the pokemon
        self.HP = hp    # The hit points or health of the pokemon
        self.damage = damage    # The amount of damage hits this pokemon does every attack
        self.pokemon_type = pokemon_type    # Determines the type of the pokemon

    
    def fighting_type(self):
        '''
        Creates a nested dictionary for the weaknesses when the first type attacks. You can then access the multiplier for a fire type attacking a grass type like this:
        attacking_dict['fire']['grass'] # yields 2.0
        '''

        self.attacking_dict = {
        'Fire': {'Fire': 0.5, 'Grass': 2.0, 'Water': 0.5}, 
        'Grass': {'Fire': 0.5, 'Grass': 0.5, 'Water': 2.0}, 
        'Water': {'Fire': 2.0, 'Grass': 0.5, 'Water': 0.5}
        }
        
        return self.attacking_dict 


    def battle(self, opponent):

        self.fighting_type()

        attackDamage = self.damage * self.attacking_dict[self.pokemon_type][opponent.pokemon_type]

        if self.HP > 0:
            print(f'{self.name} did {attackDamage} to {opponent.name}') # Text-based combat descriptors

            opponent.HP -= attackDamage # The damage you inflict upon the opponent is subtracted here

            print(f'{opponent.name} has {opponent.HP} HP left') # Text-based descriptor for the opponent's health

            return opponent.battle(self) # Now the Opponent pokemon attacks

        else:
            print(f'{opponent.name} wins! ({opponent.HP} HP left.)') # Declares the winner of the Battle
            
            return opponent, self  # Returns a tuple (Winner, Loser)


Squirtle = Pokemon('Squirtle', 100, 10, 'Water')
Bulbasaur = Pokemon('Bulbasaur', 100, 10, 'Grass')
Charmander = Pokemon('Charmander', 100, 10, 'Fire')

#Winner, Loser = Bulbasaur.battle(Squirtle)
#Winner, Loser = Charmander.battle(Squirtle)
Winner, Loser = Bulbasaur.battle(Charmander)

