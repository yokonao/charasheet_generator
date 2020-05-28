from reportlab.platypus import Table
from display.table_config import TableConfig


class CreateTable(Table):
    def __init__(self, name, data_dict, pdf_canvas):
        self.config = TableConfig(name, data_dict)
        super().__init__(self.config.data, colWidths=self.config.cell[0],
                         rowHeights=self.config.cell[1], style=self.config.style)
        self.position = self.config.position
        self.pdf_canvas = pdf_canvas
        self.drawing()

    def drawing(self):
        self.wrapOn(self.pdf_canvas, self.position[0], self.position[1])
        self.drawOn(self.pdf_canvas, self.position[0], self.position[1])
