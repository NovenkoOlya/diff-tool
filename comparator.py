import os

def read_file_lines(file_path):
    """Зчитує унікальні рядки з файлу, видаляючи зайві пробіли."""
    if not os.path.exists(file_path):
        return set()
    with open(file_path, 'r', encoding='utf-8') as f:
        return {line.strip() for line in f if line.strip()}