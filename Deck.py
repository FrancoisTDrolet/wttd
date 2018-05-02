import random

import Monster

class Deck:
    def __init__(self):
        self._monsters = []
        self.reset()
    
    def reset(self):
        self._monsters = []
        
        for i in range(2):
            self._monsters.append(Monster.Goblin())
            self._monsters.append(Monster.Skeleton())
            self._monsters.append(Monster.Orc())
            self._monsters.append(Monster.Vampire())
            self._monsters.append(Monster.Golem())
        
        self._monsters.append(Monster.Lich())
        self._monsters.append(Monster.Demon())
        self._monsters.append(Monster.Dragon())
        
        self.shuffle()
        
    def shuffle(self):
        random.shuffle(self._monsters)
        
    def draw(self):
        try:
            return self._monsters.pop()
        except Exception:
            print "Deck is empty"
            
    def remove(self,monster_name):
        for monster in self._monsters:
            if monster.name == monster_name:
                self._monsters.remove(monster)
                return
        raise Exception("No Monster of that name in Deck")
        
    def __str__(self):
        out = ""
        for monster in self._monsters:
            out += "[" + str(monster.value) + "," + monster.name + "]"
        return out
        
if __name__ == "__main__":
    deck = Deck()
    for monster in deck._monsters:
        print monster.name