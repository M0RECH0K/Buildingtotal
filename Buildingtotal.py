from random import choice, randint


class Buiding:
    total = 0

    def __init__(self, name='Объект'):
        self.name = name
        self.numberOfFloors = randint(1, 15)
        self.buildingType = choice(['Из кирпича', 'Из дерева', 'Из бетона', 'Из арболита'])
        Buiding.total += 1

    def __str__(self):
        list_ = list(map(lambda x, y: '\t' + str(x) + ' = ' + str(y) + '\n', self.__dict__.keys(),
                         self.__dict__.values()))
        return f'\n' + ' '.join(list_)


buid_list = [Buiding('Объект №' + str(i)) for i in range(1, 41)]

print(*buid_list)
print('Всего объектов:', Buiding.total)
