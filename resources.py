from exceptions import NotEnoughResources, NotValidResource

valid_resources = {'court actions', 'gold', 'swords'}

class Resource:
    def __init__(
            self,
            name: str,
            amount: int = 0,
            ):
        if name not in valid_resources:
            raise NotValidResource(valid_resources)

        self.name = name
        self.amount = amount

    def gain(
            self,
            quantity
            ):
        self.amount += quantity
        print(f"You gain {quantity} {self.name}, you now have {self.amount}")

    def lose(
            self,
            quantity
            ):
        if quantity > self.amount:
            raise NotEnoughResources(self.amount, quantity, self.name)
        self.amount -= quantity
        print(f"You lose {quantity} {self.name}, you now have {self.amount}")

    def check(
            self
            ):
        return self.amount


if __name__ == '__main__':
    courtAction = Resource(name = 'court actions', amount=3)
    gold = Resource(name = 'gold', amount=5)
    swords = Resource(name = 'swords', amount=0)

