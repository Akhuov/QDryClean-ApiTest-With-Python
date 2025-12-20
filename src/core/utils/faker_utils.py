import random
import string

def generate_random_email(domain="example.com", length=8):
    # Generate a random string of given length
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{username}@{domain}"

def generate_random_text(name:str=None,length=10):
    random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return f'{name}-{random_text}' if name is not None else random_text
