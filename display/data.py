from utils.proccess import json_to_chara


class Data:
    def __init__(self, data):
        self.chara = json_to_chara(data)
        self.picture = [['']]
        self.profile = [
            ['プロフィール', '', '', ''],
            ['探索者名', self.chara.name],
            ['職業', self.chara.profession],
            ['学校・学位', self.chara.background],
            ['出身', self.chara.birthplace],
            ['性別', self.chara.gender, '年齢', self.chara.age],
        ]
        self.ability = [
            ['能力値'],
            ['STR', '', self.chara.strength, 'DEX', '', self.chara.dexterity,
             'INT', '', self.chara.intelligence],
            ['CON', '', self.chara.constitution, 'APP', '', self.chara.appearance,
             'POW', '', self.chara.power],
            ['SIZ', '', self.chara.size, 'SAN', '', self.chara.sanity_point,
             'EDU', '', self.chara.education],
            ['アイデア', '', self.chara.idea, '幸運', '', self.chara.luck, '知識',
             '', self.chara.education],
            ['最大正気度', '', '', self.chara.max_sanity_point,
             'ダメージ・ボーナス', '', '', '', self.chara.damage_bonus],
        ]
        self.sanity_point = [
            ['SAN値'],
            * [list(range(20 * i, 20 * (i + 1))) + [''] for i in range(5)],
        ]
        self.magic_point = [
            ['マジック・ポイント'],
            *[list(range(8 * i, 8 * (i + 1))) for i in range(0, 3)],
            ['']
        ]
        self.durability = [
            ['耐久力'],
            *[list(range(-2 + 9 * i, -2 + 9 * (i + 1))) + [''] for i in range(0, 3)],
            ['']
        ]
        self.skill = [
            ['探索者の技能'],
            ['探索技能', '', '目星', self.chara.eye_star,
             '聞き耳', self.chara.listen, '図書館', self.chara.library],
            ['自動車', self.chara.driving, 'ナビゲート', self.chara.navigate,
             '鍵開け', self.chara.picking, '応急手当', self.chara.first_aid],
            ['機械修理', self.chara.machine_repair, '電気修理', self.chara.electrical_repair,
             '写真術', self.chara.photography, 'オカルト', self.chara.occult],
            ['クトゥルフ神話', self.chara.cthulhu_mythos, '', '', '', '', '', ''],
            ['身体技能', '', '回避', self.chara.avoidance,
             '跳躍', self.chara.jumpping, 'サバイバル', self.chara.survival],
            ['隠す', self.chara.hide, '隠れる', self.chara.hidden, '乗馬', self.chara.horse_riding,
             '水泳', self.chara.swimming],
            ['投擲', self.chara.throwing, '登坂', self.chara.climbing, '追跡', self.chara.chase,
             '変装', self.chara.disguise],
            ['忍び歩き', self.chara.sneaking, '', '', '', '', '', ''],
            ['コミュニケーション技能', '', '言いくるめ', self.chara.deception,
             '説得', self.chara.persuasion, '信用', self.chara.trust],
            ['値切り', self.chara.discount, '母国語', self.chara.mother_tongue,
             '精神分析', self.chara.psychoanalysis, '', ''],
            ['専門技能', '', '医学', self.chara.medicine, '薬学', self.chara.pharmacy,
             '心理学', self.chara.psychology],
            ['生物学', self.chara.biology, '化学', self.chara.chemistry,
             '物理学', self.chara.physics, '地質学', self.chara.geology],
            ['重機械操作', self.chara.heavy_machine_operation, 'コンピュータ', self.chara.computer,
             '電子工学', self.chara.electronics, '博物学', self.chara.natural_history],
            ['経理', self.chara.accounting, '法律', self.chara.law,
             '考古学', self.chara.archaeology, '人類学', self.chara.anthropology],
            ['自由技能', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
        ]
        self.battle_skill = [
            ['戦闘技能'],
            ['キック', self.chara.kick, '1D6+DB', '拳銃', self.chara.handgun, 'ライフル', self.chara.rifle],
            ['組みつき', self.chara.nelson_hold, '特殊', 'サブマシンガン', self.chara.submachinegun,
             '武道', self.chara.budo],
            ['こぶし', self.chara.punch, '1D3+DB', 'ショットガン', self.chara.shotgun,
             'マシャルアーツ', self.chara.martial_arts],
            ['頭突き', self.chara.heading, '1D4+DB', 'マシンガン', self.chara.machinegun,
             '居合', self.chara.iai],
        ]
