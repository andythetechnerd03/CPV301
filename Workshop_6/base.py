import tkinter as tk
import cv2
from PIL import Image, ImageTk
import os

files = [f for f in os.listdir(os.curdir) if os.path.isfile(f) and f.endswith('.jpg')]  # list comprehension version.
images = []
for file in files: images.append(cv2.imread(file))
meomeo = tk.Tk()


def display_image(window, img, row, column):  # format cv2.imread
    ga = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # print(img)
    img1 = Image.fromarray(ga)
    img_resized1 = img1.resize((400, 400))  # new width & height
    # print(img_resized)
    img1 = ImageTk.PhotoImage(img_resized1)
    label = tk.Label(window, image=img1)  # using Button
    label.grid(row=row, column=column)
    label.image = img1  # keep a reference! by attaching it to a widget attribute
    label['image'] = img1  # Show Image


def show_images(window, imgs):
    for i in range(len(imgs)):
        display_image(window, imgs[i], 3, i + 1)
    # img=Image.open(filename)


def stitch(window, images):
    stitchy = cv2.Stitcher.create()
    (dummy, output) = stitchy.stitch(images)

    if dummy != cv2.STITCHER_OK:
        # checking if the stitching procedure is successful
        # .stitch() function returns a true value if stitching is
        # done successfully
        print("stitching ain't successful")
    else:
        print('Your Panorama is ready!!!')
    display_image(window, output, 4, 1)


meomeo.geometry("1100x1000")  # Size of the window 
meomeo.title('Workshop 6')
b1 = tk.Button(meomeo, text='Show images',
               width=20, command=lambda: show_images(meomeo, images))
b2 = tk.Button(meomeo, text="Function 1: Image stitching", command=lambda: stitch(meomeo, images))

### pack
# base.pack()
# w.pack()
b1.grid(row=2, column=1)
b2.grid(row=2, column=2)

### die
meomeo.mainloop()
