import os


def save_blueprint(content, session_id):

    folder_path = f"generated_projects/{session_id}"
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, "architecture.md")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return file_path


def save_full_code(content, session_id):

    folder_path = f"generated_projects/{session_id}"
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, "full_code.md")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return file_path