class Dungeon:
    def __init__(self, monsters = []):
        self._monsters = monsters
    
    def add(self,monster):
        self._monsters.append(monster)
    
    def draw(self):
        try:
             return self._monsters.pop()
        except Exception:
            print "Dungeon is empty"
            
    def is_empty(self):
        if self._monsters == []:
            return True
        return False
        
    def __str__(self):
        out = ""
        for monster in self._monsters:
            out += "[" + str(monster.value) + "," + monster.name + "]"
        return out