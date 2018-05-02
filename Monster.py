class Monster:
    def __init__(self,value,name):
        self.value = value
        self.name = name
        
class Goblin(Monster):
    def __init__(self):
        Monster.__init__(self,1,"Goblin")
        
    def affect(self,champion):      
        for item in champion.items:
            if (item.name == "Vorpal Blade" and item.state == self.value):
                return                
            if item.name == "Torch":
                return   
        champion.hp -= self.value
        
            
class Skeleton(Monster):
    def __init__(self):
        Monster.__init__(self,2,"Skeleton")
        
    def affect(self,champion):
        for item in champion.items:
            if item.name == "Torch":
                return                
            if item.name == "Holy Grail":
                return               
            if (item.name == "Vorpal Blade" and item.state == self.value):
                return
        champion.hp -= self.value
            
class Orc(Monster):
    def __init__(self):
        Monster.__init__(self,3,"Orc")
        
    def affect(self,champion):        
        for item in champion.items:
            if item.name == "Torch":
                return
            if (item.name == "Vorpal Blade" and item.state == self.value):
                return
        champion.hp -= self.value
            
class Vampire(Monster):
    def __init__(self):
        Monster.__init__(self,4,"Vampire")
        
    def affect(self,champion):                
        for item in champion.items:
            if item.name == "Holy Grail":
                return
            if (item.name == "Vorpal Blade" and item.state == self.value):
                return
        champion.hp -= self.value
            
class Golem(Monster):
    def __init__(self):
        Monster.__init__(self,5,"Golem")
        
    def affect(self,champion):
        for item in champion.items:
            if (item.name == "Vorpal Blade" and item.state == self.value):
                return
        champion.hp -= self.value
        
class Lich(Monster):
    def __init__(self):
        Monster.__init__(self,6,"Lich")
        
    def affect(self,champion):          
        for item in champion.items:
            if item.name == "Holy Grail":
                return
            if (item.name == "Vorpal Blade" and item.state == self.value):
                return
        champion.hp -= self.value
            
class Demon(Monster):
    def __init__(self):
        Monster.__init__(self,7,"Demon")
        
    def affect(self,champion):
        for item in champion.items:
            if (item.name == "Vorpal Blade" and item.state == self.value):
                return
        champion.hp -= self.value
        
class Dragon(Monster):
    def __init__(self):
        Monster.__init__(self,9,"Dragon")
        
    def affect(self,champion):        
        for item in champion.items:
            if item.name == "Dragon Lance":
                return
            if (item.name == "Vorpal Blade" and item.state == self.value):
                return
        champion.hp -= self.value