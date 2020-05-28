from reportlab.lib.units import mm


class Col:
    def __init__(self):
        self.picture = 69 * mm
        self.profile = [25 * mm, 35 * mm, 25 * mm, 36 * mm]
        self.ability = 3 * [7 * mm, 8 * mm, 8 * mm]
        self.sanity_point = 20 * [6 * mm] + [1 * mm]
        self.magic_point = 8 * [7 * mm]
        self.durability = 9 * [7 * mm] + [2 * mm]
        self.skill = [32 * mm, 16 * mm, 32 * mm, 16 * mm, 32 * mm, 16 * mm, 31 * mm, 15 * mm]
        self.battle_skill = [26 * mm, 16 * mm, 21 * mm, 42 * mm, 21 * mm, 42 * mm, 22 * mm]
