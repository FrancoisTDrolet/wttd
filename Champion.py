import Item

class Champion:
    def __init__(self,name,items = [], base_hp = 0):
        self._name = name
        self.items = items
        self._base_hp = base_hp
        
        self.hp = 0
        
        self.calc_hp()
        
    def calc_hp(self):
        self.hp = self._base_hp
        for item in self.items:
            self.hp += item.bonus_hp
            
    def remove_item(self,item_name):
        self.items = [item for item in self.items if item.name!=item_name]
        self.calc_hp()
        
    def set_item_state(self,item_name,state):
        [item for item in self.items if item.name == item_name][0].state = state
        
    def get_item_state(self,item_name):
        return [item for item in self.items if item.name == item_name][0].state

class Warrior(Champion):
    def __init__(self):
        items = []
    
        items.append(Item.Vorpal_Blade())
        items.append(Item.Dragon_Lance())
        items.append(Item.Plate_Armor())
        items.append(Item.Shield())
        items.append(Item.Holy_Grail())
        items.append(Item.Torch())
        
        Champion.__init__(self,"Warrior",items,3)
        