import pytest
import os
from comparator import get_intersections, get_differences, read_file_lines

@pytest.fixture
def temp_files(tmp_path):
    """Фікстура для створення тимчасових тестових файлів."""
    f1 = tmp_path / "test1.txt"
    f2 = tmp_path / "test2.txt"
    f1.write_text("apple\nbanana\ncherry", encoding="utf-8")
    f2.write_text("banana\ndate\ncherry", encoding="utf-8")
    return f1, f2