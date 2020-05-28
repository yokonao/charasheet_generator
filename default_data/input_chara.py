from proccess import json_to_chara

picture_data = []
profile_data = []
ability_data = []
sanity_point_data = []
magic_point_data = []
durability_data = []
skill_data = []
battle_skill_data = []


def input_chara(data):
    chara = json_to_chara(data)
    global picture_data
    picture_data = [['']]

    global profile_data
    profile_data = [
        ['プロフィール', '', '', ''],
        ['探索者名', chara.name],
        ['職業', chara.profession],
        ['学校・学位', chara.background],
        ['出身', chara.birthplace],
        ['性別', chara.gender, '年齢', chara.age],
    ]

    global ability_data
    ability_data = [
        ['能力値'],
        ['STR', '', chara.strength, 'DEX', '', chara.dexterity, 'INT', '', chara.intelligence],
        ['CON', '', chara.constitution, 'APP', '', chara.appearance, 'POW', '', chara.power],
        ['SIZ', '', chara.size, 'SAN', '', chara.sanity_point, 'EDU', '', chara.education],
        ['アイデア', '', chara.idea, '幸運', '', chara.luck, '知識', '', chara.education],
        ['最大正気度', '', '', chara.max_sanity_point, 'ダメージ・ボーナス', '', '', '', chara.damage_bonus],
    ]

    global sanity_point_data
    sanity_point_data = [
        ['SAN値'],
        * [list(range(20 * i, 20 * (i + 1))) + [''] for i in range(5)],
    ]

    global magic_point_data
    magic_point_data = [
        ['マジック・ポイント'],
        *[list(range(8 * i, 8 * (i + 1))) for i in range(0, 3)],
        ['']
    ]

    global durability_data
    durability_data = [
        ['耐久力'],
        *[list(range(-2 + 9 * i, -2 + 9 * (i + 1))) + [''] for i in range(0, 3)],
        ['']
    ]

    global skill_data
    skill_data = [
        ['探索者の技能'],
        ['探索技能', '', '目星', chara.eye_star, '聞き耳', chara.listen, '図書館', chara.library],
        ['自動車', chara.driving, 'ナビゲート', chara.navigate,
         '鍵開け', chara.picking, '応急手当', chara.first_aid],
        ['機械修理', chara.machine_repair, '電気修理', chara.electrical_repair,
         '写真術', chara.photography, 'オカルト', chara.occult],
        ['クトゥルフ神話', chara.cthulhu_mythos, '', '', '', '', '', ''],
        ['身体技能', '', '回避', chara.avoidance, '跳躍', chara.jumpping, 'サバイバル', chara.survival],
        ['隠す', chara.hide, '隠れる', chara.hidden, '乗馬', chara.horse_riding, '水泳', chara.swimming],
        ['投擲', chara.throwing, '登坂', chara.climbing, '追跡', chara.chase, '変装', chara.disguise],
        ['忍び歩き', chara.sneaking, '', '', '', '', '', ''],
        ['コミュニケーション技能', '', '言いくるめ', chara.deception,
         '説得', chara.persuasion, '信用', chara.trust],
        ['値切り', chara.discount, '母国語', chara.mother_tongue, '精神分析', chara.psychoanalysis, '', ''],
        ['専門技能', '', '医学', chara.medicine, '薬学', chara.pharmacy, '心理学', chara.psychology],
        ['生物学', chara.biology, '化学', chara.chemistry, '物理学', chara.physics, '地質学', chara.geology],
        ['重機械操作', chara.heavy_machine_operation, 'コンピュータ', chara.computer,
         '電子工学', chara.electronics, '博物学', chara.natural_history],
        ['経理', chara.accounting, '法律', chara.law,
         '考古学', chara.archaeology, '人類学', chara.anthropology],
        ['自由技能', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
    ]

    global battle_skill_data
    battle_skill_data = [
        ['戦闘技能'],
        ['キック', chara.kick, '1D6+DB', '拳銃', chara.handgun, 'ライフル', chara.rifle],
        ['組みつき', chara.nelson_hold, '特殊', 'サブマシンガン', chara.submachinegun, '武道', chara.budo],
        ['こぶし', chara.punch, '1D3+DB', 'ショットガン', chara.shotgun, 'マシャルアーツ', chara.martial_arts],
        ['頭突き', chara.heading, '1D4+DB', 'マシンガン', chara.machinegun, '居合', chara.iai],
    ]
