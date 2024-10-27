from ppadb.client import Client as AdbClient
from image_utils import capture_screen
import cv2
import numpy as np

def test_batalha_detection(device):
    # Capture a tela atual
    print("Capturando a tela...")
    screen = capture_screen(device)

    # Carrega a imagem de template (substitua com o nome correto da imagem)
    template_path = "images/batalha/cacada/serpes/iniciar_run.png"  # Ajuste para o caminho correto
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

    # Verifica se a imagem foi carregada corretamente
    if template is None:
        print("Erro ao carregar a imagem 'serpes.png'")
        return

    # Realiza a comparação com threshold ajustado
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.6
    locations = np.where(result >= threshold)

    # Verifica se algum ponto de correspondência foi encontrado
    if len(locations[0]) > 0:
        # Obtém a primeira coordenada
        pt = (locations[1][0], locations[0][0])  # Coordenadas x, y

        # Calcula o ponto central inferior do template para o clique
        click_x = pt[0] + template.shape[1] // 2
        click_y = pt[1] + template.shape[0]  # Clica na parte inferior da imagem

        print(f"Imagem 'serpes.png' encontrada nas coordenadas: {pt}")
        print(f"Clicando na parte inferior da imagem em: ({click_x}, {click_y})")

        # Enviar comando de toque para o dispositivo
        device.shell(f"input tap {click_x} {click_y}")
        print("Clique efetuado com sucesso!")
    else:
        print("Imagem 'serpes.png' não encontrada.")

# Inicialização do cliente ADB e conexão com o emulador
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("emulator-5554")  # Use o ID correto do seu emulador

if device is not None:
    test_batalha_detection(device)
else:
    print("Dispositivo não encontrado. Verifique se o emulador está em execução.")
