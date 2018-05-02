class Item:
    def __init__(self,name,state = 0, bonus_hp = 0):
        self.name = name
        self.state = state
        self.bonus_hp = bonus_hp
        
class Vorpal_Blade(Item):
    def __init__(self):
        Item.__init__(self,"Vorpal Blade")
        
class Dragon_Lance(Item):
    def __init__(self):
        Item.__init__(self,"Dragon Lance")
        
class Plate_Armor(Item):
    def __init__(self):
        Item.__init__(self,"Plate Armor", bonus_hp = 5)
        
class Shield(Item):
    def __init__(self):
        Item.__init__(self,"Shield", bonus_hp = 3)
        
class Holy_Grail(Item):
    def __init__(self):
        Item.__init__(self,"Holy Grail")
        
class Torch(Item):
    def __init__(self):
        Item.__init__(self,"Torch")