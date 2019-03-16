import cv2
import numpy as np

def FiltroGama(img, gamma):
    return (np.power(img*(1/255), 1/gamma))*255

def PlanoBits(img, plano):
    return np.bitwise_and(img, 2**plano)

def Mosaic(img):
    aux_img = np.zeros((512,512))
#    for i in range(4):
#        for j in range(4):
#            aux_img = AuxMosaic(aux_img, img, i*128, j*128, )
    aux_img = AuxMosaic(aux_img, img, 0, 0, 128, 128)
    aux_img = AuxMosaic(aux_img, img, 0, 128, 256, 256)
    aux_img = AuxMosaic(aux_img, img, 0, 256, 383, 0)
    aux_img = AuxMosaic(aux_img, img, 0, 383, 0, 256)
    aux_img = AuxMosaic(aux_img, img, 128, 0, 128, 383)
    aux_img = AuxMosaic(aux_img, img, 128, 128, 383, 383)
    aux_img = AuxMosaic(aux_img, img, 128, 256, 0, 0)
    return aux_img

def AuxMosaic(aux_img, img, x1, y1, x2, y2):
    for i in range(128):
        for j in range(128):
            aux_img[x1 + i][y1 + j] = img[x2 + i][y2 + j]
    return aux_img

def ImageCombine(img1, img2, a1, a2):
    return a1*img1 + a2*img2



img = cv2.imread('img1.png', 0)
imgnew = cv2.imread('butterfly.png', 0)
#img1 = FiltroGama(img, 2.5)
#img2 = PlanoBits(img, 7)
img3 = Mosaic(img)
#img4 = ImageCombine(img, imgnew, 0.5, 0.5)
cv2.imwrite('img3.png', img3)
