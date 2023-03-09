import cv2
import numpy as np

img = cv2.imread("images/prizma.jpg") 
img = cv2.imread("images/kitap.png") 
img = cv2.imread("images/kitap2.png") 
img = cv2.imread("images/kitap3.png") 
img = cv2.imread("images/kitap4.png") 

rows, cols = img.shape[:2]
click_count = 0
a = []
dst_points = np.float32([[0,0],[cols-1,0],[0,rows-1],[cols-1,rows-1]])
cv2.namedWindow("img", cv2.WINDOW_NORMAL)
def draw(event, x, y, flags, param):
    print(x,y)
    global click_count, a
    if click_count < 4 :
        if event == cv2.EVENT_LBUTTONDBLCLK :
            click_count += 1
            a.append((x, y))
    else :        
        src_points = np.float32([
            [a[0][0], a[0][1]], ## sol-üst
            [a[1][0], a[1][1]], ## sağ-üst
            [a[2][0], a[2][1]], ## sol-alt
            [a[3][0], a[3][1]]  ## sağ-alt
        ])         
        click_count = 0
        a = []
        projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        img_output = cv2.warpPerspective(img, projective_matrix, (cols, rows))
        cv2.imshow("img_output", img_output)
        
         
 
cv2.setMouseCallback("img", draw)
while True :
    cv2.imshow("img", img) 
    if cv2.waitKey(1) == ord('q') :
        break


cv2.destroyAllWindows() 


