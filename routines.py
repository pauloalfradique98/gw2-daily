from data import load_json, save_json

TASKS_FILE = "tasks.json"
PROGRESS_FILE = "progress.json"

def load_tasks() -> dict:
    return load_json(TASKS_FILE)

def load_progress() -> dict:
    return load_json(PROGRESS_FILE)

def save_progress(progress: dict) -> None:
    save_json(PROGRESS_FILE, progress)

def toggle_task(progress: dict, task_id: str) -> dict:
    """
    Alterna o status de uma tarefa (True/False).
    """
    if task_id in progress:
        progress[task_id] = not progress[task_id]
    return progress
