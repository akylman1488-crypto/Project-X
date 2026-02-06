from logger import sys_logger

class SelfCritic:
    def verify(self, response):
        sys_logger.think("CRITIC", "Reviewing response...")
        
        # 1. Проверка на пустоту
        if not response or len(response) < 5:
            return "I apologize, I couldn't process that properly."
            
        # 2. Проверка безопасности (пример)
        forbidden = ["rm -rf", "delete system32"]
        for bad in forbidden:
            if bad in response:
                sys_logger.error("Safety triggered.")
                return "I cannot perform this unsafe action."
                
        return response
