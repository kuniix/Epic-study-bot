import cv2
import os

# Diretório onde suas imagens estão armazenadas
directory = 'images/batalha/'

# Loop através de todos os arquivos no diretório
for filename in os.listdir(directory):
    if filename.endswith('.png'):  # Verifique se é um arquivo PNG
        # Caminho completo do arquivo
        img_path = os.path.join(directory, filename)
        
        # Carrega a imagem
        img = cv2.imread(img_path)
        
        # Converte a imagem para escala de cinza
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Salva a imagem em escala de cinza
        gray_img_path = os.path.join(directory, 'gray_' + filename)  # Prefixo 'gray_' para indicar que é cinza
        cv2.imwrite(gray_img_path, gray_img)

        print(f'Imagem {filename} convertida e salva como {gray_img_path}')
