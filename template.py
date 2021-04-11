from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.pagesizes import A4, landscape

import datetime

def make(filename = "template"):
  pdf_canvas = set_info(filename)
  print_string(pdf_canvas)
  pdf_canvas.save()

def set_info(filename):
  pdf_canvas = canvas.Canvas("./{0}.pdf".format(filename), pagesize=(1190, 841))
  pdf_canvas.setAuthor("Luna Chevalier")
  pdf_canvas.setTitle("resume")
  pdf_canvas.setSubject("")
  return pdf_canvas

def print_string(pdf_canvas):
  pdfmetrics.registerFont(UnicodeCIDFont("HeiseiMin-W3"))
  small_font_size = 8
  middle_font_size = 14
  big_font_size = 22

  pdf_canvas.setFont('HeiseiMin-W3', small_font_size)
  pdf_canvas.drawString(105, 309, "る        な                  ち      ぇ        ば       り       ー")
  pdf_canvas.drawString(100, 212, "現住所ふりがな")
  pdf_canvas.drawString(110, 155, "luna.chevalier@example.com")
  pdf_canvas.drawString(458, 155, "Luna_Chevalier")

  pdf_canvas.setFont('HeiseiMin-W3', middle_font_size)
  today = datetime.date.today()
  pdf_canvas.drawString(289, 334, str(today.year))
  pdf_canvas.drawString(342, 334, str(today.month))
  pdf_canvas.drawString(370, 334, str(today.day))
  birthday = datetime.date(2000, 4, 17)
  pdf_canvas.drawString(119, 242, str(birthday.year))
  pdf_canvas.drawString(172, 242, str(birthday.month))
  pdf_canvas.drawString(210, 242, str(birthday.day))
  pdf_canvas.drawString(271, 242, str(get_age(datetime.date(2000, 4, 17))))
  pdf_canvas.drawString(356, 237, str("〇"))
  pdf_canvas.drawString(100, 189, "〇〇県××市△△区□□1-1-1萌ビル")
  pdf_canvas.drawString(100, 173 , "120階 19号")
  pdf_canvas.drawString(438, 189, "090-1234-5678")
  pdf_canvas.drawString(660, 488, "ラブライバーだからです。")
  pdf_canvas.drawString(660, 470, "やりたいからです。")
  pdf_canvas.drawString(660, 452, "ネタが尽きました。")
  pdf_canvas.drawString(660, 434, "これが最後ですw。")
  pdf_canvas.drawString(660, 388, "にっこにっこにー")
  pdf_canvas.drawString(660, 370, "あなたのハートににこにこにー")
  pdf_canvas.drawString(660, 352, "笑顔届ける矢澤にこにこー")
  pdf_canvas.drawString(660, 334, "にこにーって覚えてラブにこ")
  pdf_canvas.drawString(804, 288, str("〇"))
  pdf_canvas.drawString(902, 288, str("〇"))
  pdf_canvas.drawString(955, 293, str("徒歩10分"))
  pdf_canvas.drawString(660, 232, "この履歴書に使われているフォントの名前を教えて下さい。")
  pdf_canvas.drawString(660, 214, "リモートワークを見越して自宅環境整えたのに、")
  pdf_canvas.drawString(660, 196, "リモートワークをしたことがありませんw")
  pdf_canvas.drawString(660, 160, "エブリデイ♪")
  pdf_canvas.drawString(660, 142, "ヤングライフ♪")
  pdf_canvas.drawString(660, 124, "ジュネス♪")
  pdf_canvas.drawString(660, 106, "↑書いていたときにBGMで流れてきました")

  pdf_canvas.setFont('HeiseiMin-W3', big_font_size)
  pdf_canvas.drawString(100, 277, "ルナ・チェバリー")
  pdf_canvas.drawString(660, 720, "1990")
  pdf_canvas.drawString(732, 720, "3")
  pdf_canvas.drawString(765, 720, "音ノ木坂学院 卒業")
  pdf_canvas.drawString(660, 690, "1990")
  pdf_canvas.drawString(732, 690, "4")
  pdf_canvas.drawString(765, 690, "浦の星女学院 入学")
  pdf_canvas.drawString(660, 660, "1993")
  pdf_canvas.drawString(732, 660, "3")
  pdf_canvas.drawString(765, 660, "浦の星女学院 卒業")
  pdf_canvas.drawString(660, 630, "1993")
  pdf_canvas.drawString(732, 630, "4")
  pdf_canvas.drawString(765, 630, "虹ヶ咲学園 赴任")
  pdf_canvas.drawString(850, 600, "以上")
  pdf_canvas.showPage()

def get_age(birthday=datetime.date.today):
  today = datetime.date.today()
  age = today.year - birthday.year
  if today.month < birthday.month:
    age -= 1
  elif today.month == birthday.month:
    if today.day <= birthday.day:
      age -= 1
  return age
