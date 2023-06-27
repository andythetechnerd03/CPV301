import tkinter as tk
import cv2
from ffff import *
from harris_corner_detector import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from meomeeoeoe import *

meomeo = tk.Tk()
### def
def upload_file(my_w):
    global img, img_resized, to
    f_types = [('Jpg Files', '*.jpg'), ('PNG Files','*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    print(filename)
    # img=Image.open(filename)
    to = cv2.imread(filename)
    ga = cv2.cvtColor(to, cv2.COLOR_BGR2RGB)
    # print(img)
    img = Image.fromarray(ga)
    img_resized=img.resize((400,400)) # new width & height
    # print(img_resized)
    img=ImageTk.PhotoImage(img_resized)
    b2 =tk.Label(my_w,image=img) # using Button 
    b2.grid(row=3,column=1)
    b2.image = img # keep a reference! by attaching it to a widget attribute
    b2['image']=img # Show Image  

def func1(my_w):
    global img, to
    corners,g_dx2,g_dy2,dx,dy,loc = harris(to,0.85)
    
    # corners = 
    ga = cv2.cvtColor(corners, cv2.COLOR_BGR2RGB)

    v4 = Image.fromarray(ga)
    v4 = v4.resize((400, 400))
    pic = ImageTk.PhotoImage(v4) 
    e2 =tk.Label(my_w, image=pic) # using Button 
    e2.grid(row=4,column=1)
    e2.image = pic # keep a reference! by attaching it to a widget attribute
    e2['image']=pic # Show Image  
    print("meomeo")

def func2(my_w):
    global to
    ga = meomeoemoe(to)
    cv2.imshow("dd", ga)
    v4 = Image.fromarray(ga)
    v4 = v4.resize((400, 400))
    pic = ImageTk.PhotoImage(v4) 
    e2 =tk.Label(my_w, image=pic) # using Button 
    e2.grid(row=4,column=1)
    e2.image = pic # keep a reference! by attaching it to a widget attribute
    e2['image']=pic # Show Image  
    print("meo")

def func3(my_w):
    global to
    gray = cv2.cvtColor(to,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    v4 = Image.fromarray(edges)
    v4 = v4.resize((400, 400))
    pic = ImageTk.PhotoImage(v4) 
    e2 =tk.Label(my_w, image=pic) # using Button 
    e2.grid(row=4,column=1)
    e2.image = pic # keep a reference! by attaching it to a widget attribute
    e2['image']=pic# Show Image  
    print("meo")

def func4(my_w):
    global to
    # img = cv2.imread('image_1.jpg')
    ga = cv2.cvtColor(to, cv2.COLOR_BGR2RGB)
    # gray = cv2.cvtColor(to,cv2.COLOR_BGR2GRAY)
    # edges = cv2.Canny(gray,50,150,apertureSize = 3)
    # minLineLength = 100
    # maxLineGap = 10
    # lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
    # for x1,y1,x2,y2 in lines[0]:
    #     cv2.line(to,(x1,y1),(x2,y2),(0,255,0),2)



    gray = cv2.cvtColor(to,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)

    lines = cv2.HoughLines(edges,1,np.pi/180,200)
    # ga = cv2.resize(ga, (400, 400))
    for rho,theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(ga,(x1,y1),(x2,y2),(0,0,255),2)
    # cv2.imshow("cc", to)
    # cv2.imshow("ddd")
    v4 = Image.fromarray(ga)
    v4 = v4.resize((400, 400))
    pic = ImageTk.PhotoImage(v4) 
    e2 =tk.Label(my_w, image=pic) # using Button 
    e2.grid(row=4,column=1)
    e2.image = pic
    e2['image']=pic  
    print("meo")
### component
# base = tk.Canvas(height=500, width=500, background="yellow")
# w = tk.Scale(meomeo, from_=0, to=200, orient="horizontal")

meomeo.geometry("1100x1000")  # Size of the window 
meomeo.title('LAB3')
b1 = tk.Button(meomeo, text='Upload File', 
    width=20,command = lambda:upload_file(meomeo))
b2 = tk.Button(meomeo, text="Function 1", command=lambda: func1(meomeo))
b3 = tk.Button(meomeo, text="Function 2", command=lambda: func2(meomeo))
b4 = tk.Button(meomeo, text="Function 3",command=lambda: func3(meomeo))
b5 = tk.Button(meomeo, text="Function 4", command=lambda: func4(meomeo))





### pack
# base.pack()
# w.pack()
b1.grid(row=2,column=1)
b2.grid(row=2,column=2)
b3.grid(row=2,column=3)
b4.grid(row=2,column=4)
b5.grid(row=2,column=5)





### die
meomeo.mainloop()
