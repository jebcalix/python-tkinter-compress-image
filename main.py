from PIL import Image
from tkinter.filedialog import *
from tkinter import Tk, Button

class Compress:
	def __init__(self, master):
		master.title("Compresor de Imagenes")
		master.geometry("400x400+400+400")
		master.config(bg='gray')
		master.resizable(False, False)
		Button(width=3, height=1,font=('Arial Bold', 18), text='Abrir', relief='groove', bg='white',command=self.comprimir).place(x=175, y=175)
	def comprimir(self):
		file_path = askopenfilename(filetypes=[('Images', '.jpg .jpeg')])
		img = Image.open(file_path)

		myH, myW = img.size

		img = img.resize((myH,myW), Image.ANTIALIAS)

		save_path = asksaveasfilename(filetypes=[('Images', '.jpg .jpeg')])

		img.save(save_path + '_compressed.jpg', optimize=True, quality=70)

root = Tk()
compress=Compress(root)
root.mainloop()