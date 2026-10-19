
from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

# Lista com os níveis do reservatório
niveis_agua = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]


def definir_cor(nivel):
    """Define a cor da mensagem conforme o nível da água."""
    cores = [
        Fore.RED,
        Fore.YELLOW,
        Fore.GREEN,
        Fore.CYAN,
        Fore.BLUE
    ]

    if 1 <= nivel <= len(cores):
        return cores[nivel - 1]

    return Fore.WHITE


# Simulação dos níveis atuais do reservatório
niveis_simulados = [1, 2, 3, 4, 5]

print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

for nivel in niveis_simulados:
    cor = definir_cor(nivel)
    mensagem = niveis_agua[nivel - 1]

    print(cor + mensagem + Style.RESET_ALL)

print("\nMonitoramento finalizado.")
