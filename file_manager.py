from pathlib import Path
from config import config
from logger import sys_logger

class FileTool:
    def __init__(self):
        self.workspace = config.WORKSPACE_DIR

    def write_file(self, filename, content):
        try:
            path = self.workspace / filename
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            sys_logger.log(f"File written: {filename}")
            return f"Success: Saved {filename}"
        except Exception as e:
            sys_logger.error(f"Write error: {e}")
            return "Error writing file."

    def read_file(self, filename):
        try:
            path = self.workspace / filename
            if not path.exists():
                return "Error: File not found."
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            sys_logger.error(f"Read error: {e}")
            return "Error reading file."
            
    def list_files(self):
        return [f.name for f in self.workspace.iterdir() if f.is_file()]
