#__author: xlu.com
#date : 2018/8/10
import  pytesseract
from PIL import Image

# res = pytesseract.image_to_string(Image.open('1.jpg'),lang='chi_sim')
# res = pytesseract.image_to_string(Image.open('5.png'))
# pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
res = pytesseract.image_to_string(Image.open('4.jpg'),lang='chi_sim')
print(res)