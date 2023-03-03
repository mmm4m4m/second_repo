class Tomato:
    STATES = ("отсутствует", "цветение", "зеленый", "красный")

    def __init__(self, index):
        self._index = index + 1
        self._state = self.STATES[0]

    def grow(self):
        if not self.is_ripe():
            self._state = self.STATES[self.STATES.index(self._state) + 1]
            print(f'помидор №{self._index} на стадии "{self._state}"')
        else:
            print(f'помидор №{self._index} уже созрел')

    def is_ripe(self):
        return self._state == self.STATES[-1]


class TomatoBush:

    def __init__(self, count_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(count_tomatoes)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if not tomato.is_ripe():
                return False
        return True

    def give_away_all(self):
        tomatoes_list = self.tomatoes.copy()
        self.tomatoes.clear()
        return tomatoes_list


class Gardener:
    def __init__(self, name, tomato_bush: TomatoBush):
        self.name = name
        self._plant = tomato_bush
        self.bag = None

    def work(self):
        print('садовник работает...')
        self._plant.grow_all()
        print('садовник поработал')

    def harvest(self):
        print('садовник собирает урожай...')
        if not self._plant.all_are_ripe():
            print('урожай еще не созрел')
        else:
            self.bag = self._plant.give_away_all()
            print('урожай собран')

    @staticmethod
    def knowledge_base():
        print('справка: садовник может собрать помидоры, когда они полностью созреют, для этого следует за ними ухаживать.')


if __name__ == '__main__':
    tomato_bush = TomatoBush(5)
    gardener = Gardener('Виктор', tomato_bush)
    gardener.knowledge_base()
    gardener.harvest()
    while not tomato_bush.all_are_ripe():
        gardener.work()
    gardener.work()
    gardener.harvest()
