import pyttsx3
import threading
from logger import sys_logger

class VoiceTool:
    def __init__(self):
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 160)
            self.is_speaking = False
        except:
            self.engine = None
            sys_logger.error("Voice engine failed to init.")

    def speak(self, text):
        if not self.engine: return
        
        def _run():
            self.is_speaking = True
            self.engine.say(text)
            self.engine.runAndWait()
            self.is_speaking = False
            
        thread = threading.Thread(target=_run)
        thread.start()

    def listen(self):
        return "Listening feature placeholder"
