from reportlab.lib import colors


def get_overall(innergrid):
    overall = [
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('FONT', (0, 0), (-1, -1), 'GenShinGothic', 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]
    if innergrid:
        overall.append(('INNERGRID', (0, 0), (-1, -1), 0.1, colors.black))
    return overall


title = [
    ('FONT', (0, 0), (-1, 0), 'GenShinGothic', 12),
    ('BACKGROUND', (0, 0), (-1, 0), colors.salmon),
    ('BOX', (0, 0), (-1, 0), 1, colors.black),
    ('SPAN', (0, 0), (-1, 0)),
]


def subtitle(y):
    style_arg = []
    for i in y:
        style_arg += [
            ('BACKGROUND', (0, i), (0, i), colors.darksalmon),
            ('BOX', (0, i), (1, i), 1, colors.black),
            ('SPAN', (0, i), (1, i)),
        ]
    return style_arg
