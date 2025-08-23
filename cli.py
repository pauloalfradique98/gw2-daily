import json
import os

# Nome do arquivo onde vamos salvar o progresso
SAVE_FILE = "progress.json"

# Rotinas que você definiu
routines = [
    "Login Reward",
    "Craft Ectos",
    "Farm Daily",
    "Fractal Daily",
    "Gathering Daily",
    "Wizard Vault Daily"
]

# Função para carregar progresso salvo
def load_progress():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    else:
        # Se não existir arquivo, começa tudo como não feito
        return {routine: False for routine in routines}

# Função para salvar progresso
def save_progress(progress):
    with open(SAVE_FILE, "w") as f:
        json.dump(progress, f, indent=4)

# Inicializa progresso
progress = load_progress()

# Função para mostrar checklist
def show_routines():
    print("\n===== Daily Routine Tracker =====")
    for i, routine in enumerate(routines, 1):
        status = "[x]" if progress[routine] else "[ ]"
        print(f"{i}. {status} {routine}")
    print("0. Sair")

# Função principal
def main():
    while True:
        show_routines()
        choice = input("\nEscolha uma rotina para alternar (0 para sair): ")

        if choice == "0":
            print("Saindo... Progresso salvo!")
            save_progress(progress)
            break

        if choice.isdigit() and 1 <= int(choice) <= len(routines):
            routine = routines[int(choice) - 1]
            # Alterna True <-> False
            progress[routine] = not progress[routine]
            save_progress(progress)  # Salva automaticamente
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
