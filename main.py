import json
import reportlab
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4
# from PIL import Image
from display.create_table import CreateTable
import io


def make(data_dict, filename="charasheet"):  # ファイル名の設定
    # pdf_canvas = canvas.Canvas("./{0}.pdf".format(filename))  # キャンバス名の設定
    buffer = io.BytesIO()
    pdf_canvas = canvas.Canvas(buffer)  # キャンバス名の設定
    print_string(pdf_canvas, data_dict)
    pdf_canvas.save()  # pdfを保存
    return buffer


def print_string(pdf_canvas, data_dict):
    # font
    reportlab.rl_config.TTFSearchPath.append('./fonts')
    pdfmetrics.registerFont(TTFont('GenShinGothic', 'GenShinGothic-P-Normal.ttf'))
    # pdf size
    width, height = A4

    # im = Image.open('./images/thumbnail_django.jpg')
    # im_resize = im.resize((195, 192))
    # pdf_canvas.drawInlineImage(im_resize, 10 * mm, 219 * mm)
    CreateTable('picture', data_dict, pdf_canvas)
    CreateTable('profile', data_dict, pdf_canvas)
    CreateTable('ability', data_dict, pdf_canvas)
    CreateTable('sanity_point', data_dict, pdf_canvas)
    CreateTable('magic_point', data_dict, pdf_canvas)
    CreateTable('durability', data_dict, pdf_canvas)
    CreateTable('skill', data_dict, pdf_canvas)
    CreateTable('battle_skill', data_dict, pdf_canvas)


if __name__ == '__main__':
    with open('chara.json') as f:
        json_dict = json.load(f)
    make(json_dict)
