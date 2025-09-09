import subprocess
import random
import datetime

# 0% descansos para actividad constante todos los días
REST_PROBABILITY = 0.0

# Correo registrado en la cuenta de GitHub
GIT_EMAIL = "adrianjesus1209@gmail.com"
GIT_NAME = "adrianjesus1209-beep"

COMMIT_MESSAGES = [
    "docs: update activity log",
    "chore: routine maintenance check",
    "refactor: clean up activity log",
    "style: format log output",
    "ci: update daily activity workflow",
    "fix: patch daily activity sync",
    "feat: enhance activity tracking"
]

def run_git_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar '{' '.join(command)}': {e.stderr.strip()}")

def main():
    if random.random() < REST_PROBABILITY:
        print("Día de descanso. No se realizarán commits.")
        return

    # Configurar identidad con el correo verificado de GitHub
    run_git_command(["git", "config", "user.name", GIT_NAME])
    run_git_command(["git", "config", "user.email", GIT_EMAIL])

    # Generar entre 4 y 10 commits diarios para verde intenso
    num_commits = random.randint(4, 10)
    print(f"Hoy se realizarán {num_commits} commit(s).")

    for i in range(num_commits):
        now_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        with open("activity_log.txt", "a", encoding="utf-8") as f:
            f.write(f"Registro de actividad: {now_str}\n")
        
        commit_msg = random.choice(COMMIT_MESSAGES)
        run_git_command(["git", "add", "activity_log.txt"])
        run_git_command(["git", "commit", "-m", commit_msg, "--author", f"{GIT_NAME} <{GIT_EMAIL}>"])

    run_git_command(["git", "push"])

if __name__ == "__main__":
    main()
