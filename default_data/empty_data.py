picture_data = [['']]

profile_data = [
    ['プロフィール', '', '', ''],
    ['探索者名'],
    ['職業'],
    ['学校・学位'],
    ['出身'],
    ['性別', '', '年齢', ''],
]

ability_data = [
    ['能力値'],
    ['STR', '', '12', 'DEX', '', '', 'INT', '', ''],
    ['CON', '', '', 'APP', '', '', 'POW', '', ''],
    ['SIZ', '', '', 'SAN', '', '', 'EDU', '', ''],
    ['アイデア', '', '', '幸運', '', '', '知識', '', '100'],
    ['最大正気度', '', '', '', 'ダメージ・ボーナス', '', '', '', '1D6'],
]

sanity_point_data = [
    ['SAN値'],
    * [list(range(20 * i, 20 * (i + 1))) + [''] for i in range(5)],
]

magic_point_data = [
    ['マジック・ポイント'],
    *[list(range(8 * i, 8 * (i + 1))) for i in range(0, 3)],
    ['']
]

durability_data = [
    ['耐久力'],
    *[list(range(-2 + 9 * i, -2 + 9 * (i + 1))) + [''] for i in range(0, 3)],
    ['']
]

skill_data = [
    ['探索者の技能'],
    ['探索技能', '', '目星', '100', '聞き耳', '', '図書館', ''],
    ['自動車', '10', 'ナビゲート', '', '鍵開け', '', '応急手当', ''],
    ['機械修理', '', '電気修理', '', '写真術', '', 'オカルト', ''],
    ['クトゥルフ神話', '', '', '', '', '', '', ''],
    ['身体技能', '', '回避', '', '跳躍', '', 'サバイバル', ''],
    ['隠す', '', '隠れる', '', '乗馬', '', '水泳', ''],
    ['投擲', '', '登坂', '', '追跡', '', '変装', ''],
    ['忍び歩き', '', '追跡', '', '', '', '', ''],
    ['コミュニケーション技能', '', '言いくるめ', '', '説得', '', '信用', ''],
    ['値切り', '', '母国語', '', '精神分析', '', '', ''],
    ['専門技能', '', '医学', '', '薬学', '', '心理学', ''],
    ['生物学', '', '化学', '', '物理学', '', '地質学', ''],
    ['重機械操作', '', 'コンピュータ', '', '電子工学', '', '博物学', ''],
    ['経理', '', '法律', '', '考古学', '', '人類学', ''],
    ['自由技能', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
]

battle_skill_data = [
    ['戦闘技能'],
    ['キック', '', '1D6+DB', '拳銃', '', 'ライフル', ''],
    ['組みつき', '', '特殊', 'サブマシンガン', '', '武道', ''],
    ['こぶし', '', '1D3+DB', 'ショットガン', '', 'マシャルアーツ', ''],
    ['頭突き', '', '1D4+DB', 'マシンガン', '', '居合', ''],
]
