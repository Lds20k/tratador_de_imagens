import os
import uuid
import cv2

def converter_imagem(diretorio):
    imagem = cv2.imread('tratar/' + diretorio)
    imagem = tratar_imagem(imagem)
    cv2.imwrite('tratado/' + str(uuid.uuid4()) + '.jpg', imagem)
    os.remove('tratar/' + diretorio)

def tratar_imagem(imagem):

    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_blur = cv2.GaussianBlur(imagem_gray, (5,5), 0)

    sobelxy = cv2.Sobel(src=imagem_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

    return sobelxy

arquivos = next(os.walk('tratar'), (None, None, []))[2]
for imagem in arquivos:
    converter_imagem(imagem)