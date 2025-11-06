dir_path = r'C:\Users\bbirajda\Downloads' 
attachments = [
    f'{dir_path}/IMG-20251024-WA0119.jpg',
]
from mail import send_gmail_attach
from config import to_address 
result = send_gmail_attach(to_address, "First Day in Cisco - 06-11-2025 - Photo", "Hello from Bibhishan!", attachments)
print("Mail sent successfully?" , result)