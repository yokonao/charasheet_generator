class CharaPDF:
    pass


# generating object from JSON
def json_to_chara(data):
    chara = CharaPDF()
    for key, value in data.items():
        chara.__setattr__(key, value)
    return chara
