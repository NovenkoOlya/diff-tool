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

@pytest.mark.parametrize("set1, set2, expected", [
    ({"line1", "line2"}, {"line2", "line3"}, {"line2"}),
    ({"a"}, {"b"}, set()),
    (set(), {"a"}, set())
])

def test_get_intersections(set1, set2, expected):
    assert get_intersections(set1, set2) == expected

@pytest.mark.parametrize("set1, set2, expected", [
    ({"line1", "line2"}, {"line2", "line3"}, {"line1", "line3"}),
    ({"a"}, {"a"}, set()),
    ({"a"}, set(), {"a"})
])
def test_get_differences(set1, set2, expected):
    assert get_differences(set1, set2) == expected