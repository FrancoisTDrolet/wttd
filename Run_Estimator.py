import Deck
import Dungeon
import Meta

import copy

class Run_Estimator:
    def __init__(self,champion, dead_monsters = [],known_monsters = [],players = []):
        self.champion = champion
        self.dead_monsters = dead_monsters
        self.known_monsters = known_monsters
        self.players = players
        self.deck_init = Deck.Deck()
        self.init_deck()
        
    def init_deck(self):
        self.deck_init = Deck.Deck()
        
        for monster in self.dead_monsters:
            self.deck_init.remove(monster.name)
            
        for monster in self.known_monsters:
            if monster == None:
                continue
            else:
                self.deck_init.remove(monster.name)
    
    def to_play_or_not(self,number_of_trials):
        test_hero = copy.deepcopy(self.players[0])
        test_vilains = copy.deepcopy(self.players[1:])
        
        last_vilain_win_winrate = Meta.Meta(copy.deepcopy(self.players[0]),copy.deepcopy(self.players[1:]))
        last_vilain_lose_winrate = 1
        hero_win_winrate =1
        hero_lose_winrate =1
        
    def choose_best_vorpal_state(self,number_of_trials):
        best_vorpal_state = 0
        best_rate = 0.0
        test_rate = 0.0
        for state in [1,2,3,4,5,6,7,9]:
            self.champion.set_item_state("Vorpal Blade",state)
            test_rate = self.success_rate(number_of_trials)
            if test_rate > best_rate:
                best_rate = test_rate
                best_vorpal_state = state
        self.champion.set_item_state("Vorpal Blade",best_vorpal_state)
                
        return best_vorpal_state, best_rate
            
    def success_rate(self,number_of_trials):
        success = 0
        for i in range(number_of_trials):
            self.champion.calc_hp()
            dungeon = self.new_filled_dungeon()
            while len(dungeon._monsters)>0:
                dungeon.draw().affect(self.champion)
            if self.champion.hp>0:
                success +=1
                
        return float(success)/number_of_trials
        
                
    def new_filled_dungeon(self):
        monsters = []
        temp_deck = copy.deepcopy(self.deck_init)
        temp_deck.shuffle()
        for monster in self.known_monsters:
            if monster == None:
                monsters.append(temp_deck.draw())
            else:
                monsters.append(monster)
        return Dungeon.Dungeon(monsters)
        