import Player
import random
import copy

class Meta:
    def __init__(self,hero,players):
        self.players = players
        self.hero = hero
        
    def get_hero_winrate(self,number_of_trials):
        winrate = 0.0
        
        for i in range(number_of_trials):
            test_players = copy.deepcopy(self.players)
            test_hero = copy.deepcopy(self.hero)
            everyone = test_players+[test_hero]
            while len(everyone)>1:
                random_crawler = random.choice(everyone)
                if random.randint(0,1)==1:
                    random_crawler.win+=1
                    if random_crawler.win == 2:
                        if random_crawler == test_hero:
                            winrate += 1
                            break
                        else:
                            break
                else:
                    random_crawler.life-=1
                    if random_crawler.life == 0:
                        if random_crawler == test_hero:
                            break
                        else:
                            everyone.remove(random_crawler)
            if len(everyone) == 1:
                winrate += 1
                
        return winrate/number_of_trials
    