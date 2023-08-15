### defining the player class
from resources import Resource

class Player:
    def __init__(
            self,
            court_actions = Resource(name='court actions', amount=3),
            gold = Resource(name='gold', amount=5),
            sword = Resource(name='swords', amount=0),
            name = 'Player0'
            ):
        self.court_actions = court_actions
        self.gold = gold
        self.swords = sword
        self.name = name
        self.resource_mapping = {
                'court actions' : self.court_actions,
                'gold' : self.gold,
                'swords' : self.swords
                }

    def gain_resource(self, resource_name, quantity):
        resource = self.resource_mapping[resource_name]
        resource.gain(quantity)
        
    def lose_resource(self, resource_name, quantity):
        resource = self.resource_mapping[resource_name]
        resource.lose(quantity)

    def check_resource(self, resource_name):
        resource = self.resource_mapping[resource_name]
        quantity = resource.check()
        print(f"The player {self.name} has {quantity} {resource_name}")


if __name__ == '__main__':
    gennaro = Player(name = 'Gennaro')
    gennaro.gain_resource('swords', 3)
    gennaro.gain_resource('court actions', 12)

    gennaro.check_resource('court actions')
