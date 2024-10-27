from ppadb.client import Client as AdbClient
from PIL import Image
import numpy as np
import cv2

def capture_screen(device):
    """Captura a tela do dispositivo e retorna a imagem em escala de cinza."""
    screenshot = device.screencap()
    screen = cv2.imdecode(np.frombuffer(screenshot, np.uint8), cv2.IMREAD_GRAYSCALE)
    return screen

def compare_images(screen, template_path, device, threshold=0.7, click_on_found=False, click_position="center"):
    """Compara a imagem da tela com o template e, opcionalmente, clica em uma posição específica se encontrar uma correspondência."""
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

    if template is None:
        print(f"Erro ao carregar a imagem do template: {template_path}")
        return False

    if len(screen.shape) == 3:  # Se for colorida
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)

    if len(locations[0]) > 0:
        pt = (locations[1][0], locations[0][0])  # Posição do primeiro match encontrado

        if click_on_found:
            # Cálculo das coordenadas do clique com base na posição desejada
            if click_position == "center":
                click_x = pt[0] + template.shape[1] // 2
                click_y = pt[1] + template.shape[0] // 2
            elif click_position == "bottom_center":
                click_x = pt[0] + template.shape[1] // 2
                click_y = pt[1] + template.shape[0] - 10  # Ajusta para 10px acima da borda inferior

            device.shell(f"input tap {click_x} {click_y}")
            print(f"Clique realizado na posição ({click_x}, {click_y}) - {click_position}")

        return True
    else:
        print("Imagem não encontrada.")
        return False
