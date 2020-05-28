from reportlab.lib.units import mm


class Position:
    def __init__(self):
        self.picture = (10 * mm, 219 * mm)
        self.profile = (79 * mm, 239 * mm)
        self.ability = (10 * mm, 171 * mm)
        self.sanity_point = (79 * mm, 201 * mm)
        self.magic_point = (79 * mm, 171 * mm)
        self.durability = (135 * mm, 171 * mm)
        self.skill = (10 * mm, 45 * mm)
        self.battle_skill = (10 * mm, 10 * mm)
