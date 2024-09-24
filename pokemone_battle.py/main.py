import time
import numpy as np
import sys

# Delay printing

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Create the class
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='==================='):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # Amount of health bars


    def fight(self, Pokemon2):
        # Allow two pokemon to fight each other
    
        # Print fight information
        print("-----POKEMON BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))
    
        time.sleep(2)
    
        # Default attack messages
        string_1_attack = '\nIt had no effect...'
        string_2_attack = '\nIt had no effect...'
    
        # Consider type advantages
        version = ['Fire', 'Water', 'Grass']
        for i, k in enumerate(version):
            if self.types == k:
                # Both are the same type
                if Pokemon2.types == k:
                    string_1_attack = '\nIt\'s not very effective...'
                    string_2_attack = '\nIt\'s not very effective...'
    
                # Pokemon2 is STRONG
                elif Pokemon2.types == version[(i+1) % 3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIt\'s not very effective...'
                    string_2_attack = '\nIt\'s super effective!'
    
                # Pokemon2 is WEAK
                elif Pokemon2.types == version[(i+2) % 3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nIt\'s super effective!'
                    string_2_attack = '\nIt\'s not very effective...'
    
        # Now for the actual fighting...
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # Print the health of each pokemon
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
    
            # Player 1 attacks
            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)
    
            # Determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""
    
            # Add back bars plus defense boost
            for j in range(int(Pokemon2.bars + .1 * Pokemon2.defense)):
                Pokemon2.health += "="
    
            time.sleep(1)
            print(f"\n{self.name}\t\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)
    
            # Check to see if Pokemon fainted
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' fainted.')
                break
    
            # Pokemon2's turn
            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)
    
            # Determine damage
            self.bars -= Pokemon2.attack
            self.health = ""
    
            # Add back bars plus defense boost
            for j in range(int(self.bars + .1 * self.defense)):
                self.health += "="
    
            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)
    
            # Check to see if Pokemon fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')
                break
    
        money = np.random.choice(5000)
        delay_print(f"\nOpponent paid you ${money}.\n")



# Function to display available Pokemon and allow player to choose
def choose_pokemon(pokemon_list):
    print("Choose your Pokémon:")
    for idx, pokemon in enumerate(pokemon_list):
        print(f"{idx+1}. {pokemon.name} (Type: {pokemon.types}, Attack: {pokemon.attack}, Defense: {pokemon.defense})")
    
    choice = int(input("\nEnter the number of your choice: ")) - 1
    return pokemon_list[choice]

if __name__ == '__main__':
    # List of available Pokemon
    pokemon_list = [
        Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE': 8}),
        Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'], {'ATTACK':10, 'DEFENSE':10}),
        Pokemon('Venusaur', 'Grass', ['Vine Whip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'], {'ATTACK':8, 'DEFENSE':12}),
        Pokemon('Pyronix', 'Fire', ['Lava Plume', 'Heat Wave', 'Dragon Claw', 'Inferno'], {'ATTACK':14, 'DEFENSE':7}),
        Pokemon('Aquafy', 'Water', ['Aqua Jet', 'Tsunami Crash', 'Whirlpool', 'Ice Fang'], {'ATTACK':11, 'DEFENSE':9}),
        Pokemon('Thornix', 'Grass', ['Leaf Storm', 'Thorn Whip', 'Earthquake', 'Solar Beam'], {'ATTACK':12, 'DEFENSE':10}),
        Pokemon('Voltanic', 'Electric', ['Thunder Shock', 'Volt Tackle', 'Plasma Punch', 'Electric Surge'], {'ATTACK':13, 'DEFENSE':8}),
        Pokemon('Cryogale', 'Ice', ['Ice Beam', 'Blizzard', 'Frostbite', 'Cold Snap'], {'ATTACK':10, 'DEFENSE':11}),
        Pokemon('Shadowfang', 'Dark', ['Shadow Claw', 'Dark Pulse', 'Night Slash', 'Phantom Bite'], {'ATTACK':13, 'DEFENSE':9}),
        Pokemon('Terabyte', 'Steel', ['Iron Tail', 'Hyper Beam', 'Magnet Slam', 'Steel Crush'], {'ATTACK':15, 'DEFENSE':12}),
        Pokemon('Zephyrix', 'Flying', ['Sky Attack', 'Hurricane', 'Air Slash', 'Gale Force'], {'ATTACK':12, 'DEFENSE':9}),
        Pokemon('Lumisect', 'Bug', ['Bug Buzz', 'Luminous Wings', 'Sting Shot', 'Pollen Storm'], {'ATTACK':9, 'DEFENSE':7})
    ]

    # Choose Pokémon for both players
    print("Player 1, choose your Pokémon:")
    player1_pokemon = choose_pokemon(pokemon_list)

    print("\nPlayer 2, choose your Pokémon (or AI opponent):")
    player2_pokemon = choose_pokemon(pokemon_list)

    # Start the battle
    player1_pokemon.fight(player2_pokemon)
