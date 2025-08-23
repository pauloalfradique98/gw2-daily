import json
import os

# --- Funções para carregar e salvar dados ---

def load_tasks():
    with open("tasks.json", "r", encoding="utf-8") as f:
        return json.load(f)

def load_progress():
    if not os.path.exists("progress.json"):
        return []
    with open("progress.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_progress(progress):
    with open("progress.json", "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2, ensure_ascii=False)

# --- Funções principais ---

def show_tasks(tasks, progress):
    done_ids = {p["id"] for p in progress}
    print("\n===== Rotina Diária GW2 =====")
    for task in tasks:
        status = "[x]" if task["id"] in done_ids else "[ ]"
        print(f"{task['id']}. {task['name']} {status}")

def mark_tasks(task_ids, progress):
    for task_id in task_ids:
        if not any(p["id"] == task_id for p in progress):
            progress.append({"id": task_id, "done": True})
    return progress

def reset_progress():
    save_progress([])
    print("✅ Progresso resetado!")

def gerar_relatorio(tasks, progress):
    done_ids = {p["id"] for p in progress}
    relatorio = ["===== Relatório Diário GW2 =====\n"]
    for task in tasks:
        status = "[x]" if task["id"] in done_ids else "[ ]"
        relatorio.append(f"{task['id']}. {task['name']} {status}")
    # Salva em arquivo txt
    with open("relatorio.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(relatorio))
    print("📄 Relatório salvo em relatorio.txt")

# --- Execução do programa ---

if __name__ == "__main__":
    tasks = load_tasks()
    progress = load_progress()

    show_tasks(tasks, progress)

    print("\nOpções:")
    print(" - Digite números separados por vírgula para marcar (ex: 2,4,5)")
    print(" - Digite R para resetar o progresso")
    print(" - Digite G para gerar relatório")
    print(" - ENTER para sair")

    choice = input("\nSua escolha: ").strip()

    if choice.upper() == "R":
        reset_progress()
    elif choice.upper() == "G":
        gerar_relatorio(tasks, progress)
    elif choice:
        try:
            task_ids = [int(x.strip()) for x in choice.split(",") if x.strip().isdigit()]
            progress = mark_tasks(task_ids, progress)
            save_progress(progress)
            print("✅ Progresso salvo com sucesso!")
        except ValueError:
            print("⚠️ Entrada inválida. Use números separados por vírgula.")
