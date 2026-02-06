from llm_engine import LLMHandler
from config import config

class TaskPlanner:
    def __init__(self):
        pass

    def create_plan(self, user_input, context, memory):
        plan = []
        user_input = user_input.lower()
        
        if "search" in user_input or "find" in user_input or "who is" in user_input:
            plan.append(f"search: {user_input}")
        
        if "write code" in user_input or "python" in user_input:
            plan.append(f"code: {user_input}")
            
        if "save" in user_input:
            plan.append("file_save")
            
        return plan
