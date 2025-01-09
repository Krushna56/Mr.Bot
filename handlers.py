import random
from collections import deque
from .utils.responses import flirty_responses

class MessageHandler:
    def __init__(self):
        self.message_history = deque(maxlen=100)
    
    def add_message(self, author, content):
        self.message_history.append({
            'author': author,
            'content': content
        })
    
    def generate_response(self, trigger_message):
        if random.random() < 0.5 and len(self.message_history) > 0:
            recent_msg = random.choice(list(self.message_history))
            context = f"Responding to {recent_msg['author']}'s message: {recent_msg['content']}\n"
            return context + random.choice(flirty_responses)
        
        return random.choice(flirty_responses)
    
    async def handle_message(self, message):
        self.add_message(message.author.name, message.content)
        
        if random.random() < 0.3:
            response = self.generate_response(message.content)
            await message.channel.send(response)