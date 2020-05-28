# cell size of each table
from display.col import Col
from display.row import Row


class Cell:
    def __init__(self):
        self.col = Col()
        self.row = Row()
        self.picture = (self.col.picture, self.row.picture)
        self.profile = (self.col.profile, self.row.profile)
        self.ability = (self.col.ability, self.row.ability)
        self.sanity_point = (self.col.sanity_point, self.row.sanity_point)
        self.magic_point = (self.col.magic_point, self.row.magic_point)
        self.durability = (self.col.durability, self.row.durability)
        self.skill = (self.col.skill, self.row.skill)
        self.battle_skill = (self.col.battle_skill, self.row.battle_skill)
