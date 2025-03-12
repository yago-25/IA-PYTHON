# Exercício 3 - Mapa Mundi

class State:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def density(self):
        return self.population / self.area if self.area > 0 else 0

    def __str__(self):
        return f"estado: {self.name}, população: {self.population}, area: {self.area} km2, densidade: {self.density():.2f} habitantes/km2"


class Country:
    def __init__(self, name, capital, states=None):
        self.name = name
        self.capital = capital
        self.states = states if states else []

    def add_state(self, state):
        self.states.append(state)

    def total_population(self):
        return sum(state.population for state in self.states)

    def __str__(self):
        return f"país: {self.name}, capitar: {self.capital}, populacao total: {self.total_population()}"


class WorldMap:
    def __init__(self):
        self.countries = []

    def add_country(self, country):
        self.countries.append(country)

    def total_population(self):
        return sum(country.total_population() for country in self.countries)

    def __str__(self):
        return f"mapa mundi - paises: {len(self.countries)}, populacao geral: {self.total_population()}"


sp = State("sp", 45000000, 248222)
rj = State("rj", 17366189, 43780)

brasil = Country("brasil", "brasilia")
brasil.add_state(sp)
brasil.add_state(rj)

world = WorldMap()
world.add_country(brasil)

print(sp)
print(rj)
print(brasil)
print(world)
