from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from PIL import Image

import datetime
import data

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
  # フォントの大きさを設定
  small_font_size = 8
  middle_font_size = 14
  big_font_size = 22
  # yamlからデータ取得
  person_data = data.get_data()

  photo = Image.open(person_data['photo'])
  pdf_canvas.drawInlineImage(photo.resize((get_size_photo(photo))), 450, 247)

  pdf_canvas.setFont('HeiseiMin-W3', small_font_size)
  pdf_canvas.drawString(105, 309, person_data['name_kana'])
  pdf_canvas.drawString(100, 212, person_data['address_kana'])
  pdf_canvas.drawString(100, 137, person_data['address_kana2'])
  pdf_canvas.drawString(110, 155, person_data['email'])
  pdf_canvas.drawString(458, 155, person_data['twitter'] or '')

  pdf_canvas.setFont('HeiseiMin-W3', middle_font_size)
  today = datetime.date.today()
  pdf_canvas.drawString(289, 334, str(today.year))
  pdf_canvas.drawString(342, 334, str(today.month))
  pdf_canvas.drawString(370, 334, str(today.day))
  birthday = datetime.date(person_data['birthday']['year'], person_data['birthday']['month'], person_data['birthday']['day'])
  pdf_canvas.drawString(119, 242, str(birthday.year))
  pdf_canvas.drawString(172, 242, str(birthday.month))
  pdf_canvas.drawString(210, 242, str(birthday.day))
  pdf_canvas.drawString(271, 242, str(get_age(birthday)))
  if person_data['gender'] == '男':
    pdf_canvas.drawString(356, 237, str("〇"))
  else:
    pdf_canvas.drawString(381, 237, str("〇"))
  pdf_canvas.drawString(100, 189, person_data['address'][0] or '')
  pdf_canvas.drawString(100, 173, person_data['address'][1] or '')
  pdf_canvas.drawString(100, 115, person_data['address2'][0] or '')
  pdf_canvas.drawString(100, 99, person_data['address2'][1] or '')
  pdf_canvas.drawString(438, 189, person_data['tel'])
  pdf_canvas.drawString(438, 114, person_data['tel2'])
  pdf_canvas.drawString(660, 488, person_data['motivation'][0] or '')
  pdf_canvas.drawString(660, 470, person_data['motivation'][1] or '')
  pdf_canvas.drawString(660, 452, person_data['motivation'][2] or '')
  pdf_canvas.drawString(660, 434, person_data['motivation'][3] or '')
  pdf_canvas.drawString(660, 388, person_data['self_pr'][0] or '')
  pdf_canvas.drawString(660, 370, person_data['self_pr'][1] or '')
  pdf_canvas.drawString(660, 352, person_data['self_pr'][2] or '')
  pdf_canvas.drawString(660, 334, person_data['self_pr'][3] or '')
  pdf_canvas.drawString(694, 290, str(person_data['dependents']))
  if person_data['spouse'] == '有':
    pdf_canvas.drawString(772, 288, str("〇"))
  else:
    pdf_canvas.drawString(804, 288, str("〇"))
  if person_data['supporting_spouse'] == '有':
    pdf_canvas.drawString(870, 288, str("〇"))
  else:
    pdf_canvas.drawString(902, 288, str("〇"))
  pdf_canvas.drawString(955, 293, person_data['commuting_time'])
  pdf_canvas.drawString(660, 232, person_data['request'][0] or '')
  pdf_canvas.drawString(660, 214, person_data['request'][1] or '')
  pdf_canvas.drawString(660, 196, person_data['request'][2] or '')
  pdf_canvas.drawString(660, 178, person_data['request'][3] or '')
  pdf_canvas.drawString(660, 160, person_data['request'][4] or '')
  pdf_canvas.drawString(660, 142, person_data['request'][5] or '')
  pdf_canvas.drawString(660, 124, person_data['request'][6] or '')
  pdf_canvas.drawString(660, 106, person_data['request'][7] or '')

  pdf_canvas.setFont('HeiseiMin-W3', big_font_size)
  pdf_canvas.drawString(100, 277, person_data['name'])
  if person_data['is_cellphone']:
    pdf_canvas.drawString(517, 167, str("〇"))
  else:
    pdf_canvas.drawString(498, 167, str("〇"))
  writing_height = 720
  delta_height = 30
  for ed in person_data['education']:
    pdf_canvas.drawString(660, writing_height, str(ed['year']))
    pdf_canvas.drawString(732, writing_height, str(ed['month']))
    pdf_canvas.drawString(765, writing_height, ed['value'])
    writing_height -= delta_height
  for ex in person_data['experience']:
    pdf_canvas.drawString(660, writing_height, str(ex['year']))
    pdf_canvas.drawString(732, writing_height, str(ex['month']))
    pdf_canvas.drawString(765, writing_height, ex['value'])
    writing_height -= delta_height
  pdf_canvas.drawString(850, writing_height, person_data['finish_value'])
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

def get_size_photo(image):
  base_width, base_height = (75, 105)
  ratio_width = image.width / base_width
  ratio_height = image.height / base_height

  if ratio_width < ratio_height:
    return int(image.width // ratio_width), int(image.height // ratio_width)
  else:
    return int(image.width // ratio_height), int(image.height // ratio_height)
