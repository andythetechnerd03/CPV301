import tkinter as tk
import cv2
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import numpy as np
MIN_MATCH_COUNT = 10
meomeo = tk.Tk()
query, train = "query_img.jpg", "train_img.jpg"
query, train,query_g, train_g = cv2.imread(query), cv2.imread(train),cv2.imread(query,0), cv2.imread(train,0)
### def
def upload_query(my_w, img):
    global img1, img_resized1, to1, query
    f_types = [('Jpg Files', '*.jpg'), ('PNG Files','*.png')]
    # img=Image.open(filename)
    ga = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # print(img)
    img1 = Image.fromarray(ga)
    img_resized1=img1.resize((400,400)) # new width & height
    # print(img_resized)
    img1=ImageTk.PhotoImage(img_resized1)
    b2 =tk.Label(my_w,image=img1) # using Button 
    b2.grid(row=3,column=1)
    b2.image = img1 # keep a reference! by attaching it to a widget attribute
    b2['image']=img1 # Show Image  

def upload_train(my_w, img):
    global img2, img_resized2, to2, train
    ga = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # print(img)
    img2 = Image.fromarray(ga)
    img_resized2=img2.resize((400,400)) # new width & height
    # print(img_resized)
    img2=ImageTk.PhotoImage(img_resized2)
    b2 =tk.Label(my_w,image=img2) # using Button 
    b2.grid(row=3,column=2)
    b2.image = img2 # keep a reference! by attaching it to a widget attribute
    b2['image']=img2 # Show Image  


def func1(my_w, to1, to2):
    # Initiate SIFT detector
    sift = cv2.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(to1,None)
    kp2, des2 = sift.detectAndCompute(to2,None)
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1,des2,k=2)
    # store all the good matches as per Lowe's ratio test.
    good = []
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)
    if len(good)>MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()
        h,w = to1.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,M)
        img2 = cv2.polylines(to2,[np.int32(dst)],True,255,3, cv2.LINE_AA)
    else:
        print( "Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT) )
        matchesMask = None
    draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                    singlePointColor = None,
                    matchesMask = matchesMask, # draw only inliers
                    flags = 2)
    img3 = cv2.drawMatches(to1,kp1,to2,kp2,good,None,**draw_params)
    v4 = Image.fromarray(img3)
    v4 = v4.resize((400, 400))
    pic = ImageTk.PhotoImage(v4)
    e2 =tk.Label(my_w, image=pic) # using Button 
    e2.grid(row=4,column=1)
    e2.image = pic # keep a reference! by attaching it to a widget attribute
    e2['image']= pic # Show Image 
    '''# corners = 
    ga = cv2.cvtColor(corners, cv2.COLOR_BGR2RGB)

    v4 = Image.fromarray(ga)
    v4 = v4.resize((400, 400))
    pic = ImageTk.PhotoImage(v4) 
    e2 =tk.Label(my_w, image=pic) # using Button 
    e2.grid(row=4,column=1)
    e2.image = pic # keep a reference! by attaching it to a widget attribute
    e2['image']=pic # Show Image  
    print("meomeo")
    '''

meomeo.geometry("1100x1000")  # Size of the window 
meomeo.title('Workshop 5')
b1 = tk.Button(meomeo, text='Show query image', 
    width=20,command = lambda:upload_query(meomeo, query))
b2 = tk.Button(meomeo, text='Show train image', 
    width=20,command = lambda:upload_train(meomeo, train))
b3 = tk.Button(meomeo, text="Function 1: RANSAC", command=lambda: func1(meomeo, query_g, train_g))






### pack
# base.pack()
# w.pack()
b1.grid(row=2,column=1)
b2.grid(row=2,column=2)
b3.grid(row=2,column=3)


### die
meomeo.mainloop()
