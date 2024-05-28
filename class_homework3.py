class Buiding:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = f'Этажность здания: {numberOfFloors}.'
        self.buildingType = f'\nТип постройки: {buildingType}.'

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
Home1 = Buiding(3, 'Барнхаус')
Home2 = Buiding(3, 'Барнхаус')
print(Home1.numberOfFloors, Home1.buildingType)
print(Home1 == Home2)
# т.к. при обращении к объектам класса я задал одинаковые позиционные параметры (оба здания 3-ех этажные, оба
# типа Барнхаус, соответственно они равны, т.е условно одинаковые