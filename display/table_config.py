# configuration object for creating table
from display.data import Data
from display.cell import Cell
from display.position import Position
from display.styles import Style


class TableConfig:
    def __init__(self, name, data_dict):
        self.data = Data(data_dict).__getattribute__(name)
        self.cell = Cell().__getattribute__(name)
        self.style = Style().__getattribute__(name)
        self.position = Position().__getattribute__(name)
