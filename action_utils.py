from ppadb.client import Client as AdbClient
from verify_game import verify_game
import time

verify_game()
def unlock_screen(device):
    device.shell(f"input tap {300} {300}")
    time.sleep(1)  # Espera um pouco para permitir que a tela responda
    
def click_screen(device, x,y):
    device.shell(f"input tap {x} {y}")
    
def wait():
    time.sleep(3)