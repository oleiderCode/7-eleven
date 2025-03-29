import winreg

# Clave del registro donde se almacenará el contador
registry_key = r"SOFTWARE\GioTickets"

def make_registry_key():
    try:
        # Intentar abrir la clave del registro
        reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_key, 0, winreg.KEY_READ | winreg.KEY_WRITE)
        ejecuciones, _ = winreg.QueryValueEx(reg, "TrialRuns")
        winreg.CloseKey(reg)
    except FileNotFoundError:
        # Si la clave no existe, crearla y establecer en 0
        reg = winreg.CreateKey(winreg.HKEY_CURRENT_USER, registry_key)
        winreg.SetValueEx(reg, "TrialRuns", 0, winreg.REG_DWORD, 0)
        ejecuciones = 0
        winreg.CloseKey(reg)

    # Verificar si alcanzó el límite
    if ejecuciones >= 45:
        return({
        "ejecuciones": ejecuciones, 
        # "limite": > 100,
        "limite": ejecuciones >= 45,
        })
        exit()

    # Aumentar y guardar el contador en el registro
    ejecuciones += 1
    # ejecuciones = 97
    reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_key, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(reg, "TrialRuns", 0, winreg.REG_DWORD, ejecuciones)
    winreg.CloseKey(reg)

    return({
        "ejecuciones": ejecuciones, 
        # "limite": > 100,
        "limite": ejecuciones >= 45,
        })
