import os
import tempfile
import shutil
import pytest

from .search import get_text_files_content

# PUBLIC_INTERFACE
def test_get_text_files_content_reads_text_based_files():
    """
    Test that get_text_files_content correctly reads content from .txt, .py, .md, .json files in a folder.
    This test creates a temporary directory with multiple files, including supported and unsupported extensions.
    """
    temp_dir = tempfile.mkdtemp()
    try:
        # Create sample files
        supported_files = {
            "a.txt": "Alpha text content",
            "b.py": "print('Hello World!')",
            "c.md": "# Markdown Title",
            "d.json": '{"key": "value"}'
        }
        unsupported_files = {
            "e.jpg": "not a text file",
            "f.exe": "executable code"
        }

        for fname, content in supported_files.items():
            with open(os.path.join(temp_dir, fname), "w", encoding="utf-8") as f:
                f.write(content)
        for fname, content in unsupported_files.items():
            with open(os.path.join(temp_dir, fname), "w", encoding="utf-8") as f:
                f.write(content)

        # Call the function
        result = get_text_files_content(temp_dir)
        found_files = {filename for filename, _ in result}

        # It should only include files with supported extensions and skip the rest
        assert found_files == set(supported_files.keys())
        result_dict = dict(result)
        for fname, expected_content in supported_files.items():
            assert result_dict[fname] == expected_content

    finally:
        shutil.rmtree(temp_dir)

# PUBLIC_INTERFACE
def test_get_text_files_content_returns_empty_when_no_supported_files():
    """
    Test that get_text_files_content returns an empty list if no supported files exist in the directory.
    """
    empty_dir = tempfile.mkdtemp()
    try:
        # Only unsupported file
        with open(os.path.join(empty_dir, "data.bin"), "w", encoding="utf-8") as f:
            f.write("fake binary content")

        result = get_text_files_content(empty_dir)
        assert result == []
    finally:
        shutil.rmtree(empty_dir)

# PUBLIC_INTERFACE
def test_get_text_files_content_handles_file_read_errors_gracefully(monkeypatch):
    """
    Test that get_text_files_content skips files that cannot be read (simulated with monkeypatch).
    """
    temp_dir = tempfile.mkdtemp()
    try:
        supported = os.path.join(temp_dir, "sample.txt")
        with open(supported, "w", encoding="utf-8") as f:
            f.write("hello")

        # Simulate permission error with monkeypatch if possible
        original_open = open
        def raising_open(*args, **kwargs):
            if args[0].endswith("sample.txt"):
                raise PermissionError("Simulated permission error")
            return original_open(*args, **kwargs)
        monkeypatch.setattr("builtins.open", raising_open)

        result = get_text_files_content(temp_dir)
        assert result == [], "Expected empty because reading caused PermissionError"
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    pytest.main([__file__])
