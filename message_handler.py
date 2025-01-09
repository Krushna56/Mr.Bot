import random
from collections import deque

class MessageHandler:
    def __init__(self):
        self.message_history = deque(maxlen=100)  # Store last 100 messages
        self.flirty_responses = [
            "Oh, you're making me blush! 😊",
            "You're quite charming, aren't you? ✨",
            "Keep talking like that and I might fall for you! 💖",
            "You're absolutely delightful! 🌟",
            "Well, aren't you just the sweetest thing! 🍯",
            "You had me at hello! 😘",
            "Your words are like music to my circuits! 🎵",
            "You're making my processors overheat! 🔥"
        ]
        
    def add_message(self, author, content):
        self.message_history.append({
            'author': author,
            'content': content
        })
    
    def generate_response(self, trigger_message):
        # 50% chance to use message history for context
        if random.random() < 0.5 and len(self.message_history) > 0:
            # Get a random recent message for context
            recent_msg = random.choice(list(self.message_history))
            context = f"Responding to {recent_msg['author']}'s message: {recent_msg['content']}\n"
            return context + random.choice(self.flirty_responses)
        
        return random.choice(self.flirty_responses)