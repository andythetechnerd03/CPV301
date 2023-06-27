import cv2
import numpy as np
import threading
from scipy.ndimage.interpolation import rotate
drawing = False
ix,iy = -1,-1
k = [0,0,0,0]
rect = None
# define mouse callback function to draw circle
def draw_rectangle(event, x, y, flags, param):
   global ix, iy, drawing, img, k, rect
   if event == cv2.EVENT_LBUTTONDOWN:
        img = np.zeros((512,700, 3), np.uint8)
        img += 255
        drawing = True
        ix = x
        iy = y
   elif event == cv2.EVENT_LBUTTONUP:
      drawing = False
      k = [ix, iy, x, y]
      rect = cv2.rectangle(img, (ix, iy),(x, y),(0, 0, 0),-1)
"""      print(rect)
      print(rect.shape)"""

# Create a black image
img = np.zeros((512,700, 3), np.uint8)
img += 255



# display the window
def display():
    # Create a window and bind the function to window
    cv2.namedWindow("Rectangle Window")

    # Connect the mouse button to our callback function
    cv2.setMouseCallback("Rectangle Window", draw_rectangle)
    while True:
        cv2.imshow("Rectangle Window", img)
        if cv2.waitKey(10) == 27:
            break
    cv2.destroyAllWindows()

def translation(image,x,y):
    global k, img, rect
    k[0] += x
    k[2] += x
    k[1] += y
    k[3] += y
    print(k)
    img = np.zeros((512,700, 3), 3, np.uint8)
    img += 255
    cv2.rectangle(img, (k[0], k[1]),(k[2], k[3]),(0, 0, 0),-1)

def rotation():
    global k, img, rect
    phi = float(input("Goc (degree): ")) * np.pi / 180
    center_x=(k[0]+k[2])/2
    center_y=(k[1]+k[3])/2
    print(k)
    rot_mat = np.array([[np.cos(phi), -np.sin(phi)],[np.sin(phi), np.cos(phi)]])
    rect = rotate(rect, angle=phi)
    '''k[0] = int(center_x + (k[0]-center_x) * np.cos(phi) - (k[1] - center_y) * np.sin(phi))
    k[1] = int(center_y + (k[0]-center_x) * np.sin(phi) + (k[1] - center_y) * np.cos(phi))
    k[2] = int(center_x + (k[2]-center_x) * np.cos(phi) - (k[3] - center_y) * np.sin(phi))
    k[3] = int(center_y + (k[2]-center_x) * np.cos(phi) + (k[3] - center_y) * np.cos(phi))'''
    img = np.zeros((512,700,3), np.uint8)
    img += 255
    '''cv2.rectangle(img, (k[0], k[1]),(k[2], k[3]),(0, 0),-1)'''
    cv2.imshow("Rectangle Window", rect)

def scale():
    global k, img
    s = float(input("He so scale: "))
    center_x=(k[0]+k[2])/2
    center_y=(k[1]+k[3])/2
    k[0] = int((k[0] -center_x) * s + center_x)
    k[2] = int((k[2] -center_x) * s + center_x)
    k[1] = int((k[1] -center_y) * s + center_y)
    k[3] = int((k[3] -center_y) * s + center_y)
    print(k)
    img = np.zeros((512,700,3), np.uint8)
    img += 255
    cv2.rectangle(img, (k[0], k[1]),(k[2], k[3]),(0, 0),-1)



if __name__ == "__main__":
    a = threading.Thread(target=display)
    while True:
        print("Welcome!")
        print("1: Create rectangle")
        print("2: Translation")
        print("3: Rotation")
        print("4: Scale")
        print("5: Exit")
        opt = input("Option: ")
        if opt == '1':
            a.start()
        if opt == '2':
            vecx= int(input("Input x: "))
            vecy = int(input("Input y: "))
            translation(img, vecx, vecy)
        if opt == '3':
            rotation()
        if opt == '4':
            scale()
        if opt == "5":
            exit()

