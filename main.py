import PIL
from PIL import Image
from tkinter.filedialog import *

file_path = askopenfilename()
img = Image.open(file_path)

myH, myW = img.size

img = img.resize((myH,myW), Image.LANCZOS)

save_path = asksaveasfilename()

img.save(save_path + '_compressed.jpg')