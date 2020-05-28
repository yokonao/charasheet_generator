from reportlab.lib.units import mm


class Row:
    def __init__(self):
        self.picture = 68 * mm
        self.profile = 8 * mm
        self.ability = 8 * mm
        self.sanity_point = [8 * mm] + 5 * [6 * mm]
        self.magic_point = [8 * mm] + 3 * [7 * mm] + [1 * mm]
        self.durability = [8 * mm] + 3 * [7 * mm] + [1 * mm]
        self.skill = 7 * mm
        self.battle_skill = 7 * mm
