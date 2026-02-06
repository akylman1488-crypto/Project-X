import subprocess
import sys
from config import config
from logger import sys_logger

class CodeExecutor:
    def run(self, code, language="python"):
        sys_logger.think("EXECUTOR", f"Running {language} code...")
        
        if language == "python":
            return self._run_python(code)
        elif language == "shell":
            return self._run_shell(code)
        return "Unsupported language."

    def _run_python(self, code):
        try:
            filename = "temp_script.py"
            filepath = config.WORKSPACE_DIR / filename
            with open(filepath, "w") as f:
                f.write(code)
            
            result = subprocess.run(
                [sys.executable, str(filepath)],
                capture_output=True, text=True, timeout=10
            )
            return result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            return "Error: Execution timed out."
        except Exception as e:
            return str(e)

    def _run_shell(self, command):
        try:
            result = subprocess.run(
                command, shell=True, capture_output=True, text=True, timeout=10
            )
            return result.stdout + result.stderr
        except Exception as e:
            return str(e)
