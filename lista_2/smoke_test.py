"""
smoke_test.py — Missão 4: Execução Nativa e Evidência Visual
Abre uma janela nativa do OpenCV exibindo uma imagem autoral em tons de cinza.
"""
import cv2
import sys
import os

# Caminho para a imagem autoral (relativo à raiz do repositório)
CAMINHO_IMAGEM = os.path.join(os.path.dirname(__file__),
                              '..', 'lista_1', 'pics', 'IMG_2520.jpg')

img = cv2.imread(CAMINHO_IMAGEM)
if img is None:
    print(f"Erro: imagem não encontrada em {CAMINHO_IMAGEM}")
    sys.exit(1)

img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Teste Nativo — Imagem em Tons de Cinza', img_cinza)
print("Imagem aberta com sucesso! Pressione qualquer tecla para fechar.")
cv2.waitKey(0)
cv2.destroyAllWindows()
