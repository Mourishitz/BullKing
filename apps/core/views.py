import string
import random


def generate_random_password():
    characters = list(string.ascii_letters + string.digits)
    sp_char = list("!@#$%^&*()")
    length = 10
    random.shuffle(characters+sp_char)
    da_password = []
    for i in range(length):
        da_password.append(random.choice(characters+sp_char))
    random.shuffle(da_password)
    return("".join(da_password))
