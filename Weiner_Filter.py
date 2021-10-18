from tkinter import*
from PIL import ImageTk,Image
from tkinter import filedialog


root = Tk()
root.title('Belajar Tkinter')



def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/gui/images", title="Select A File", filetypes=(("jpg file", " *.jpg"),("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_imange_label = Label(image=my_image).pack()

my_btn = Button(root, text="Buka File",command=open).pack()


root.mainloop()