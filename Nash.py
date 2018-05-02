MAX_WINS = 10
MAX_DEATHS = 10

def success_rate_equilibria(hero_wins, hero_deaths, vilain_wins,
                             vilain_deaths):
    a = expectation(hero_wins + 1, hero_deaths, vilain_wins, vilain_deaths)
    b = expectation(hero_wins, hero_deaths + 1, vilain_wins, vilain_deaths)
    c = expectation(hero_wins, hero_deaths, vilain_wins + 1, vilain_deaths)
    d = expectation(hero_wins, hero_deaths, vilain_wins, vilain_deaths + 1)
    
    return (d-b)/(a-b-c+d)
    
def expectation(hero_wins, hero_deaths, vilain_wins, vilain_deaths):
    if hero_wins >= MAX_WINS or vilain_deaths >= MAX_DEATHS:
        return 1.0
    
    if hero_deaths>= MAX_DEATHS or vilain_wins >= MAX_WINS:
        return 0.0
        
    x = success_rate_equilibria(hero_wins, hero_deaths, vilain_wins,
                                vilain_deaths)
    a = expectation(hero_wins + 1, hero_deaths, vilain_wins, vilain_deaths)
    b = expectation(hero_wins, hero_deaths + 1, vilain_wins, vilain_deaths)
    
    return (a-b)*x + b
    
    
print success_rate_equilibria(1,0,0,0)
print expectation(1,0,0,0)