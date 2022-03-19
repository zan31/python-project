from PIL import Image
import re
import cv2
import pytesseract
from matplotlib import pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pic = 'tvoja-dijaska.jpg'

slika = cv2.imread(pic)
slika = cv2.cvtColor(slika, cv2.COLOR_BGR2RGB)

dimensions = slika.shape
height = slika.shape[0]
cropy = height / 2.5
cropy1 = height - height / 4
cropped = slika[int(cropy):int(cropy1)]

cv2.imwrite("Cropped_" + pic, cropped)
crop = cv2.imread("Cropped_" + pic)

text = pytesseract.image_to_string(crop, lang="slv")
pattern = r'[^A-Ž0-9 ]+'
text = re.sub(pattern, '', text)
remove_lower = lambda text: re.sub('[a-z]', '', text)
text = remove_lower(text)
print(text)

im = Image.open(pic)
x = 30
y = 360

pix = im.load()
rgb = pix[x, y]
if (rgb[2] > rgb[1]) and (rgb[2] > rgb[0]):
    print("ERŠ")
if (rgb[2] == rgb[1]) and (rgb[2] > rgb[0]):
    print("ERŠ")
if (rgb[2] < rgb[1]) or (rgb[2] < rgb[0]):
    print("ni ERŠ")