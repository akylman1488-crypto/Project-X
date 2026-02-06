class EmotionAnalyzer:
    def __init__(self):
        self.state = "neutral"

    def analyze(self, text):
        text = text.lower()
        if any(w in text for w in ['bad', 'sad', 'wrong', 'stupid']):
            self.state = "concerned"
        elif any(w in text for w in ['good', 'great', 'thanks', 'wow']):
            self.state = "happy"
        else:
            self.state = "neutral"
        return self.state

    def get_prompt_suffix(self):
        if self.state == "happy": return " (Reply enthusiastically)"
        if self.state == "concerned": return " (Reply carefully and apologetically)"
        return ""
