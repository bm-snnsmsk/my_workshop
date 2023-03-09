import cv2
import numpy as np

img = cv2.imread("images/prizma.jpg") 

resize_img = cv2.resize(img, (500,700))
resize_img = cv2.resize(img, None, fx=0.5, fy= 0.5)
resize_img = cv2.resize(img, None, fx=0.5, fy= 0.5, interpolation = cv2.INTER_CUBIC)

##------------------ resim taşıma  START ----------------------##
rows, cols = img.shape[:2]
translation_matrix = np.float32([
    [1, 0, 100], ## 50 sağa - verilirse sola
    [0, 1, 25]  ## 50 aşağıya  - verilirse aşağıya
])
img_translation = cv2.warpAffine(img, translation_matrix, (cols + 50, rows + 50))
##------------------ resim taşıma  END ------------------------##


##------------------ rotation START ----------------------##
rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), 30, 0.7)
img_rotation = cv2.warpAffine(img, rotation_matrix, (int(cols*1.2), int(rows*1.2)))
##------------------ rotation END ------------------------##


##------------------ getAffineTransform START ----------------------##
src_points = np.float32([
    [0,0],
    [cols - 1,0],
    [0,rows - 1]
])
dst_points = np.float32([
    [0,0],
    [int((cols - 1)*0.6),0], # 60% sola
    [int((cols - 1)*0.4),(rows - 1)] # 40% sağa
])
affine_matrix = cv2.getAffineTransform(src_points, dst_points)
img_output = cv2.warpAffine(img, affine_matrix, (cols, rows))
##------------------ getAffineTransform END ------------------------##



##------------------ getPerspectiveTransform START ----------------------##
src_points = np.float32([
    [0,0],
    [cols - 1,0],
    [0,rows - 1],
    [cols - 1,rows - 1]
])
dst_points = np.float32([
    [0,0],
    [cols - 1,0],
    [int(0.33*(cols-1)),rows - 1],
    [int(0.66*(cols-1)),rows - 1]
])
projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
img_output = cv2.warpPerspective(img, projective_matrix, (cols, rows))
##------------------ getPerspectiveTransform END ------------------------##

##------------------ getPerspectiveTransform START ----------------------##
src_points = np.float32([
    [50, 31],
    [210, 31],
    [5, 210],
    [210, 210]
])
dst_points = np.float32([
    [0,0],
    [cols - 1,0],
    [0,rows - 1],
    [cols-1,rows - 1]
]) 
## eğik açıda çekilmiş fotolar kırpılmak istendiğinde sadece odak kısmın kırpılması istendiğinde 
projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
img_output = cv2.warpPerspective(img, projective_matrix, (cols, rows))
##------------------ getPerspectiveTransform END ------------------------##



cv2.imshow("Original", img)  
# cv2.imshow("resize_img", resize_img) 
# cv2.imshow("img_translation", img_translation) 
# cv2.imshow("img_rotation", img_rotation) 
cv2.imshow("img_output", img_output) 

cv2.waitKey(0) 
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


