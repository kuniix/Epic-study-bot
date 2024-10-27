from ppadb.client import Client as AdbClient

def verify_game():
    """Verifica se o jogo Epic Seven está em execução."""
    client = AdbClient(host="127.0.0.1", port=5037)
    
    # Conecta ao emulador usando o ID correto
    device = client.device("emulator-5554")
    
    if device is None:
        print("Erro: Dispositivo não encontrado ou emulador não está conectado.")
        return False

    try:
        # Primeira tentativa: verificar o processo usando `pidof`
        output_pidof = device.shell("pidof com.stove.epic7.google")
        if output_pidof.strip():
            return True  # Processo encontrado com `pidof`
        
        # Segunda tentativa: verificar o processo usando `dumpsys`
        output_dumpsys = device.shell("dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'")
        if "com.stove.epic7.google" in output_dumpsys:
            return True  # Processo encontrado com `dumpsys`

        # Terceira tentativa: verificar pacotes em execução
        output_ps = device.shell("ps | grep com.stove.epic7.google")
        if "com.stove.epic7.google" in output_ps:
            return True  # Processo encontrado com `ps`

        return False  # Processo não encontrado em nenhuma verificação

    except Exception as e:
        print(f"Erro ao verificar o estado do jogo: {e}")
        return False
