import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"
PROGRESS_FILE = "progress.json"


def load_tasks():
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_progress():
    # Se não existir progresso, cria novo
    if not os.path.exists(PROGRESS_FILE):
        return create_new_progress()

    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        progress = json.load(f)

    today = datetime.today().strftime("%Y-%m-%d")

    # Se a data mudou → resetar
    if progress.get("date") != today:
        return create_new_progress(today)

    return progress


def create_new_progress(date=None):
    """Cria progresso zerado para o dia atual"""
    tasks = load_tasks()
    today = date or datetime.today().strftime("%Y-%m-%d")
    progress = {
        "date": today,
        "tasks": {str(task["id"]): False for task in tasks}
    }
    save_progress(progress)
    return progress


def save_progress(progress):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=4)


def show_routines(tasks, progress):
    print("\n===== Daily Routine Tracker =====")
    completed = 0
    for task in tasks:
        status = "[x]" if progress["tasks"][str(task["id"])] else "[ ]"
        if progress["tasks"][str(task["id"])]:
            completed += 1
        print(f"{task['id']}. {status} {task['name']}")
    print(f"\nProgresso: {completed}/{len(tasks)} concluídas\n")


def toggle_task(progress, task_id):
    task_id = str(task_id)
    if task_id in progress["tasks"]:
        progress["tasks"][task_id] = not progress["tasks"][task_id]
        save_progress(progress)
        print(f"Tarefa {task_id} atualizada!")
    else:
        print("ID inválido.")


def main():
    tasks = load_tasks()
    progress = load_progress()

    while True:
        show_routines(tasks, progress)
        choice = input("Digite o ID da tarefa para marcar/desmarcar (ou 'q' para sair): ")

        if choice.lower() == "q":
            break
        elif choice.isdigit():
            toggle_task(progress, int(choice))
        else:
            print("Entrada inválida!")


if __name__ == "__main__":
    main()
