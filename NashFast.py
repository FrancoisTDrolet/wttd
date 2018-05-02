from copy import *

MAX_WINS = 5
MAX_DEATHS = 1

sre_quick_index = []
e_quick_index = []

template = []

for i in range(MAX_WINS+1):
    a = []
    for j in range(MAX_DEATHS+1):
        b = []
        for k in range(MAX_WINS+1):
            c =[]
            for L in range(MAX_DEATHS+1):
                c.append(None)
            b.append(c)
        a.append(b)
    template.append(a)
    
sre_quick_index = deepcopy(template)
e_quick_index = deepcopy(template)      

def success_rate_equilibria(hero_wins, hero_deaths, vilain_wins,
                             vilain_deaths):
    if not(sre_quick_index[hero_wins][hero_deaths][vilain_wins][vilain_deaths] is None):
        return sre_quick_index[hero_wins][hero_deaths][vilain_wins][vilain_deaths]
        
    a = expectation(hero_wins + 1, hero_deaths, vilain_wins, vilain_deaths)
    b = expectation(hero_wins, hero_deaths + 1, vilain_wins, vilain_deaths)
    c = expectation(hero_wins, hero_deaths, vilain_wins + 1, vilain_deaths)
    d = expectation(hero_wins, hero_deaths, vilain_wins, vilain_deaths + 1)
    
    result = (d-b)/(a-b-c+d)
    sre_quick_index[hero_wins][hero_deaths][vilain_wins][vilain_deaths] = result
    
    return result
    
def expectation(hero_wins, hero_deaths, vilain_wins, vilain_deaths):
    if not(e_quick_index[hero_wins][hero_deaths][vilain_wins][vilain_deaths] is None):
        return e_quick_index[hero_wins][hero_deaths][vilain_wins][vilain_deaths]
    
    if hero_wins >= MAX_WINS or vilain_deaths >= MAX_DEATHS:
        return 1.0
    
    if hero_deaths>= MAX_DEATHS or vilain_wins >= MAX_WINS:
        return 0.0
        
    x = success_rate_equilibria(hero_wins, hero_deaths, vilain_wins,
                                vilain_deaths)
    a = expectation(hero_wins + 1, hero_deaths, vilain_wins, vilain_deaths)
    b = expectation(hero_wins, hero_deaths + 1, vilain_wins, vilain_deaths)
    
    result = (a-b)*x + b
    e_quick_index[hero_wins][hero_deaths][vilain_wins][vilain_deaths] = result
    return (a-b)*x + b
    
    
print success_rate_equilibria(0,0,0,0)
print expectation(0,0,0,0)