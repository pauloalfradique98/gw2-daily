import os
from routines import load_tasks, load_progress, save_progress, toggle_task
from utils import color_text, Colors

def display_menu(tasks: dict, progress: dict) -> None:
    os.system("cls" if os.name == "nt" else "clear")
    print(color_text("=-=-=-= Daily Routine Tracker =-=-=-=\n", Colors.CYAN))
    
    for task_id, task_name in tasks.items():
        status = color_text("[x]", Colors.GREEN) if progress.get(task_id, False) else color_text("[ ]", Colors.RED)
        print(f"{task_id}. {status} {task_name}")

def clear_screen():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print("\033c", end="")

def main():
    tasks = load_tasks()
    progress = load_progress()

    while True:
        # Limpa a tela antes de mostrar o menu
        os.system("cls" if os.name == "nt" else "clear")

        display_menu(tasks, progress)

        choice = input("Selecione uma tarefa pelo número para alternar (ou 'q' para sair): ")

        if choice.lower() == "q":
            save_progress(progress)
            print(color_text("Progresso salvo! Até mais 👋", Colors.CYAN))
            break

        if choice in tasks:
            progress[choice] = not progress.get(choice, False)
            save_progress(progress)
        else:
            print(color_text("Opção inválida!", Colors.RED))

if __name__ == "__main__":
    main()
