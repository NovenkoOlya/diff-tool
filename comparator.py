import os

def read_file_lines(file_path):
    """Зчитує унікальні рядки з файлу, видаляючи зайві пробіли."""
    if not os.path.exists(file_path):
        return set()
    with open(file_path, 'r', encoding='utf-8') as f:
        return {line.strip() for line in f if line.strip()}
    
def get_intersections(set1, set2):
    """Повертає спільні рядки."""
    return set1.intersection(set2)

def get_differences(set1, set2):
    """Повертає унікальні для обох файлів рядки (симетрична різниця)."""
    return set1.symmetric_difference(set2)

def write_to_file(file_path, lines):
    """Записує список рядків у файл."""
    with open(file_path, 'w', encoding='utf-8') as f:
        for line in sorted(lines):
            f.write(f"{line}\n")

def main(file1, file2):
    lines1 = read_file_lines(file1)
    lines2 = read_file_lines(file2)
    
    same = get_intersections(lines1, lines2)
    diff = get_differences(lines1, lines2)
    
    write_to_file("same.txt", same)
    write_to_file("diff.txt", diff)

if __name__ == "__main__":
    main("file1.txt", "file2.txt")