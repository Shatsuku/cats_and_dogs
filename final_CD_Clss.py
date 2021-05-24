import tkinter as tk
from tkinter import filedialog
from tkinter import *


from PIL import ImageTk, Image
import numpy as np

import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model("h5.h5")



ans = { 
    0:'its a CAT!',
    1:'its a DOG!',
}

top = Tk()
top.title("Cats vs Dogs Classification")
top.geometry('800x600')
top.configure(background="#0091e3")
label=Label(top,background='#0091e3', font=('arial',15,'bold'), pady=0)

sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((150,150))
    image = np.expand_dims(image,axis=0)
    image = np.array(image)
    image= image/255.
    pred = model.predict_classes([image])[0]
    sign = ans[pred]
    print(sign)
    label.configure(foreground='white', text=sign) 

def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",
    command=lambda: classify(file_path),
    padx=10,pady=5)
    classify_b.configure(background='#ff8000', foreground='white',
    font=('arial',10,'bold'))
    # classify_b.place(x=600, y=300)
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),
                            (top.winfo_height()/2.25)))
        # uploaded.thumbnail(((300),
        #                     (250)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        # sign_image.place(x=300, y=200)
        # sign_image.place(relx=0.35, rely=0.35)
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#ff8000', foreground='white',font=('arial',10,'bold'))

upload.place(relx=0.79, rely=0.55)
# upload.place(x=600, y=350)
# upload.pack(side=BOTTOM,pady=50)


sign_image.pack(side=BOTTOM,expand=True)
# sign_image.pack()
heading = Label(top, text="Cats VS Dogs Classification",pady=20, font=('arial',20,'bold'))
heading.configure(background='#0091e3',foreground='white')
heading.pack()
label.pack()
# label.pack(side=TOP,expand=True)
# fill = Label(top)
# fill.pack(side=BOTTOM)


top.mainloop()