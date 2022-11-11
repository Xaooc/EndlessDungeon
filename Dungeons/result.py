from random import randint


class Result:
    def __init__(self, difficulty: int, res: int):
        self.res = res
        self.difficulty = difficulty
        self.damage = randint(1, (self.difficulty - 10) // 2)
        self.gold = randint(1, self.difficulty)

        self.result = {
            1: {'description': f'\n\nВы получаете {self.damage} урона!',
                'effect': -1*self.damage,
                'type': 'damage'},
            2: {'description': f'\n\nВы теряете {self.gold} золота!',
                'effect': -1*self.gold,
                'type': 'gold'},
            3: {'description': f'\n\nВы восстанавливаете {self.damage} здоровья!',
                'effect': self.damage,
                'type': 'damage'},
            4: {'description': f'\n\nВы получаете {self.gold} золота!',
                'effect': self.gold,
                'type': 'gold'},
            0: {'description': '',
                'effect': 0,
                'type': ''}
        }

     async def get_result(self) -> dict:
        return self.result.get(self.res)
