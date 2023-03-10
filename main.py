class Footballer:
    def __init__(self, movement, team, item):
        self.__movement = movement
        self.__team = team
        self.__item = item

    @property
    def movement(self):
        return self.__movement

    @movement.setter
    def movement(self, movement):
        self.__movement = movement

    def get_team(self):
        return self.__team

    def set_team(self, team):
        self.__team = team

    @property
    def item(self):
        return self.__item

    def set_item(self):
        return self.item


footballer = Footballer("Forward", "Arsenal", "red football uniform ")
footballer2 = Footballer("Defender", "Barcelona", "yellow football uniform")

print(footballer.movement)
print(footballer.get_team())
print(footballer.item, "\n")
print(footballer2.movement)
print(footballer2.get_team())
print(footballer2.item, "\n")

