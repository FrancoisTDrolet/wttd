import Monster
import Deck
import Dungeon
import Champion
import Item
import Run_Estimator
import Player
import Meta

def step(dungeon,champion):
    monster_facing = dungeon.draw()
    monster_facing.affect(champion)
    return monster_facing

p1 = Player.Player()
p2 = Player.Player()
hero = Player.Player()
hero.win = 0

meta = Meta.Meta(hero,[p1])
print meta.get_hero_winrate(10000)

