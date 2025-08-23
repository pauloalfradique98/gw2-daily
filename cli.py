import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"
PROGRESS_FILE = "progress.json"


def load_tasks():
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return create_new_progress()

    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        progress = json.load(f)

    today = datetime.today().strftime("%Y-%m-%d")
    if progress.get("date") != today:
        return create_new_progress(today)
    return progress


def create_new_progress(date=None):
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
        json.dump(progress, f, indent=4, ensure_ascii=False)


def show_routines(tasks, progress):
    today_tasks = progress["tasks"]
    completed = sum(1 for done in today_tasks.values() if done)
    total = len(today_tasks)

    print("\n" + "="*30)
    print(f" GW2 Daily Routine — {progress['date']}")
    print("="*30)

    for task in tasks:
        status = "[x]" if today_tasks[str(task["id"])] else "[ ]"
        print(f"{task['id']}. {status} {task['name']}")

    print(f"\nProgresso do dia: {completed}/{total} concluídas")
    print("="*30 + "\n")


def toggle_task(progress, task_id, tasks):
    task_id = str(task_id)
    today_tasks = progress["tasks"]

    if task_id in today_tasks:
        today_tasks[task_id] = not today_tasks[task_id]
        save_progress(progress)

        # Mensagem motivacional
        task_name = next(task["name"] for task in tasks if str(task["id"]) == task_id)
        if today_tasks[task_id]:
            print(f"✔️  {task_name} concluída!")
        else:
            print(f"❌  {task_name} desmarcada!")
    else:
        print("ID inválido.")


def main():
    tasks = load_tasks()
    progress = load_progress()

    while True:
        show_routines(tasks, progress)
        choice = input("Digite o ID da tarefa para marcar/desmarcar (ou 'q' para sair): ").strip()

        if choice.lower() == "q":
            print("Até mais! Progresso do dia salvo.")
            break
        elif choice.isdigit():
            toggle_task(progress, int(choice), tasks)
        else:
            print("Entrada inválida! Digite um número ou 'q' para sair.")


if __name__ == "__main__":
    main()
