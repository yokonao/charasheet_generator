from reportlab.platypus import TableStyle
from reportlab.lib import colors
from display.style_snippet import get_overall, title, subtitle


picture_style = TableStyle([*get_overall(False)])

profile_style = TableStyle([
    *get_overall(True),
    *title,
    *[('SPAN', (1, i), (3, i)) for i in range(5)]
])

ability_style = TableStyle([
    *get_overall(True),
    *title,
    *[('SPAN', (0, i), (1, i)) for i in range(1, 5)],
    *[('SPAN', (3, i), (4, i)) for i in range(1, 5)],
    *[('SPAN', (6, i), (7, i)) for i in range(1, 5)],
    ('SPAN', (0, 5), (2, 5)),
    ('SPAN', (4, 5), (7, 5)),
])

sanity_point_style = TableStyle([
    *get_overall(False),
    *title,
])

magic_point_style = TableStyle([
    *get_overall(False),
    *title,
])

durability_style = TableStyle([
    *get_overall(False),
    *title,
])

magic_point_style = TableStyle([
    *get_overall(False),
    *title,
])

skill_style = TableStyle([
    *get_overall(True),
    *title,
    *subtitle(y=[1, 5, 9, 11, 15]),
    ('BOX', (0, 1), (-1, 4), 1, colors.black),
    ('BOX', (0, 5), (-1, 8), 1, colors.black),
    ('BOX', (0, 9), (-1, 10), 1, colors.black),
    ('BOX', (0, 11), (-1, 14), 1, colors.black),
])

battle_skill_style = TableStyle([
    *get_overall(True),
    *title,
    # sections
    ('LINEAFTER', (2, 0), (2, -1), 0.01, colors.black),
    ('LINEAFTER', (4, 0), (4, -1), 0.01, colors.black),
])
