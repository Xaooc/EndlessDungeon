from random import sample, randint


class Rooms:
    def __init__(self):
        self.rooms = {
            1: {'description': 'Вы попадаете в комнату, покрытую паутиной и пылью. '
                               'Вокруг темнота и лишь свет факела позволяет оглядеть окружение.'
                               'У дальней стены виднеется дверь с запертым замком. '
                               'Сбоку можно разглядеть спуск вниз. Что будете делать?',
                'event': [1, 2]},
            2: {'description': '',
                'event': []},
            3: {'description': '',
                'event': []},
            4: {'description': '',
                'event': []},
            5: {'description': '',
                'event': []}
    }

    async def get_room(self, room: int) -> dict:
        return self.rooms.get(room)

    async def path(self) -> list:
        return sample(list(self.rooms.keys()), randint(3, 5))

