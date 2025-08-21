# The Dependency Inversion Principle (DIP) states that high-level modules should not depend on 
# low-level modules, but both should depend on abstractions. 
# It ensures that code is flexible, reusable, and easy to maintain.

# In traditional programming, a high-level class (like a service) directly 
# depends on a low-level class (like a database or file system).

# This creates tight coupling, meaning if the low-level class changes, the high-level class breaks.

# DIP suggests we should depend on interfaces or abstract classes instead of concrete implementations.

# This way, the high-level module only knows about the abstraction, not the actual implementation.

# This makes the system more scalable, testable, and loosely coupled.

class MessageSender:
    def send(self, message):
        raise NotImplementedError("Subclass must implement send method")
    
class EmailSender(MessageSender):
    def send(self, message):
        print("Sending Email:", message)

class SMSSender(MessageSender):
    def send(self, message):
         print("Sending SMS:", message)

class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)

email_service = NotificationService(EmailSender())
email_service.notify("Hello via Email!")

sms_service = NotificationService(SMSSender())
sms_service.notify("Hello via SMS!")
        
