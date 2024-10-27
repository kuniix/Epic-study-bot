from verify_game import verify_game
from ppadb.client import Client as AdbClient
from image_utils import capture_screen, compare_images
from action_utils import unlock_screen, wait,click_screen

def main_menu():
    """Exibe o menu principal."""
    print("\n=== Menu Principal ===")
    print("Digite 1 para verificar se o jogo está aberto")
    print("Digite 0 para sair do programa")

def action_menu():
    """Exibe o menu de ações."""    
    print("\n=== Menu de Ações ===")
    print("Digite 1 para iniciar a ação 'caçada'")
    print("Digite 0 para voltar ao menu principal")

if __name__ == "__main__":
    client = AdbClient(host="127.0.0.1", port=5037)
    device = client.device("emulator-5554")  # Use o ID correto do seu emulador

    while True:
        main_menu()
        choice = input("Escolha uma opção: ")

        if choice == "0":
            print("Fechando o programa.")
            break

        elif choice == "1":
            if verify_game():
                print("Sim, o jogo está aberto.")
                
                while True:
                    action_menu()
                    action_choice = input("Escolha uma ação: ")
                    
                    if action_choice == "0":
                        print("Voltando ao menu principal.")
                        break

                    elif action_choice == "1":
                        click_screen(device, 300, 300)
                        print("Iniciando a ação 'caçada'...")
                        screen = capture_screen(device)
                        wait()
                        
                        # Verifica a presença de `menu_inicial.png` e clica se encontrado
                        if compare_images(screen, "images/menu_inicial.png", device, threshold=0.6, click_on_found=True, click_position="center"):
                            wait()
                            screen = capture_screen(device)

                            #clica no batalha.
                            click_screen(device, 1100, 600)
                            wait()
                            screen = capture_screen(device)
                            #verificar a imagem caçada
                            if (compare_images(screen,"images/batalha/cacada/cacada.png",device, threshold=0.5, click_on_found=True, click_position="center")):
                                print("A imagem de caçada foi encontrada")
                                wait()
                                screen = capture_screen(device)

                                #verifica imagem do serpes
                                if(compare_images(screen,"images/batalha/cacada/serpes/serpes.png", device, threshold=0.4, click_on_found=True, click_position="center")):
                                    print("A imagem de serpes foi encontrada e selecionada")
                                    wait()
                                    
                                    click_screen(device, 1100, 700)
                                    wait()
                                    
                                    click_screen(device, 1040, 651)
                                    
                                    
                                else:
                                    print("Imagem do serpes não foi localizada")
                                
                            else:
                                print("Imagem caçada não foi encontrada")
                        else:
                            print("Imagem do menu inicial não encontrada.")
                    else:
                        print("Opção inválida. Tente novamente.")
            else:
                print("Não, o jogo NÃO está aberto.")
