import cv2


img = cv2.imread('imgBordas.png')
cv2.imshow('Img : ',img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Imag : ',img)
frame = cv2.Canny(img,30,90,3)
cv2.imshow('Imagem : ',frame)
cv2.waitKey(0)
